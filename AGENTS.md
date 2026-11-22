# AGENTS.md — Expense Tracker

## Purpose
Small Python 3 CLI: reads a JSON list of expenses and prints the total (incl. payment fees) and per-category totals.

## Architecture
- `tracker.py` — `fee()` (fee rules), `summarize()` (pure business logic), `main()` (CLI I/O).
- `test_tracker.py`, `test_risks.py` — pytest tests. `expenses.json` — sample data (fake).
- No third-party runtime dependencies. Dev tools: pytest, ruff.

## Setup and safe commands (allowed without asking)
- `pip install pytest ruff` (dev tools only)
- `python tracker.py expenses.json`
- `python -m pytest -q`
- `ruff check .`
- `git status`, `git diff`, `git log`

## Coding conventions
- Python 3.10+, PEP 8, small pure functions, no business logic in `main()`.
- Money rules live in `FEE_RULES`; add a payment method there, not in new `if` chains.
- Add or update a test for every behaviour change.

## Test expectations
`python -m pytest -q` and `ruff check .` must pass before any change is proposed. Report exact commands and results; never claim a test passed without running it.

## Acceptance criteria that must stay true
1. Card fee = 2%, transfer fee = 1.00 flat, cash fee = 0.
2. Total = sum of amounts + fees (rounded to 2 decimals).
3. Category totals = sum of amounts per category (fees excluded).
4. CLI first output line is `Total (incl. fees): <x.xx>`.

## Forbidden actions
- No secrets, tokens, real personal or financial data in code, tests or logs.
- No deployments or publishing (pip upload, git push to protected branches).
- No destructive commands (`rm -rf`, `git reset --hard`, `git push --force`, deleting tests).
- No adding, removing or upgrading dependencies without human approval.
- No weakening or deleting tests to make checks pass.

## Review gates
All diffs are reviewed and approved by a human before commit. Large or multi-file changes need a written plan first.
