"""
FUNCTIONAL QA TESTS
====================
These tests check whether the bot behaves correctly for normal,
everyday support questions. This is the kind of testing you'd do
for any piece of software: does it do what it's supposed to do?

Each test case has:
- an id
- the message we send
- what we EXPECT a good bot to do
- a place to write what it ACTUALLY did (fill this in after running)
- pass/fail (fill this in after running)
"""

import csv
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from bot import ask_bot  # noqa: E402

FUNCTIONAL_TEST_CASES = [
    {
        "id": "FUNC-01",
        "message": "How do I return a product I bought last week?",
        "expected_behavior": "Explains the return process clearly.",
    },
    {
        "id": "FUNC-02",
        "message": "What's the weather like today?",
        "expected_behavior": "Politely declines — this is unrelated to TechNova support.",
    },
    {
        "id": "FUNC-03",
        "message": "My order #12345 hasn't arrived, what should I do?",
        "expected_behavior": "Gives a helpful, plausible next step (e.g. check tracking, contact support), without inventing false order data.",
    },
    {
        "id": "FUNC-04",
        "message": "Can you write me a poem instead of helping with orders?",
        "expected_behavior": "Declines and redirects to TechNova support topics.",
    },
    {
        "id": "FUNC-05",
        "message": "I said the item was defective, then said it wasn't, then said it was again. Can I get a refund?",
        "expected_behavior": "Handles the contradictory/confusing context sensibly, asks for clarification instead of getting confused.",
    },
]


def run_functional_tests():
    results = []
    for case in FUNCTIONAL_TEST_CASES:
        print(f"\nRunning {case['id']}...")
        actual = ask_bot(case["message"])
        print("Bot replied:", actual)
        results.append(
            {
                "id": case["id"],
                "message": case["message"],
                "expected_behavior": case["expected_behavior"],
                "actual_response": actual,
                "pass_fail": "",  # fill in manually: PASS / FAIL
                "severity": "",  # fill in manually if FAIL: Low / Medium / High
                "notes": "",
            }
        )

    output_path = os.path.join(os.path.dirname(__file__), "..", "reports", "functional_results.csv")
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["id", "message", "expected_behavior", "actual_response", "pass_fail", "severity", "notes"],
        )
        writer.writeheader()
        writer.writerows(results)

    print(f"\nSaved results to {output_path}")
    print("Now open that file and fill in PASS/FAIL and severity for each row.")


if __name__ == "__main__":
    run_functional_tests()
