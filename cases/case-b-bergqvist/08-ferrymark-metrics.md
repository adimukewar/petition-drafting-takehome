# Ferrymark — Project Metrics

**Repository:** github.com/bergqvist/ferrymark *(illustrative — not a real repo)*
**Created:** 22 June 2020
**License:** Apache 2.0
**Snapshot date:** 18 May 2026

---

## Repository statistics

| Metric | Value |
|---|---|
| Stars | 4,231 |
| Forks | 388 |
| Contributors (all-time) | 94 |
| Contributors (last 12 months) | 31 |
| Commits | 3,847 |
| Commits authored by T. Bergqvist | 1,912 (49.7%) |
| Open issues | 63 |
| Closed issues | 1,104 |
| Releases | 41 |
| Package downloads (last 12 months) | 2.1M |

## Governance

Bergqvist is sole owner of the repository and one of four maintainers with
merge rights. The `MAINTAINERS.md` file lists him as project lead. All release
tags since v0.1 have been cut by him.

## Notable technical contributions (from release notes)

- **v0.4 (Nov 2021)** — heterogeneity-aware placement. The core scheduling
  contribution: placement decisions weight node class, spot-eviction
  probability, and task shape jointly rather than filtering sequentially.
- **v0.9 (Aug 2022)** — adaptive backpressure. Queue admission responds to
  downstream saturation signals.
- **v1.0 (Mar 2023)** — stability guarantees, formal API.
- **v2.0 (Jan 2025)** — multi-tenant isolation.

## Downstream references

Three other open-source projects cite Ferrymark's placement approach in their
own design documents:

- *Tinderbox* (workflow engine) — "placement follows the approach described in
  Ferrymark's design notes"
- *Halyard* (batch runner) — lists Ferrymark as prior art in its scheduling RFC
- *Cormorant* (ML training orchestrator) — vendors a modified Ferrymark
  placement module

## Conference and community

Ferrymark has been the subject of talks by people other than Bergqvist at two
community events (per organizer listings): a 30-minute session at Nordic
Infra Summit 2024 by an engineer at Ironwood Freight, and a lightning talk at
DistSysDays 2025 by a Bellhaven Analytics engineer.
