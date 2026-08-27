# Portfolio Guide

The repository contains projects at different levels of depth. That is intentional: it records both focused learning exercises and larger integrated builds.

## Maturity levels

### Featured projects

The featured projects in the main README are the best starting point. They contain broader workflows, project-specific context, expected outputs, and explicit limitations. These are the notebooks to discuss first in interviews or demonstrations.

### Applied labs

Applied labs combine several techniques or produce an analyst-facing result. They are useful demonstrations, but may rely on synthetic data, Colab-specific setup, or simplified infrastructure.

### Focused exercises

Focused exercises isolate one concept—such as hashing, parsing a log, evaluating password entropy, or applying a detection heuristic. They show progression and breadth, but should not be presented as production tools.

## How to evaluate a notebook

Before running or presenting a project, review:

1. The problem statement and authorization boundary.
2. Input data and whether it is synthetic, public, or user supplied.
3. Dependencies and environment assumptions.
4. Evaluation method and false-positive or false-negative tradeoffs.
5. Security limitations and what would be needed for production use.

## Recommended presentation order

Lead with one project aligned to the audience:

- SOC or detection engineering: AI-Augmented Threat Hunting
- DFIR or malware analysis: Digital Forensics & Malware Analysis Lab
- Network defense: NSL-KDD Intrusion Detection
- Application security: Custom-Rule WAF
- Threat intelligence: Adaptive Honeynet
- Web3 security: Smart Contract Auditor

Then use two smaller exercises to demonstrate breadth and learning progression.
