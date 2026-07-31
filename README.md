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

1. **The system**, in a private GitHub repository shared with shuo@tryalma.ai,
   with clear setup instructions.
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
5. **A recording, 5 minutes or less**, showing the system running.

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
