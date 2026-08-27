"""Add durable project context to the portfolio's featured notebooks."""

from __future__ import annotations

import json
import re
from pathlib import Path


FEATURED = {
    "notebooks/security-analytics/ai-augmented-threat-hunting-system-for-real-time-detection-of-polymorphic-malware-in-enterprise-networks.ipynb": {
        "goal": "Model a threat-hunting workflow that turns behavioral telemetry into prioritized signals for analyst review.",
        "workflow": "Generate or load representative telemetry, engineer behavioral features, score suspicious activity, and present the highest-risk observations for investigation.",
        "outputs": "Risk-scored events, model evaluation results, and analyst-oriented visual summaries.",
        "limits": "Synthetic behavior cannot reproduce the full diversity or noise of enterprise telemetry. Results demonstrate a workflow, not a production detection guarantee.",
        "skills": "Python, feature engineering, anomaly detection, detection engineering, security analytics",
    },
    "notebooks/dfir-malware/digital-forensics-and-malware-analysis-lab.ipynb": {
        "goal": "Demonstrate a repeatable first-pass investigation of suspicious artifacts without executing real malware.",
        "workflow": "Collect synthetic evidence, calculate identifiers, extract static indicators, organize findings, and build an investigation summary.",
        "outputs": "Artifact metadata, indicators of compromise, severity context, and a structured analyst report.",
        "limits": "This is a training workflow. Real investigations require validated forensic acquisition, chain of custody, isolated tooling, and case-specific expertise.",
        "skills": "DFIR, static analysis, indicators of compromise, evidence handling, Python",
    },
    "notebooks/network-security/network-intrusion-detection-using-the-nsl-kdd-dataset.ipynb": {
        "goal": "Build and evaluate an intrusion-classification pipeline using the NSL-KDD benchmark dataset.",
        "workflow": "Prepare features, encode labels, train a classifier, measure performance, and inspect where the model succeeds or fails.",
        "outputs": "Classification metrics, confusion analysis, and visualizations of model behavior.",
        "limits": "NSL-KDD is useful for learning but does not represent modern production traffic. A deployable IDS needs current telemetry, drift monitoring, and careful false-positive tuning.",
        "skills": "Network security, supervised learning, preprocessing, evaluation, data visualization",
    },
    "notebooks/blockchain-security/blockchain-security-and-smart-contract-auditor.ipynb": {
        "goal": "Show how rule-based analysis can surface common smart-contract security smells for manual review.",
        "workflow": "Parse representative contract content, apply focused security checks, classify findings, and summarize remediation guidance.",
        "outputs": "Categorized findings with severity and recommended follow-up actions.",
        "limits": "Pattern matching cannot prove a contract is safe. Production assessment requires compiler-aware static analysis, testing, and expert review.",
        "skills": "Smart-contract security, static analysis, secure coding, rule design, Python",
    },
    "notebooks/network-security/web-application-firewall-waf-with-custom-rules.ipynb": {
        "goal": "Demonstrate defensive HTTP request inspection with understandable, testable custom rules.",
        "workflow": "Create synthetic requests, inspect request attributes, apply allow and deny rules, and record the decision with an explanation.",
        "outputs": "Request decisions, matched-rule details, and examples of tuning tradeoffs.",
        "limits": "A notebook rule engine is not a production WAF. Real deployments need canonicalization, managed rules, performance testing, observability, and continuous tuning.",
        "skills": "Application security, HTTP, detection logic, rule tuning, secure architecture",
    },
    "notebooks/threat-intelligence/adaptive-honeynet-for-real-time-attacker-profiling-and-threat-signature-generation.ipynb": {
        "goal": "Model how honeynet telemetry can be transformed into behavioral profiles and candidate threat signatures.",
        "workflow": "Generate controlled interaction data, aggregate behaviors, identify recurring patterns, and express those patterns as analyst-reviewable signatures.",
        "outputs": "Attacker behavior summaries, clustered activity, and candidate detection signatures.",
        "limits": "All activity is synthetic. Deploying an internet-facing honeypot requires isolation, legal review, monitoring, and controls that are outside this notebook's scope.",
        "skills": "Threat intelligence, honeypots, behavioral profiling, detection engineering, Python",
    },
}


def markdown_cell(text: str) -> dict:
    return {"cell_type": "markdown", "metadata": {"portfolio": "project-overview-v1"}, "source": text.splitlines(keepends=True)}


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    changed = 0
    for relative_path, details in FEATURED.items():
        path = root / relative_path
        notebook = json.loads(path.read_text(encoding="utf-8"))
        if any(cell.get("metadata", {}).get("portfolio") == "project-overview-v1" for cell in notebook["cells"]):
            continue
        overview = f"""## Project overview

**Objective:** {details['goal']}

**Workflow:** {details['workflow']}

**Expected output:** {details['outputs']}

**Skills demonstrated:** {details['skills']}

### Limitations

{details['limits']}
"""
        notebook["cells"].insert(1, markdown_cell(overview))
        path.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        changed += 1
    manifest_path = root / "portfolio-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    cell_counts: dict[str, int] = {}
    for item in manifest["notebooks"]:
        notebook = json.loads((root / item["path"]).read_text(encoding="utf-8"))
        item["cells"] = len(notebook["cells"])
        cell_counts[item["path"]] = item["cells"]
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    readme_path = root / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    for relative_path, count in cell_counts.items():
        escaped = re.escape(relative_path)
        readme = re.sub(
            rf"(\]\({escaped}\)\s*\|[^\n|]+\|\s*)\d+(\s*\|)",
            rf"\g<1>{count}\2",
            readme,
        )
    readme_path.write_text(readme, encoding="utf-8")
    print(f"Enriched {changed} featured notebooks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
