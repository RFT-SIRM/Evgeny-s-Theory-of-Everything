#!/usr/bin/env python3
"""Documentation-integrity checks only; these do not prove mathematical claims."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "LICENSE",
    "NOTICE",
    "CITATION.cff",
    "FOUNDATIONS.md",
    "RESEARCH_PROGRAM.md",
    "CLAIMS_AND_EVIDENCE.md",
    "OPEN_PROBLEMS.md",
    "HISTORICAL_DEVELOPMENT.md",
    "MATHEMATICAL_FRAMEWORK.md",
    "references/SOURCE_REPOSITORIES.md",
    "computational/REPRODUCIBILITY.md",
    "formalization/README.md",
]

def main() -> int:
    errors = []
    for rel in REQUIRED:
        path = ROOT / rel
        if not path.is_file():
            errors.append(f"Missing required document: {rel}")
        elif not path.read_text(encoding="utf-8").strip():
            errors.append(f"Empty required document: {rel}")

    ledger_path = ROOT / "CLAIMS_AND_EVIDENCE.md"
    if ledger_path.is_file():
        ledger = ledger_path.read_text(encoding="utf-8")
        for status in ("OPEN", "NOT ESTABLISHED", "NUMERICALLY REPRODUCED"):
            if status not in ledger:
                errors.append(f"Claim ledger is missing evidence status: {status}")

    readme_path = ROOT / "README.md"
    if readme_path.is_file():
        readme = readme_path.read_text(encoding="utf-8")
        for source in (
            "https://github.com/RFT-SIRM/Evgeny-Theorem",
            "https://github.com/RFT-SIRM/Phi-Genesis",
        ):
            if source not in readme:
                errors.append(f"README missing source provenance URL: {source}")

    license_path = ROOT / "LICENSE"
    if license_path.is_file():
        license_text = license_path.read_text(encoding="utf-8")
        if "Apache License" not in license_text or "Version 2.0" not in license_text:
            errors.append("LICENSE must contain the Apache License 2.0 text")

    readme_path = ROOT / "README.md"
    if readme_path.is_file():
        readme = readme_path.read_text(encoding="utf-8")
        for reference in ("LICENSE", "NOTICE", "CITATION.cff"):
            if reference not in readme:
                errors.append(f"README missing repository-governance reference: {reference}")

    if errors:
        print("Documentation integrity checks FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Documentation integrity checks passed ({len(REQUIRED)} required documents).")
    print("Note: these checks validate repository structure and provenance labels only; they do not verify mathematical theorems.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
