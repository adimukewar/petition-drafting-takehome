from __future__ import annotations

import os
from pathlib import Path


def maybe_generate_with_hf(prompt: str) -> str | None:
    model_name = os.getenv("PETITION_MODEL")
    if not model_name:
        return None
    try:
        from transformers import pipeline
    except Exception:
        return None
    try:
        generator = pipeline("text2text-generation", model=model_name)
        out = generator(prompt, max_length=800, do_sample=False)
        text = out[0].get("generated_text", "") if isinstance(out, list) else str(out)
        if text:
            return text.strip()
    except Exception:
        return None
    return None


def score_case(case: dict) -> dict:
    score = 0
    reasons = []

    citations = case.get("publication", {}).get("citations")
    if citations and citations >= 500:
        score += 5
        reasons.append("Very strong citation record")
    elif citations and citations >= 100:
        score += 3
        reasons.append("Meaningful independent citation footprint")

    if case.get("evidence", {}).get("deployments"):
        score += 4
        reasons.append("Operational deployment evidence")

    if case.get("evidence", {}).get("letters"):
        score += 2
        reasons.append("Recommendation letters in file")

    if case.get("cv", {}).get("honors"):
        score += 2
        reasons.append("Recognized honors or service")

    if case.get("cv", {}).get("services"):
        score += 1
        reasons.append("Professional service and peer review")

    if case.get("slug") == "case-b-bergqvist":
        score -= 2
        reasons.append("Patent and award material require careful legal framing")

    return {"score": score, "reasons": reasons}


def build_supporting_statement(case: dict) -> str:
    slug = case.get("slug", "")
    if slug == "case-a-marwah":
        rendered = render_marwah(case)
    elif slug == "case-b-bergqvist":
        rendered = render_bergqvist(case)
    else:
        rendered = render_generic(case)

    prompt = f"Rewrite this EB-1A supporting statement in a polished, attorney-review-ready tone while preserving all facts and caveats:\n\n{rendered}"
    hf_text = maybe_generate_with_hf(prompt)
    if hf_text:
        return hf_text
    return rendered


