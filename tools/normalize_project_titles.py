"""Normalize legacy Drive-export titles and keep repository references in sync."""

from __future__ import annotations

import json
import re
from pathlib import Path


TITLE_FIXES = {
    "AI Model Adversial Attack and Defense System": "AI Model Adversarial Attack and Defense System",
    "AI-powered malware analysis": "AI-Powered Malware Analysis",
    "BlockChain and CryptoCurrency": "Blockchain and Cryptocurrency",
    "BlockChain Forensics and Cryptocurrency Tracing": "Blockchain Forensics and Cryptocurrency Tracing",
    "CryptoCurrency Security Anaylsis": "Cryptocurrency Security Analysis",
    "Hash Function Comparsions": "Hash Function Comparisons",
    "Log Anaylsis and SIEM Tool": "Log Analysis and SIEM Tool",
    "Malware Anaylsis and Reverse Engineering": "Malware Analysis and Reverse Engineering",
    "Zero-Star Exploit Detection Via Memory Forensics": "Zero-Day Exploit Detection via Memory Forensics",
    "Caesar Cipher Encryptor_Decryptor": "Caesar Cipher Encryptor/Decryptor",
    "CyberSec Lab_ Network Traffic Analysis + Vulnerability Scanning": "Cybersecurity Lab: Network Traffic Analysis and Vulnerability Scanning",
    "encrypted password vault using AES encryption": "Encrypted Password Vault Using AES Encryption",
    "LLM-CTIA_ Cyber Threat Intel Aggregator": "LLM-CTIA: Cyber Threat Intelligence Aggregator",
    "Simple XOR File Encryptor _ Decryptor": "Simple XOR File Encryptor/Decryptor",
}


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    manifest_path = root / "portfolio-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    readme_path = root / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    changed = 0

    for item in manifest["notebooks"]:
        old_title = item["title"]
        new_title = TITLE_FIXES.get(old_title)
        if not new_title:
            continue
        old_relative = Path(item["path"])
        old_path = root / old_relative
        new_relative = old_relative.with_name(f"{slugify(new_title)}.ipynb")
        new_path = root / new_relative
        if new_path != old_path:
            if new_path.exists():
                raise FileExistsError(f"Refusing to overwrite {new_relative}")
            old_path.rename(new_path)

        notebook = json.loads(new_path.read_text(encoding="utf-8"))
        if notebook.get("cells") and notebook["cells"][0].get("cell_type") == "markdown":
            source = "".join(notebook["cells"][0].get("source", []))
            source = source.replace(f"# {old_title}", f"# {new_title}", 1)
            notebook["cells"][0]["source"] = source.splitlines(keepends=True)
            new_path.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

        readme = readme.replace(f"[{old_title}]({old_relative.as_posix()})", f"[{new_title}]({new_relative.as_posix()})")
        item["title"] = new_title
        item["path"] = new_relative.as_posix()
        changed += 1

    readme = readme.replace("| Dfir Malware |", "| DFIR & Malware |")
    readme = readme.replace("| Identity And Access |", "| Identity & Access |")
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    readme_path.write_text(readme, encoding="utf-8")
    print(f"Normalized {changed} project titles.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
