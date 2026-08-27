# Cybersecurity Portfolio

[![Notebook validation](https://github.com/Opatel23/cybersecurity-portfolio/actions/workflows/validate-notebooks.yml/badge.svg)](https://github.com/Opatel23/cybersecurity-portfolio/actions/workflows/validate-notebooks.yml)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)
![Authorized labs only](https://img.shields.io/badge/scope-authorized%20labs%20only-2f855a)

A collection of 110 hands-on cybersecurity notebooks spanning detection engineering, network defense, DFIR, threat intelligence, applied cryptography, identity, web security, and controlled adversary simulation.

The projects use Python and reproducible synthetic data to turn security concepts into working prototypes. Each notebook is independent: open one directly in GitHub, run it in Google Colab, or download it for a local Jupyter environment.

> This repository intentionally includes both flagship builds and smaller learning exercises. See the [portfolio guide](docs/PORTFOLIO_GUIDE.md) for maturity levels and recommendations on presenting the work.

## Featured projects

Start here for the strongest demonstrations of breadth and technical depth.

| Project | What it demonstrates | Focus |
|---|---|---|
| [AI-Augmented Threat Hunting](notebooks/security-analytics/ai-augmented-threat-hunting-system-for-real-time-detection-of-polymorphic-malware-in-enterprise-networks.ipynb) | A detection pipeline for evolving malware behavior | Detection engineering, ML |
| [Digital Forensics & Malware Analysis Lab](notebooks/dfir-malware/digital-forensics-and-malware-analysis-lab.ipynb) | A structured workflow for triage, artifact review, and evidence analysis | DFIR, malware analysis |
| [Network Intrusion Detection with NSL-KDD](notebooks/network-security/network-intrusion-detection-using-the-nsl-kdd-dataset.ipynb) | Dataset preparation, model training, and intrusion classification | Network security, ML |
| [Blockchain Security & Smart Contract Auditor](notebooks/blockchain-security/blockchain-security-and-smart-contract-auditor.ipynb) | Automated checks for common smart-contract risks | Blockchain security |
| [Web Application Firewall with Custom Rules](notebooks/network-security/web-application-firewall-waf-with-custom-rules.ipynb) | Rule-based request inspection and defensive filtering | AppSec, detection |
| [Adaptive Honeynet](notebooks/threat-intelligence/adaptive-honeynet-for-real-time-attacker-profiling-and-threat-signature-generation.ipynb) | Attacker profiling and synthetic threat-signature generation | Threat intelligence |

## Skills represented

- Security analytics: anomaly detection, feature engineering, classification, and visualization
- Defensive engineering: IDS, WAF, log analysis, integrity monitoring, and alerting
- DFIR: artifact triage, malware analysis, incident timelines, YARA, and memory concepts
- Network security: traffic analysis, DNS, packet inspection, honeypots, and authorized scanning
- Applied security: authentication, cryptography, password security, and blockchain analysis

## Browse by area

| Area | Notebooks | Directory |
|---|---:|---|
| Network Security | 24 | [Browse](notebooks/network-security) |
| Cryptography | 17 | [Browse](notebooks/cryptography) |
| Security Tools | 17 | [Browse](notebooks/security-tools) |
| Web Application Security | 14 | [Browse](notebooks/web-application-security) |
| DFIR & Malware | 12 | [Browse](notebooks/dfir-malware) |
| Security Analytics | 12 | [Browse](notebooks/security-analytics) |
| Threat Intelligence | 7 | [Browse](notebooks/threat-intelligence) |
| Blockchain Security | 4 | [Browse](notebooks/blockchain-security) |
| Identity & Access | 3 | [Browse](notebooks/identity-and-access) |

## Running a notebook

1. Open a notebook from the catalog below.
2. Select **Open in Colab** on GitHub, or upload the `.ipynb` file at [Google Colab](https://colab.research.google.com/).
3. Review the code and the notebook-specific dependencies before executing cells.
4. Use only synthetic data, a local lab, or a system you own and are authorized to test.
5. Supply required API credentials through Colab secrets or environment variables—never hard-code them.

Notebooks vary in dependency and dataset requirements. They are statically validated in CI, but they are not all executed automatically because some need Colab-only packages, external datasets, elevated networking capabilities, or user-provided credentials.

## Safety and responsible use

These projects are educational and intended only for authorized environments. Stored outputs and execution counters have been removed, placeholder credentials are standardized, and the two highest-risk demonstrations are constrained to local disposable simulations. See [SECURITY.md](SECURITY.md) before running offensive-security material.

## Complete project catalog

| Notebook | Area | Cells |
|---|---|---:|
| [2FA Authenticator with QR Code and Verification](notebooks/cryptography/2fa-authenticator-with-qr-code-and-verification.ipynb) | Cryptography | 2 |
| [Adaptive Honeynet for Real-Time Attacker Profiling and Threat Signature Generation](notebooks/threat-intelligence/adaptive-honeynet-for-real-time-attacker-profiling-and-threat-signature-generation.ipynb) | Threat Intelligence | 3 |
| [Advanced Network Anomaly Detection](notebooks/security-analytics/advanced-network-anomaly-detection.ipynb) | Security Analytics | 2 |
| [Advanced Web Vulnerability Scanner](notebooks/web-application-security/advanced-web-vulnerability-scanner.ipynb) | Web Application Security | 2 |
| [AES + RSA Encryption Toolkit (Hybrid Encryption Model)](notebooks/cryptography/aes-rsa-encryption-toolkit-hybrid-encryption-model.ipynb) | Cryptography | 5 |
| [AI Honeypot + Real-Time Threat Dashboard](notebooks/network-security/ai-honeypot-real-time-threat-dashboard.ipynb) | Network Security | 2 |
| [AI Model Adversarial Attack and Defense System](notebooks/security-analytics/ai-model-adversarial-attack-and-defense-system.ipynb) | Security Analytics | 2 |
| [AI-Augmented Threat Hunting System for Real-Time Detection of Polymorphic Malware in Enterprise Networks](notebooks/security-analytics/ai-augmented-threat-hunting-system-for-real-time-detection-of-polymorphic-malware-in-enterprise-networks.ipynb) | Security Analytics | 4 |
| [AI-Powered Malware Analysis](notebooks/dfir-malware/ai-powered-malware-analysis.ipynb) | DFIR & Malware | 2 |
| [AI-Powered Supply Chain Attack Detection](notebooks/security-analytics/ai-powered-supply-chain-attack-detection.ipynb) | Security Analytics | 2 |
| [AI-Powered Threat Intelligence](notebooks/threat-intelligence/ai-powered-threat-intelligence.ipynb) | Threat Intelligence | 2 |
| [Anomaly Detection in Network Traffic using Synthetic Data + Isolation Forest](notebooks/network-security/anomaly-detection-in-network-traffic-using-synthetic-data-isolation-forest.ipynb) | Network Security | 2 |
| [Anomaly Detection in System Logs Using Autoencoders](notebooks/security-analytics/anomaly-detection-in-system-logs-using-autoencoders.ipynb) | Security Analytics | 2 |
| [APT Detection with Graph Neural Networks](notebooks/network-security/apt-detection-with-graph-neural-networks.ipynb) | Network Security | 2 |
| [Auth Log Anomaly Detection](notebooks/security-analytics/auth-log-anomaly-detection.ipynb) | Security Analytics | 2 |
| [Automation Suite](notebooks/security-tools/automation-suite.ipynb) | Security Tools | 2 |
| [Base64 Steganography Detector](notebooks/cryptography/base64-steganography-detector.ipynb) | Cryptography | 2 |
| [Basic XOR Cipher Cryptanalysis with Frequency Analysis](notebooks/cryptography/basic-xor-cipher-cryptanalysis-with-frequency-analysis.ipynb) | Cryptography | 2 |
| [Blockchain and Cryptocurrency](notebooks/blockchain-security/blockchain-and-cryptocurrency.ipynb) | Blockchain Security | 2 |
| [Blockchain Forensics and Cryptocurrency Tracing](notebooks/blockchain-security/blockchain-forensics-and-cryptocurrency-tracing.ipynb) | Blockchain Security | 2 |
| [Blockchain Security & Smart Contract Auditor](notebooks/blockchain-security/blockchain-security-and-smart-contract-auditor.ipynb) | Blockchain Security | 3 |
| [Brute Force Attack Simulation on a Login Form (Offline)](notebooks/identity-and-access/brute-force-attack-simulation-on-a-login-form-offline.ipynb) | Identity & Access | 2 |
| [Build a Phishing URL Detector with Python](notebooks/web-application-security/build-a-phishing-url-detector-with-python.ipynb) | Web Application Security | 2 |
| [Building a Honeypot](notebooks/network-security/building-a-honeypot.ipynb) | Network Security | 2 |
| [C2 Server and Agent for Penetration Testing](notebooks/security-tools/c2-server-and-agent-for-penetration-testing.ipynb) | Security Tools | 2 |
| [Caesar Cipher Encryptor/Decryptor](notebooks/cryptography/caesar-cipher-encryptor-decryptor.ipynb) | Cryptography | 2 |
| [Comprehensive Network Security Analyzer](notebooks/network-security/comprehensive-network-security-analyzer.ipynb) | Network Security | 2 |
| [Cryptocurrency Security Analysis](notebooks/blockchain-security/cryptocurrency-security-analysis.ipynb) | Blockchain Security | 2 |
| [Cryptographic Attack](notebooks/cryptography/cryptographic-attack.ipynb) | Cryptography | 2 |
| [CryptoGraphic Malware Detection](notebooks/cryptography/cryptographic-malware-detection.ipynb) | Cryptography | 2 |
| [Cybersecurity Lab: Network Traffic Analysis and Vulnerability Scanning](notebooks/network-security/cybersecurity-lab-network-traffic-analysis-and-vulnerability-scanning.ipynb) | Network Security | 2 |
| [Cybersecurity Network Analyzer & Vulnerability Scanner](notebooks/network-security/cybersecurity-network-analyzer-and-vulnerability-scanner.ipynb) | Network Security | 2 |
| [Detect Suspicious Network Connections (Log Analyzer)](notebooks/network-security/detect-suspicious-network-connections-log-analyzer.ipynb) | Network Security | 2 |
| [Detect Typo-Squatting Domains Using Fuzzy Matching](notebooks/security-tools/detect-typo-squatting-domains-using-fuzzy-matching.ipynb) | Security Tools | 2 |
| [Detecting Malicious URLs with Machine Learning](notebooks/web-application-security/detecting-malicious-urls-with-machine-learning.ipynb) | Web Application Security | 2 |
| [Develop a Simple Ransomware Simulation](notebooks/dfir-malware/develop-a-simple-ransomware-simulation.ipynb) | DFIR & Malware | 2 |
| [Digital Forensics & Malware Analysis Lab](notebooks/dfir-malware/digital-forensics-and-malware-analysis-lab.ipynb) | DFIR & Malware | 3 |
| [Digital Forensics & Malware Analysis Toolkit](notebooks/dfir-malware/digital-forensics-and-malware-analysis-toolkit.ipynb) | DFIR & Malware | 2 |
| [Digital Forensics Data Visualization](notebooks/dfir-malware/digital-forensics-data-visualization.ipynb) | DFIR & Malware | 2 |
| [DNS Fingerprinting & Host Profiling](notebooks/network-security/dns-fingerprinting-and-host-profiling.ipynb) | Network Security | 2 |
| [DNS Spoof Detector](notebooks/network-security/dns-spoof-detector.ipynb) | Network Security | 2 |
| [DoS (Denial of Service), R2L (Remote to Local), U2R (User to Root), and Probing Project](notebooks/security-tools/dos-denial-of-service-r2l-remote-to-local-u2r-user-to-root-and-probing-project.ipynb) | Security Tools | 2 |
| [Educational Cybersecurity Learning Dashboard](notebooks/security-tools/educational-cybersecurity-learning-dashboard.ipynb) | Security Tools | 2 |
| [Email Header Phishing Detector](notebooks/web-application-security/email-header-phishing-detector.ipynb) | Web Application Security | 2 |
| [Encrypted Network Traffic Classifier with Deep Learning](notebooks/network-security/encrypted-network-traffic-classifier-with-deep-learning.ipynb) | Network Security | 2 |
| [Encrypted Password Vault Using AES Encryption](notebooks/cryptography/encrypted-password-vault-using-aes-encryption.ipynb) | Cryptography | 2 |
| [Entropy Analysis of Executables](notebooks/security-tools/entropy-analysis-of-executables.ipynb) | Security Tools | 3 |
| [Federated Learning Security and Byzantine Attack](notebooks/security-tools/federated-learning-security-and-byzantine-attack.ipynb) | Security Tools | 2 |
| [File Hash Integrity Checker](notebooks/security-tools/file-hash-integrity-checker.ipynb) | Security Tools | 2 |
| [File Integrity Checker with SHA256](notebooks/security-tools/file-integrity-checker-with-sha256.ipynb) | Security Tools | 2 |
| [Hash Function Comparisons](notebooks/security-tools/hash-function-comparisons.ipynb) | Security Tools | 2 |
| [Homomorphic Encryption Attack and Privacy Analysis](notebooks/cryptography/homomorphic-encryption-attack-and-privacy-analysis.ipynb) | Cryptography | 2 |
| [Insecure HTTP Exposure Scanner with Shodan Validation](notebooks/web-application-security/insecure-http-exposure-scanner-with-shodan-validation.ipynb) | Web Application Security | 3 |
| [Intermediate Keylogger](notebooks/identity-and-access/intermediate-keylogger.ipynb) | Identity & Access | 2 |
| [Intrusion Detection System (IDS)](notebooks/security-analytics/intrusion-detection-system-ids.ipynb) | Security Analytics | 3 |
| [LLM-CTIA: Cyber Threat Intelligence Aggregator](notebooks/threat-intelligence/llm-ctia-cyber-threat-intelligence-aggregator.ipynb) | Threat Intelligence | 2 |
| [Log Analysis and SIEM Tool](notebooks/security-analytics/log-analysis-and-siem-tool.ipynb) | Security Analytics | 2 |
| [Log File Anomaly Detection System](notebooks/security-analytics/log-file-anomaly-detection-system.ipynb) | Security Analytics | 2 |
| [Malicious URL Detection (Heuristic-Based, No ML or API)](notebooks/web-application-security/malicious-url-detection-heuristic-based-no-ml-or-api.ipynb) | Web Application Security | 2 |
| [Malware Analysis Laboratory](notebooks/dfir-malware/malware-analysis-laboratory.ipynb) | DFIR & Malware | 2 |
| [Malware Analysis with YARA](notebooks/dfir-malware/malware-analysis-with-yara.ipynb) | DFIR & Malware | 3 |
| [Malware Analysis and Reverse Engineering](notebooks/dfir-malware/malware-analysis-and-reverse-engineering.ipynb) | DFIR & Malware | 2 |
| [Malware Classification Using Static Analysis](notebooks/dfir-malware/malware-classification-using-static-analysis.ipynb) | DFIR & Malware | 2 |
| [Malware Traffic Classification Using Machine Learning](notebooks/dfir-malware/malware-traffic-classification-using-machine-learning.ipynb) | DFIR & Malware | 2 |
| [Multi Vector IoT Botnet Detection](notebooks/security-analytics/multi-vector-iot-botnet-detection.ipynb) | Security Analytics | 2 |
| [Multi-Domain Threat Intelligence & Attribution Engine](notebooks/threat-intelligence/multi-domain-threat-intelligence-and-attribution-engine.ipynb) | Threat Intelligence | 2 |
| [Network Intrusion Detection System](notebooks/network-security/network-intrusion-detection-system.ipynb) | Network Security | 2 |
| [Network Intrusion Detection Using the NSL-KDD Dataset](notebooks/network-security/network-intrusion-detection-using-the-nsl-kdd-dataset.ipynb) | Network Security | 3 |
| [Network Packet Analysis](notebooks/network-security/network-packet-analysis.ipynb) | Network Security | 2 |
| [network packet sniffing and analysis](notebooks/network-security/network-packet-sniffing-and-analysis.ipynb) | Network Security | 2 |
| [Network Security Analyzer](notebooks/network-security/network-security-analyzer.ipynb) | Network Security | 2 |
| [Network Security Monitor](notebooks/network-security/network-security-monitor.ipynb) | Network Security | 2 |
| [Network Security Scanner](notebooks/network-security/network-security-scanner.ipynb) | Network Security | 2 |
| [Network Security Scanner and Vulnerability Assessment Tool](notebooks/network-security/network-security-scanner-and-vulnerability-assessment-tool.ipynb) | Network Security | 2 |
| [Network Security Tool](notebooks/network-security/network-security-tool.ipynb) | Network Security | 2 |
| [Network Traffic Analyzer](notebooks/network-security/network-traffic-analyzer.ipynb) | Network Security | 2 |
| [Network Traffic Anomaly Detection using an Autoencoder](notebooks/network-security/network-traffic-anomaly-detection-using-an-autoencoder.ipynb) | Network Security | 2 |
| [Network Traffic Anomaly Detection using Machine Learning](notebooks/security-analytics/network-traffic-anomaly-detection-using-machine-learning.ipynb) | Security Analytics | 2 |
| [Password Cracking with Rainbow Table](notebooks/cryptography/password-cracking-with-rainbow-table.ipynb) | Cryptography | 2 |
| [Password Strength Checker using Entropy](notebooks/cryptography/password-strength-checker-using-entropy.ipynb) | Cryptography | 2 |
| [Password Strength Classifier (Machine Learning)](notebooks/cryptography/password-strength-classifier-machine-learning.ipynb) | Cryptography | 2 |
| [Password Strength Cracker (Entropy + Dictionary Attack Simulator)](notebooks/cryptography/password-strength-cracker-entropy-dictionary-attack-simulator.ipynb) | Cryptography | 2 |
| [Password Vault](notebooks/cryptography/password-vault.ipynb) | Cryptography | 2 |
| [Phishing Email Detector](notebooks/web-application-security/phishing-email-detector.ipynb) | Web Application Security | 2 |
| [Phishing URL Detection with NLP](notebooks/web-application-security/phishing-url-detection-with-nlp.ipynb) | Web Application Security | 2 |
| [Phishing URL Detector Prototype](notebooks/web-application-security/phishing-url-detector-prototype.ipynb) | Web Application Security | 2 |
| [Phishing URL Detector with Machine Learning](notebooks/web-application-security/phishing-url-detector-with-machine-learning.ipynb) | Web Application Security | 2 |
| [Port Scanner](notebooks/network-security/port-scanner.ipynb) | Network Security | 2 |
| [Quantum Key Distribution Attack and Security Analysis](notebooks/security-tools/quantum-key-distribution-attack-and-security-analysis.ipynb) | Security Tools | 2 |
| [Quantum Resistant Cryptographic Attack Simulator](notebooks/cryptography/quantum-resistant-cryptographic-attack-simulator.ipynb) | Cryptography | 2 |
| [Scan for Suspicious IPs in Public Logs](notebooks/security-analytics/scan-for-suspicious-ips-in-public-logs.ipynb) | Security Analytics | 2 |
| [Security Incident Timeline Tracker](notebooks/dfir-malware/security-incident-timeline-tracker.ipynb) | DFIR & Malware | 2 |
| [Side-Channel Attack System](notebooks/security-tools/side-channel-attack-system.ipynb) | Security Tools | 2 |
| [Simple Email Address Extractor](notebooks/security-tools/simple-email-address-extractor.ipynb) | Security Tools | 2 |
| [Simple JWT Cracker (Weak Secret Brute-Forcer)](notebooks/security-tools/simple-jwt-cracker-weak-secret-brute-forcer.ipynb) | Security Tools | 2 |
| [Simple Password Strength Classifier Using Regex & Basic Features](notebooks/cryptography/simple-password-strength-classifier-using-regex-and-basic-features.ipynb) | Cryptography | 2 |
| [Simple XOR File Encryptor/Decryptor](notebooks/security-tools/simple-xor-file-encryptor-decryptor.ipynb) | Security Tools | 2 |
| [SQL Injection exploit script](notebooks/web-application-security/sql-injection-exploit-script.ipynb) | Web Application Security | 2 |
| [Steganographic Detection](notebooks/cryptography/steganographic-detection.ipynb) | Cryptography | 2 |
| [Suspicious File Scanner (Offline, No API)](notebooks/web-application-security/suspicious-file-scanner-offline-no-api.ipynb) | Web Application Security | 2 |
| [Target Recon Toolkit](notebooks/threat-intelligence/target-recon-toolkit.ipynb) | Threat Intelligence | 2 |
| [Threat Hunting Intelligence Program](notebooks/threat-intelligence/threat-hunting-intelligence-program.ipynb) | Threat Intelligence | 2 |
| [Threat Intelligence Dashboard](notebooks/threat-intelligence/threat-intelligence-dashboard.ipynb) | Threat Intelligence | 2 |
| [Userland Rootkit via LD_PRELOAD](notebooks/security-tools/userland-rootkit-via-ld-preload.ipynb) | Security Tools | 2 |
| [Web Application Firewall (WAF) with Custom Rules](notebooks/network-security/web-application-firewall-waf-with-custom-rules.ipynb) | Network Security | 3 |
| [Web Application Security Scan](notebooks/web-application-security/web-application-security-scan.ipynb) | Web Application Security | 2 |
| [Web Application Security Scanner](notebooks/web-application-security/web-application-security-scanner.ipynb) | Web Application Security | 2 |
| [Wireless Security Auditor](notebooks/security-tools/wireless-security-auditor.ipynb) | Security Tools | 2 |
| [Zero-Knowledge Proof Authentication System](notebooks/identity-and-access/zero-knowledge-proof-authentication-system.ipynb) | Identity & Access | 2 |
| [Zero-Day Exploit Detection via Memory Forensics](notebooks/dfir-malware/zero-day-exploit-detection-via-memory-forensics.ipynb) | DFIR & Malware | 2 |

## Repository notes

- Generated files, local secrets, and notebook outputs are excluded from version control.
- The original Drive export is not included.
- Notebooks have not been automatically executed because many require Colab-only packages, network access, or user-provided datasets.
