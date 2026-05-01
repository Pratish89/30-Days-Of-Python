# stock-research-agent

A beginner-friendly modular Python project to analyze a stock ticker and produce a markdown report.

> **Educational disclaimer:** This project is for learning purposes only and is **not financial advice**.

## Features

- Current price and valuation snapshot
- Latest fundamentals extraction
- Growth drivers and risks commentary
- Practical trim/re-entry zones (simple, educational heuristics)
- Optional OpenAI human-style summary
- Markdown report output

## Requirements

- Python 3.11+

## Installation

```bash
cd stock-research-agent
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## OpenAI setup (optional)

```bash
cp .env.example .env
# then add your key in .env
```

## Usage

```bash
python -m stock_agent AVGO
python -m stock_agent AVGO --ai-summary --save
```

When using `--save`, reports are written to `output/`.

## Testing

```bash
pytest -q
```

## Publish to GitHub

If you want this project as a GitHub repository:

```bash
git init
git add .
git commit -m "Initial commit: stock-research-agent"
git branch -M main
git remote add origin https://github.com/<your-username>/stock-research-agent.git
git push -u origin main
```

You can also create the remote first using the GitHub web UI, then run the same commands.
