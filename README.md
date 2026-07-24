# QA & Security Testing of a Conversational AI Assistant

A small portfolio project demonstrating **functional QA testing** and
**lightweight security / prompt-injection testing** applied to a
conversational AI (LLM-based) assistant.

This project was built to demonstrate skills relevant to QA and
conversational AI roles: designing test cases, executing them
systematically, documenting bugs/vulnerabilities with severity levels,
and writing a clear professional report — the same process used for
testing enterprise software, applied here to an AI chatbot.

## What's inside

```
chatbot-qa-security-testing/
├── src/
│   └── bot.py                 # The chatbot being tested ("system under test")
├── tests/
│   ├── test_functional_qa.py  # Functional QA test cases
│   └── test_security.py       # Prompt-injection / jailbreak test cases
├── reports/
│   ├── REPORT_TEMPLATE.md     # Final report (fill in after running tests)
│   ├── functional_results.csv # Raw functional test output (generated)
│   └── security_results.csv   # Raw security test output (generated)
├── requirements.txt
└── README.md
```

## The bot being tested

`src/bot.py` is a simple customer support assistant for a fictional
company, "TechNova". It's intentionally simple - the point of this
project is the **testing process**, not the bot itself.

## What is tested

**Functional QA** - does the bot answer normal support questions
correctly, stay on topic, and handle confusing/contradictory input
sensibly?

**Security testing** - can the bot be manipulated into:
- revealing its internal system prompt
- abandoning its role/rules ("jailbreak")
- believing a user has special/admin authority
- leaking restricted information indirectly

This mirrors the kind of testing used in LLM red-teaming and
conversational AI QA roles.

## How to run it

This project uses [Ollama](https://ollama.com) to run a free, open-source
LLM (Llama 3.2) locally on your own computer - no API key and no cost.

1. Install [Ollama](https://ollama.com/download) for your OS.
2. Pull the model (one-time download, ~2GB):
   ```
   ollama pull llama3.2
   ```
3. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the functional tests:
   ```
   python tests/test_functional_qa.py
   ```
5. Run the security tests:
   ```
   python tests/test_security.py
   ```
6. Open `reports/functional_results.csv` and `reports/security_results.csv`,
   fill in PASS/FAIL and severity columns based on what you observe.
7. Copy the results into `reports/REPORT_TEMPLATE.md` to produce the
   final report.

## Disclaimer

This is a learning/portfolio project using a small demo bot built for
this purpose. It is not a security audit of any real product or company.
