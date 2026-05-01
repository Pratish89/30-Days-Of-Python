"""Fundamentals extraction and growth drivers."""

from stock_agent.models import FundamentalsSnapshot


def build_fundamentals(info: dict) -> FundamentalsSnapshot:
    """Extract key fundamentals from info payload."""
    def v(key: str) -> float | None:
        raw = info.get(key)
        return float(raw) if raw is not None else None

    return FundamentalsSnapshot(
        revenue_growth=v("revenueGrowth"),
        earnings_growth=v("earningsGrowth"),
        gross_margins=v("grossMargins"),
        operating_margins=v("operatingMargins"),
        debt_to_equity=v("debtToEquity"),
        return_on_equity=v("returnOnEquity"),
    )


def growth_drivers(f: FundamentalsSnapshot) -> list[str]:
    """Generate plain-language growth drivers."""
    drivers: list[str] = []
    if f.revenue_growth and f.revenue_growth > 0.1:
        drivers.append("Strong revenue growth trend.")
    if f.earnings_growth and f.earnings_growth > 0.1:
        drivers.append("Healthy earnings expansion.")
    if f.gross_margins and f.gross_margins > 0.4:
        drivers.append("High gross margins support profitability.")
    if not drivers:
        drivers.append("No obvious quantitative growth driver from recent fundamentals.")
    return drivers