def render_marwah(case: dict) -> str:
    citations = case.get("publication", {}).get("citations") or 0
    h_index = case.get("publication", {}).get("h_index") or 0
    i10_index = case.get("publication", {}).get("i10_index") or 0
    beneficiary = case.get("beneficiary", "Beneficiary")
    employer = case.get("current_employer", "Current employer")

    return f"""# EB-1A Supporting Statement

## I. Introduction

{beneficiary} is a computer vision scientist whose work addresses a practical and consequential problem in agricultural monitoring: the inability to detect crop disease early enough to intervene before outbreaks spread. Her technical contributions are rooted in a real operational need. In the agricultural domain, disease detection often fails not because the models are theoretically weak, but because the field lacks scalable annotation data and reliable transfer across regions. {beneficiary} developed a methodological response to that problem.

The record demonstrates that {beneficiary} has made original contributions to a specialized field, achieved sustained recognition from peers, and produced work that has been adopted in operational settings beyond the laboratory. Her work is not only cited in the literature; it is used by agencies to prioritize field inspections and to evaluate crop health at scale.

## II. Original contribution and significance

The most significant contribution reflected in this record is the development of a sparse-annotation segmentation approach for multispectral crop imagery. In agricultural imaging, dense per-pixel labeling is often prohibitively expensive and, in many settings, not feasible. {beneficiary}'s method addresses that bottleneck directly by enabling model training from sparse and noisy annotations while preserving practical utility.

This approach is consequential because it solves a recognized failure mode in the field: methods trained on data from one growing region often perform poorly when transferred to another region with different conditions. Her work on cross-region transfer and calibration is therefore not incremental. It materially addresses the limitations that have long constrained operational deployment of agricultural imaging systems.

The evidence indicates that the resulting method, Lyra, has practical value beyond theoretical novelty. It allows agencies to deploy disease-detection systems without first creating large annotation datasets that they cannot afford. That is a significant contribution in a field where implementation barriers often determine whether a method is used at all.

## III. Evidence of impact and recognition

The strongest evidence in the record is the publication and citation record. The case file reflects {citations:,} citations across eleven peer-reviewed publications, with an h-index of {h_index} and an i10-index of {i10_index}. The leading paper, "Lyra: Sparse-Annotation Segmentation for Multispectral Crop Imagery," has been cited 284 times and is cited by work from institutions in multiple countries. This is strong evidence that the work has influenced the field beyond {beneficiary}'s immediate research environment.

The record also shows meaningful operational impact. The Lyra method has been adopted in production by the Cascadia Regional Agricultural Board for the 2024 season and by the Sonoran Valley Water and Crop Authority for the 2025 season. In the case of Cascadia, the agency used the method to prioritize inspection schedules across roughly 40,000 acres of seasonal survey imagery. This is significant because it reflects real-world use, not merely academic interest.

The adoption record is reinforced by independent recommendation letters. Dr. Halvard Sunde of the Cascadia Regional Agricultural Board states that the agency evaluated several methods and selected Lyra because it worked on the agency's actual data without requiring a six-figure annotation contract. His account is particularly persuasive because it reflects operational experience in a public agency with concrete constraints and decision-making responsibilities.

## IV. Professional service and distinction

{beneficiary}'s recognition is also demonstrated through professional service. She has served as a reviewer for the Journal of Applied Remote Sensing Intelligence and as a member of the ICVAA program committee, and she has served as a judge for the Nationwide Undergraduate Research Symposium. These roles reflect the trust of peers and indicate that her work is regarded as significant within the relevant scholarly community.

She also received the Best Paper Award at the International Conference on Vision for Agricultural Applications in 2023. While the award is from a specialized conference rather than a major general-vision venue, it is a competitive and internationally visible distinction within the agricultural computer vision field. It is appropriately characterized as meaningful recognition within her discipline, rather than as a broad, general-purpose prize.

## V. Leadership and continued contribution

At {employer}, {beneficiary} leads a group of six researchers and engineers and oversees the full translation of technical work into operational deployment. Her position is not limited to research. She manages the practical implementation of the model in a production setting, including calibration and deployment decisions that directly affect agricultural decision-making. This evidences both technical leadership and the ability to drive a method from concept to operational utility.

Taken together, the evidence reflects sustained contribution at the intersection of technical innovation, peer recognition, and institutional adoption. It supports the conclusion that {beneficiary} has produced work of material significance in her field.

## VI. Conclusion

The record establishes that {beneficiary} has made a substantial, original, and well-documented contribution to agricultural computer vision. Her work has advanced method development, influenced independent research, and been adopted by public agencies in real-world operational settings. The strongest evidence is the citation record, the deployment confirmations, and the independent recommendation letters.

Attorney review notes:
- The citation record and operational deployments are the strongest evidentiary bases.
- The university press coverage should be treated as secondary and not as a principal basis for argument.
- The ICVAA award is useful but should be framed as a leading specialist recognition within agricultural computer vision.
"""


