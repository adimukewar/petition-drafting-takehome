# Coding-agent usage summary

I used a coding agent as an accelerator for the structured, repetitive parts of the task rather than as a substitute for judgment.

## What the agent did

- Rapidly scaffolded the project structure and Python package layout.
- Helped convert the raw markdown corpus into a reusable case-loading layer.
- Drafted the first-pass generation and evaluation logic.
- Identified parser edge cases and mismatches between the source files and the generated output.
- Helped keep the system focused on the actual job: a repeatable drafting workflow for attorney review.

## Why this was useful

The case files are dense but structured. The agent was effective at turning that raw corpus into a consistent schema and at iterating on the pipeline quickly. This reduced the amount of manual boilerplate and allowed more attention to the legal framing problem: which sources are strong, which are weak, and what should be omitted or caveated.

## Human supervision

The final legal narrative still required human oversight. The agent was not allowed to invent unsupported facts or overstate weak evidence. That is especially important in EB-1A drafting, where the legal risk is not just stylistic but factual. I kept control of the evidence-quality decisions and the final framing, using the agent to speed up implementation and iteration.

## Result

The workflow is deterministic, auditable, and transparent. That is stronger than a one-shot black-box generation approach, especially for legal work where evidence quality matters more than fluency.
