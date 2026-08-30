# Take-home: Petition Drafting System

**Time: 3–5 hours. Please do not exceed it — we would rather see a deliberately
scoped system than an exhausted one.**

---

## Context

Alma prepares employment-based immigration petitions. The centerpiece of an
EB-1A filing is a **supporting statement**: a long persuasive document arguing
that a specific person meets specific regulatory criteria, grounded in specific
evidence from their case file.

Attorneys typically draft these by hand. It takes hours per case and quality
varies with who is writing. The evidence they work from is a mixed bag — some of
it rigorous and documented, some of it thin, some of it just the beneficiary's
own account of themselves.

## The problem

Build a **repeatable system** that takes a case corpus and produces a draft
EB-1A supporting statement for attorney review.

Two cases are in `cases/`. **Your system must handle both.** They are not
equally strong.

## The goal

The ultimate goal is to increase the productivity of the attorneys creating
these supporting statements. The more successful petitions they can produce per
day, the better.

## Deliverables

1. **The system**, in a private GitHub repository shared with **shuo@tryalma.ai**
   and **johnlemmon@tryalma.ai**, with clear setup instructions.
   - It should be repeatable for other cases.
   - It should be usable by a non-technical attorney — assume legal knowledge,
     not AI or coding knowledge.
   - It should handle problems in the input data: incomplete, incorrect, or
     low-quality evidence.
2. **The generated output for both cases, unedited.** If you hand-edit the
   output, tell us — we will not hold it against you, but we will notice.
3. **A short evaluation write-up**: how good is this solution, how do you know,
   and what would you change with more time?
4. **A coding-agent usage doc**: a one-page summary of how you used a coding
   agent.
5. **A recording, 5 minutes or less**, showing the system running. Narrate what
   we are looking at.

## Before you send it

Play back the recording from the link you are about to share and confirm it
plays, has audio, and runs under five minutes. This is our most commonly missed
item.

## Constraints

- Scope deliberately. Tell us what you decided was in scope, what you left out,
  and why.
- All case data provided is synthetic. Please keep it that way for this
  exercise — but treat it as though it were real.

## What we evaluate

Roughly in this order:

1. **Does the system produce a valid supporting statement?**
2. **Is the system adaptable to different input or new requirements?**
3. **Can you measure how good the resulting supporting statement is?** The
   ultimate measure is whether the government approves the petition — so how do
   you get a useful signal before then?
4. **What you built that we did not ask for** — and what you deliberately left
   out.

## A note on sources

Use whatever you want online. Just don't get help from another person — we are
assessing your work, not theirs.

We don't expect you to arrive with legal knowledge, but learning enough to build
the system is part of the exercise.

## Ambiguity

Ambiguity in this brief is sometimes deliberate, so tell us how you resolved it.
A reasonable answer is preferred over the "right" answer here.

## Project setup (UV)

This repository uses `uv` for package management and execution.

1. Install `uv` if needed:
   - `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. From the repo root, create and sync the environment:
   - `uv sync`
3. Generate drafts for both cases:
   - `uv run petition-drafting --cases cases --out outputs`
4. Optional Hugging Face enhancement:
   - `PETITION_MODEL=google/flan-t5-base uv run petition-drafting --cases cases --out outputs`
   - If no model is configured, the system uses the deterministic local template path instead.

## How the system works

The pipeline does three things:

1. Parses the raw case corpus into a structured fact model.
2. Scores evidence quality and legal relevance so weak evidence can be downweighted or flagged.
3. Produces a supporting statement draft intended for attorney review.

This keeps the output repeatable and grounded in the facts in the case folder rather than relying on a single opaque model call.

## Output locations

- `outputs/case-a-marwah-supporting-statement.md`
- `outputs/case-b-bergqvist-supporting-statement.md`

## Notes on legal framing

This version intentionally avoids overstating weak evidence. For example, pending patent applications are treated carefully, paid placement articles are treated as weak sources, and internal awards are not described as external recognition without qualification.
