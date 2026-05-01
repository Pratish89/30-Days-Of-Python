"""Prompt builders for AI summary."""

from stock_agent.models import StockAnalysis


def build_summary_prompt(analysis: StockAnalysis) -> str:
    """Build a concise prompt for generating a human-style summary."""
    return (
        f"Summarize {analysis.valuation.ticker} in plain English for a beginner investor. "
        f"Current price: {analysis.valuation.current_price}. "
        f"Valuation: {analysis.valuation.valuation_label}. "
        f"Drivers: {analysis.growth_drivers}. Risks: {analysis.growth_risks}. "
        f"Trim zone: {analysis.zones.trim_zone}. Re-entry zone: {analysis.zones.reentry_zone}. "
        "Keep it balanced and practical in under 180 words."
    )
