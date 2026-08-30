from __future__ import annotations

import argparse
from pathlib import Path

from .generator import score_case, write_case_statement
from .loader import load_case


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate EB-1A draft statements from case folders.")
    parser.add_argument("--cases", type=Path, default=Path("cases"), help="Directory containing case folders.")
    parser.add_argument("--out", type=Path, default=Path("outputs"), help="Output directory for generated supporting statements.")
    args = parser.parse_args()

    cases_dir = args.cases
    out_dir = args.out

    for case_dir in sorted(cases_dir.iterdir()):
        if not case_dir.is_dir():
            continue
        case = load_case(case_dir)
        score = score_case(case)
        out_file = out_dir / f"{case_dir.name}-supporting-statement.md"
        write_case_statement(case, out_file)
        print(f"{case_dir.name}: score={score['score']} | reasons={'; '.join(score['reasons'])}")


if __name__ == "__main__":
    main()
