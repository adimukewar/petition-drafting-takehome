from __future__ import annotations

import subprocess
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

ROOT = Path(__file__).resolve().parent


def make_slide(path: Path, title: str, body: str, accent: str = "#5cc8ff") -> None:
    width, height = 1280, 720
    img = Image.new("RGB", (width, height), color="#0b1220")
    draw = ImageDraw.Draw(img)

    draw.rectangle((0, 0, 180, height), fill=accent)
    title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 54)
    body_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 32)

    draw.text((220, 80), title, fill="white", font=title_font)

    wrapped = textwrap.fill(body, width=40)
    y = 180
    for line in wrapped.split("\n"):
        draw.text((220, y), line, fill="#dfeafc", font=body_font)
        y += 42

    draw.text((220, 660), "Alma take-home: EB-1A drafting workflow", fill="#9cb5d3", font=body_font)
    img.save(path)


def main() -> None:
    ROOT.mkdir(exist_ok=True)

    slides = [
        (
            "Petition drafting system",
            "A repeatable workflow that reads case files, scores evidence quality, and produces a draft supporting statement for attorney review.",
        ),
        (
            "Case corpus parsing",
            "The system ingests intake notes, CVs, publications, letters, press, deployments, and other evidence into a structured case model.",
        ),
        (
            "Evidence quality scoring",
            "Strong sources are emphasized while weak material such as a pending patent, paid placement, or internal award is flagged or downweighted.",
        ),
        (
            "Draft generation + QA",
            "The generator writes a draft per case and keeps legal caveats in the output so the attorney can review the supporting statement with context.",
        ),
    ]

    for idx, (title, body) in enumerate(slides):
        make_slide(ROOT / f"slide_{idx}.png", title, body, accent=["#5cc8ff", "#8bd3b0", "#f7b267", "#d98cff"][idx])

    narration = (
        "Hi everyone. This is the petition drafting system we built for the Alma take-home. "
        "The goal is straightforward: take raw case files, extract the evidence, and turn that into a draft supporting statement for attorney review. "
        "We do not start from a blank page. We start from the facts already in the case folder. "
        "This repository contains two cases, Marwah and Bergqvist. The workflow reads the intake notes, the CV, the publication record, the recommendation letters, the press, and the deployment confirmations. "
        "It normalizes that information into a structured case model. "
        "The key design choice is that weak evidence is not treated as equal to strong evidence. "
        "A pending patent, an internal award, or a paid article is flagged or downweighted instead of being over-claimed in the final legal argument. "
        "Once the evidence is organized, the system generates a draft supporting statement for each case. "
        "The strongest items are emphasized: publication impact, operational deployments, peer review, and independent letters of recommendation. "
        "The draft also keeps attorney review notes so the lawyer can see the evidentiary limits and decide how to frame them. "
        "Finally, the workflow is repeatable through a simple UV setup. In the project root, we run uv sync and then the CLI against the cases folder. "
        "The outputs are generated under the outputs directory. "
        "The whole point is to stay conservative where the evidence is thin and to keep the final product grounded in verifiable facts. "
        "That is what makes it useful for legal drafting work."
    )

    audio_path = ROOT / "narration.aiff"
    subprocess.run(["say", "-o", str(audio_path.with_suffix("")), narration], check=True)

    image_files = []
    frame_repetitions = 24
    for idx in range(len(slides)):
        image_files.extend([str(ROOT / f"slide_{idx}.png")] * frame_repetitions)

    video = ImageSequenceClip(image_files, fps=1)
    audio = AudioFileClip(str(audio_path))
    video = video.with_duration(audio.duration)
    video = video.with_audio(audio)

    out_path = ROOT / "petition-drafting-demo.mp4"
    video.write_videofile(str(out_path), fps=30, codec="libx264", audio_codec="aac", bitrate="2500k")
    print(f"Created {out_path}")


if __name__ == "__main__":
    main()
