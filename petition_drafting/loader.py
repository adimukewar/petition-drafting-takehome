from __future__ import annotations

from pathlib import Path
import re


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalize_text(value: str | None) -> str | None:
    if value is None:
        return None
    cleaned = value.strip().replace("**", "").replace("*", "")
    cleaned = cleaned.replace("\n", " ")
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.strip()


def clean_name(value: str | None) -> str | None:
    if value is None:
        return None
    cleaned = normalize_text(value)
    if not cleaned:
        return None
    cleaned = re.sub(r"^(Dr\.|Mr\.|Ms\.|Prof\.)\s+", "", cleaned)
    cleaned = cleaned.split(",")[0]
    cleaned = cleaned.split(" — ")[0]
    return cleaned.strip()


def clean_employer(value: str | None) -> str | None:
    if value is None:
        return None
    cleaned = normalize_text(value)
    if not cleaned:
        return None
    cleaned = cleaned.split(" — ")[0]
    cleaned = cleaned.split(",")[0]
    return cleaned.strip()


def extract_case_notes(case_dir: Path) -> dict:
    notes = read_text(case_dir / "00-case-notes.md")
    meta = {
        "slug": case_dir.name,
        "title": case_dir.name,
        "beneficiary": None,
        "classification": None,
        "current_status": None,
        "current_employer": None,
        "summary": None,
    }

    beneficiary_match = re.search(r"Beneficiary:\s*(.+)", notes)
    if beneficiary_match:
        meta["beneficiary"] = clean_name(beneficiary_match.group(1))

    classification_match = re.search(r"Classification sought:\s*(.+)", notes)
    if classification_match:
        meta["classification"] = normalize_text(classification_match.group(1))

    status_match = re.search(r"Current status:\s*(.+)", notes)
    if status_match:
        meta["current_status"] = normalize_text(status_match.group(1))

    employer_match = re.search(r"Current employer:\s*(.+)", notes)
    if employer_match:
        meta["current_employer"] = clean_employer(employer_match.group(1))

    summary_match = re.search(r"## Summary\n\n(.+?)\n\n## Evidence gathered", notes, re.S)
    if summary_match:
        summary = summary_match.group(1).strip().replace("\n", " ")
        meta["summary"] = summary

    return meta


def extract_cv_summary(case_dir: Path) -> dict:
    cv = read_text(case_dir / "01-cv.md")
    summary = {
        "current_position": None,
        "education": [],
        "publications": None,
        "honors": [],
        "services": [],
        "languages": [],
    }

    current_position_match = re.search(r"## Current Position\s+\*\*(.+?)\*\*", cv, re.S)
    if current_position_match:
        summary["current_position"] = normalize_text(current_position_match.group(1))

    education_match = re.findall(r"\*\*(.+?)\*\*", cv)
    for value in education_match:
        v = normalize_text(value)
        if v and v not in {summary.get("current_position"), "Current Position", "Previous Positions", "Summary"}:
            summary["education"].append(v)

    if "peer-reviewed publications" in cv.lower():
        summary["publications"] = "Peer-reviewed publication record available"

    honors = re.findall(r"- \*\*(.+?)\*\*", cv)
    summary["honors"] = [normalize_text(h) for h in honors if normalize_text(h)]

    languages = re.findall(r"([A-Za-z][A-Za-z\-]+)\s*\(.*?\)", cv)
    summary["languages"] = [normalize_text(lang) for lang in languages if normalize_text(lang)]

    summary["services"] = list(summary["honors"])
    return summary


def extract_publication_record(case_dir: Path) -> dict:
    publication_file = case_dir / "03-publication-record.md"
    if not publication_file.exists():
        return {"citations": None, "h_index": None, "i10_index": None}

    text = read_text(publication_file)
    citation_match = re.search(r"\*\*Total citations:\*\*\s*([0-9,]+)\s*·\s*\*\*h-index:\*\*\s*([0-9]+)\s*·\s*\*\*i10-index:\*\*\s*([0-9]+)", text)
    if citation_match:
        return {
            "citations": int(citation_match.group(1).replace(",", "")),
            "h_index": int(citation_match.group(2)),
            "i10_index": int(citation_match.group(3)),
        }

    citation_match = re.search(r"Total citations:\s*([0-9,]+)\s*·\s*h-index:\s*([0-9]+)\s*·\s*i10-index:\s*([0-9]+)", text)
    if citation_match:
        return {
            "citations": int(citation_match.group(1).replace(",", "")),
            "h_index": int(citation_match.group(2)),
            "i10_index": int(citation_match.group(3)),
        }
    return {"citations": None, "h_index": None, "i10_index": None}


def extract_adoption_and_press(case_dir: Path) -> dict:
    result = {"deployments": [], "press": [], "letters": []}
    for path in sorted(case_dir.glob("*.md")):
        text = read_text(path)
        lower = text.lower()
        if "deployment" in lower and "deployment confirmations" in path.name.lower():
            result["deployments"].append(path.name)
        if "press coverage" in text.lower() or "press" in lower:
            result["press"].append(path.name)
        if "letter of recommendation" in text.lower():
            result["letters"].append(path.name)
    return result


def load_case(case_dir: Path) -> dict:
    notes = extract_case_notes(case_dir)
    cv = extract_cv_summary(case_dir)
    publication = extract_publication_record(case_dir)
    evidence = extract_adoption_and_press(case_dir)

    return {
        **notes,
        "cv": cv,
        "publication": publication,
        "evidence": evidence,
    }
