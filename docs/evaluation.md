# Evaluation write-up

## Scope

This project intentionally focuses on the repeatable drafting layer, not on a full legal research or compliance engine. In scope are:

- parsing a case corpus from markdown evidence files,
- scoring evidence quality and legal relevance,
- generating an EB-1A supporting statement draft from structured facts,
- flagging weak or ambiguous inputs for attorney review.

Out of scope for this version are:

- exhaustive legal database checks,
- full drafting of the entire immigration filing packet,
- end-user UI and authentication,
- complex multi-agent orchestration or external SaaS dependencies.

This keeps the system usable for an attorney who is not technical while still being strong enough to handle mixed-quality facts.

## How good is it?

The generated drafts are strongest where the input evidence is direct and independently verified. For the Marwah case, the system appropriately emphasizes:

- the high citation count,
- the operational deployments,
- the external recommendation letters,
- the service and recognition record.

For the Bergqvist case, the system appropriately downweights:

- the paid placement article,
- the internal hackathon award,
- the pending patent application when it is still pending and has not matured into a final patent right.

This matters because a legal drafting system should not turn weak evidence into confident assertions. The current design is deliberately cautious about that.

## How do we know?

The output is grounded in the evidence files, not in generic legal language. Each supporting statement is built from a structured evidence summary, and high-confidence sources are emphasized while weaker or ambiguous materials are either ignored or flagged. The pipeline extracts metadata from the case folder, scores case strength, and produces a draft with explicit attorney-review notes.

This is a useful proxy for quality because the strongest evidence in the corpus is the kind that would matter most in a real EB-1A filing: independent confirmations, production use, peer review, and external recognition.

## What I would change with more time

- Add a more formal evidence schema with explicit source-type weights and legal criterion mapping.
- Add human-in-the-loop review: a checklist that helps the attorney confirm whether evidence is strong, moderate, or weak.
- Expand the generator to support multiple drafting styles and sections such as a short summary, a criterion-by-criterion argument, and a red-flag memo.
- Use an LLM or Hugging Face model at the optional final polish stage, but only after the factual backbone is locked in.
