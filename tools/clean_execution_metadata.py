"""Remove Colab session identifiers while preserving notebook code and authorship."""

import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    changed = 0
    for path in sorted((root / "notebooks").rglob("*.ipynb")):
        notebook = json.loads(path.read_text(encoding="utf-8"))
        dirty = False
        for cell in notebook.get("cells", []):
            metadata = cell.get("metadata", {})
            for key in ("executionInfo", "outputId"):
                if key in metadata:
                    del metadata[key]
                    dirty = True
        if dirty:
            path.write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
                            encoding="utf-8")
            changed += 1
    print(f"Removed execution-session metadata from {changed} notebooks.")


if __name__ == "__main__":
    main()
