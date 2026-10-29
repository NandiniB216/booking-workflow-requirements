"""Traceability check for the requirements pack.

    python scripts/check_traceability.py

Fails (exit 1) if a test scenario references an AC, BR or edge case that does
not exist, or if an acceptance criterion or business rule has no test.
Also regenerates docs/test-scenarios.csv from the Markdown table so the two
never drift apart.
"""

import csv
import re
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parents[1] / "docs"
ID = re.compile(r"\b(AC-\d{2}\.\d|BR-\d{2}|E-\d{2})\b")


def defined_ids(text):
    ids = set(re.findall(r"\*\*(AC-\d{2}\.\d)\*\*", text))
    ids |= set(re.findall(r"^\| (BR-\d{2}) \|", text, flags=re.M))
    ids |= set(re.findall(r"^\| (E-\d{2}) \|", text, flags=re.M))
    return ids


def scenario_rows(text):
    rows = []
    for line in text.splitlines():
        if re.match(r"^\| T-\d{2} \|", line):
            rows.append([cell.strip() for cell in line.strip().strip("|").split("|")])
    return rows


def main():
    requirements = (DOCS / "requirements.md").read_text(encoding="utf-8")
    scenarios_md = (DOCS / "test-scenarios.md").read_text(encoding="utf-8")
    defined = defined_ids(requirements)
    rows = scenario_rows(scenarios_md)

    problems = []
    referenced = set()
    for row in rows:
        refs = set(ID.findall(row[1]))
        referenced |= refs
        for ref in refs - defined:
            problems.append(f"{row[0]} references {ref}, which is not defined")

    # Every BR and AC should be exercised by at least one scenario.
    for item in sorted(i for i in defined if not i.startswith("E-")):
        if item not in referenced:
            problems.append(f"{item} has no test scenario")

    with open(DOCS / "test-scenarios.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "traces_to", "given", "when", "then", "type"])
        writer.writerows(rows)

    print(f"{len(defined)} requirement IDs defined, {len(rows)} scenarios, "
          f"{len(referenced & defined)} IDs covered")
    for p in problems:
        print("PROBLEM:", p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
