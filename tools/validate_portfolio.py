"""Static validation for the sanitized notebook portfolio."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


SECRET_PATTERNS = {
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "GitHub token": re.compile(r"(?:github_pat_|ghp_)[A-Za-z0-9_]+"),
    "OpenAI-style key": re.compile(r"sk-[A-Za-z0-9]{20,}"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    notebooks = sorted((root / "notebooks").rglob("*.ipynb"))
    failures: list[str] = []

    for path in notebooks:
        try:
            notebook = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            failures.append(f"{path.relative_to(root)}: invalid JSON ({exc})")
            continue
        if notebook.get("nbformat") != 4 or not isinstance(notebook.get("cells"), list):
            failures.append(f"{path.relative_to(root)}: invalid notebook structure")
        text = json.dumps(notebook)
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                failures.append(f"{path.relative_to(root)}: possible {label}")
        for index, cell in enumerate(notebook.get("cells", []), start=1):
            if cell.get("cell_type") == "code":
                if cell.get("outputs"):
                    failures.append(f"{path.relative_to(root)} cell {index}: stored output")
                if cell.get("execution_count") is not None:
                    failures.append(f"{path.relative_to(root)} cell {index}: execution count")

    manifest = json.loads((root / "portfolio-manifest.json").read_text(encoding="utf-8"))
    if manifest.get("notebook_count") != len(notebooks):
        failures.append("manifest notebook count does not match filesystem")

    if failures:
        print("Validation failed:")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1
    print(f"Validated {len(notebooks)} notebooks: JSON, metadata, outputs, manifest, and secret patterns passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
