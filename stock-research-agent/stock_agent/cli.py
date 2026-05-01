"""CLI entrypoint for stock agent."""

from __future__ import annotations

import argparse
from pathlib import Path

from stock_agent.ai.summary import generate_ai_summary
from stock_agent.analysis.fundamentals import build_fundamentals, growth_drivers
from stock_agent.analysis.price_zones import calculate_price_zones
from stock_agent.analysis.risks import growth_risks
from stock_agent.analysis.valuation import build_valuation
from stock_agent.data.market_data import get_stock_info
from stock_agent.models import StockAnalysis
from stock_agent.reports.markdown_report import render_markdown_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Stock research agent")
    parser.add_argument("ticker", help="Ticker symbol like AVGO")
    parser.add_argument("--ai-summary", action="store_true", help="Generate optional AI summary with OpenAI API")
    parser.add_argument("--save", action="store_true", help="Save markdown report to output folder")
    return parser


def run() -> None:
    args = build_parser().parse_args()
    info = get_stock_info(args.ticker)

    valuation = build_valuation(args.ticker, info)
    fundamentals = build_fundamentals(info)
    analysis = StockAnalysis(
        valuation=valuation,
        fundamentals=fundamentals,
        growth_drivers=growth_drivers(fundamentals),
        growth_risks=growth_risks(fundamentals, valuation.pe_ratio),
        zones=calculate_price_zones(valuation.current_price),
    )

    if args.ai_summary:
        try:
            analysis.ai_summary = generate_ai_summary(analysis)
        except Exception as exc:
            analysis.ai_summary = f"AI summary unavailable: {exc}"

    report = render_markdown_report(analysis)
    print(report)

    if args.save:
        output_dir = Path("output")
        output_dir.mkdir(parents=True, exist_ok=True)
        out_file = output_dir / f"{args.ticker.upper()}_report.md"
        out_file.write_text(report, encoding="utf-8")
        print(f"Saved report to {out_file}")
