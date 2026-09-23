Markdown

# AI Chatbot Security Assessment Framework

A production-grade command-line tool designed to perform automated red-teaming and vulnerability assessments on Large Language Models (LLMs) and AI chatbots against the **OWASP LLM Top 10**.

## Features

- **Advanced Adversarial Payloads:** Evaluates multi-step hypothetical jailbreaks, system prompt extractions, and base64-encoded obfuscation bypasses.
- **Commercial API Compatibility:** Easily targets production-grade REST APIs (such as OpenAI or custom enterprise chat gateways).
- **Heuristic Safety Tracking:** Tracks model responses against automated alignment and refusal indicators.
- **Structured Compliance Reporting:** Exports complete audit trails and verdicts into a structured JSON report for security analysis.

---

## Project Structure

```text
ai-security-scanner/
│
├── ai_scanner_pro.py       # Core scanner engine and CLI logic
├── setup.py                # Installation and configuration script
└── README.md               # Project documentation

Installation & Setup

    Clone the repository:
    Bash

git clone [https://github.com/JosephOxan/ai-security-scanner.git](https://github.com/JosephOxan/ai-security-scanner.git)
cd ai-security-scanner

Install the package locally in editable mode:

cd to the downloaded/clonned folder then =>  pipx install .

Usage

Once installed, you can invoke your custom command line tool (aicheck) from anywhere on your system.
Command Syntax
Bash

aicheck -u <TARGET_API_URL> -k <YOUR_API_KEY> -o <REPORT_OUTPUT_PATH>

Example Execution
Bash

aicheck -u [https://api.openai.com/v1/chat/completions](https://api.openai.com/v1/chat/completions) -k sk-your-api-key-here -o audit_results.json

Arguments

    -u, --url: (Required) The target chatbot API endpoint URL.

    -k, --key: The Bearer API key required to authenticate against the commercial target. (Can also be set via the TARGET_API_KEY environment variable).

    -o, --output: Path to store the generated JSON audit compliance report (default: production_audit_report.json).

OWASP LLM Top 10 Coverage

    LLM01: Prompt Injection: Tests multi-step context manipulation and base64-encoded instruction overrides.

    LLM02: Sensitive Information Disclosure: Probes for credential template leaks and internal context extraction.

    LLM03: Excessive Agency: Evaluates backend command execution attempts and unauthorized tool call simulations.

License

This project is licensed under the MIT License. For educational, research, and authorized security auditing purposes only.
