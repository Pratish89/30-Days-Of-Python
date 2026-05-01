"""Risk analysis helpers."""

from stock_agent.models import FundamentalsSnapshot


def growth_risks(f: FundamentalsSnapshot, pe_ratio: float | None) -> list[str]:
    """Generate key risk statements."""
    risks: list[str] = []
    if pe_ratio is not None and pe_ratio > 35:
        risks.append("Valuation is elevated and may compress.")
    if f.debt_to_equity is not None and f.debt_to_equity > 150:
        risks.append("Leverage is high relative to equity.")
    if f.operating_margins is not None and f.operating_margins < 0.1:
        risks.append("Thin operating margins increase downside sensitivity.")
    if not risks:
        risks.append("No major red flags in selected metrics, but execution risk remains.")
    return risks