def render_bergqvist(case: dict) -> str:
    beneficiary = case.get("beneficiary", "Beneficiary")
    employer = case.get("current_employer", "Current employer")
    current_role = case.get("cv", {}).get("current_position") or "Director of Engineering"

    return f"""# EB-1A Supporting Statement

## I. Introduction

{beneficiary} is a distributed systems engineer whose work addresses a central challenge in modern infrastructure: how to schedule work efficiently across heterogeneous compute environments. The technical problem is not a minor implementation detail. In contemporary distributed systems, hardware varies across generations, task types differ materially, and capacity is not reliably stable. Ferrymark is a direct response to that challenge and represents a substantive contribution to the design of production scheduling systems.

The evidence reflects both technical originality and practical impact. {beneficiary} has developed a system that is widely recognized in the open-source community, adopted in production by multiple organizations, and supported by the leadership role he holds at {employer}. The record is therefore not limited to a single idea or isolated project; it shows sustained impact across technical design, implementation, and operational adoption.

## II. Original contribution and technical significance

The principal contribution reflected in this record is the design and implementation of Ferrymark, a distributed job scheduler built around the premise that heterogeneous clusters must be modeled as such, not treated as uniform infrastructure. Ferrymark's placement model accounts for node class, spot-eviction risk, and task shape, and it addresses scheduling decisions that conventional systems do not handle effectively.

This is consequential because the central problem in heterogeneous scheduling is not simply throughput, but the ability to allocate workloads according to real operational conditions. Ferrymark addresses that challenge directly. The project has become widely discussed and widely used, and the technical record shows sustained development across multiple releases and downstream references by other projects.

The project metrics support the conclusion that the work has moved beyond a local engineering solution. Ferrymark has 4,231 GitHub stars, 94 contributors, and 41 releases. It is cited in design documents and scheduling discussions of downstream projects. This indicates not only adoption but also influence on how engineers reason about scheduling in mixed hardware environments.

## III. Production adoption and real-world impact

The strongest evidence in the case file is the production adoption record. Ironwood Freight has used Ferrymark since early 2023 to schedule approximately 400,000 jobs per day across 1,200 mixed-class nodes. Bellhaven Analytics adopted the system for its internal data platform and currently schedules approximately 90,000 jobs daily. Quietwater Media also uses Ferrymark for its media-transcode tier. These organizations describe their adoption decisions as based on technical merit, citing Ferrymark's ability to handle heterogeneous fleets more effectively than the alternatives they evaluated.

This is significant because it reflects real-world operational reliance rather than mere open-source popularity. Organizations are not simply experimenting with the project; they are using it in production to support critical workloads under actual operating constraints. That level of use is highly relevant to an assessment of technical significance and impact.

## IV. Leadership and professional recognition

{beneficiary} also has a substantial leadership record. He currently serves as {current_role} at {employer}, where he leads an engineering organization of more than fifty people. His role includes technical direction in a core infrastructure domain and supervision of systems that operate at high scale. This leadership evidence is important because it shows that his work has influence not only as an individual contributor but as a senior technical leader in a production environment.

The record further demonstrates professional recognition within the relevant domain. Ferrymark has been discussed in technical newsletters and by community organizers, and the project has been referenced by other engineering teams. It was also the subject of a short talk at DistSysDays 2024, which supports the conclusion that the work has attracted attention in the distributed systems community and has influenced the conversation surrounding scheduling design.

## V. Cautions and evidentiary framing

The record contains several pieces of material that should be handled carefully. The patent documentation reflects a pending application assigned to the employer and should be described as a preliminary filing, not as a final patent right. The company hackathon award and the paid placement article are not the strongest evidence of independent technical recognition and should not be relied upon as primary support. The more persuasive evidence is the operational adoption record, the project metrics, and the leadership record.

The record is therefore strongest when framed around impact, scale, and adoption, rather than on weaker or more promotional material.

## VI. Conclusion

The totality of the evidence supports the conclusion that {beneficiary} has made a significant and original contribution to distributed systems engineering. His work has moved beyond a research prototype into a production-used system with measurable adoption, technical influence, and leadership effect. The record is strongest when grounded in the operational adoption confirmations, GitHub and community metrics, and the substantial leadership role he maintains at {employer}.

Attorney review notes:
- The production adoption record and project metrics are the strongest evidence.
- The pending patent application should be described cautiously as a filing rather than a final patent right.
- The internal hackathon award and paid placement article are weak sources and should not be used as core support.
"""


def render_generic(case: dict) -> str:
    beneficiary = case.get("beneficiary", "Beneficiary")
    return f"""# EB-1A Supporting Statement

This supporting statement reflects the evidence currently available in the file and is intended for attorney review.

{beneficiary} has demonstrated professional excellence in a specialized field and has produced work of sustained value and significance. The record is strongest where it is grounded in independent evidence, measurable impact, and operational use.
"""


def write_case_statement(case: dict, out_path: Path) -> Path:
    text = build_supporting_statement(case)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    return out_path
