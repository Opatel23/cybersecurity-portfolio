# Contributing

This repository is a personal cybersecurity learning portfolio, but corrections and defensive improvements are welcome.

## Notebook standards

- Keep each project in one independently usable `.ipynb` file.
- Begin with a clear objective, expected inputs, and authorized-use boundary.
- Use synthetic or openly licensed datasets whenever possible.
- Read credentials from environment variables or notebook secret storage.
- Do not commit notebook outputs, execution counts, local paths, keys, tokens, packet captures, or private datasets.
- Keep offensive-security demonstrations restricted to local, disposable labs.

## Before opening a pull request

Run the repository validator:

```bash
python tools/validate_portfolio.py
```

The validator checks notebook JSON, stored outputs, execution counts, manifest consistency, and common credential signatures.
