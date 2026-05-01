"""Markdown report renderer."""

from stock_agent.models import StockAnalysis


def render_markdown_report(analysis: StockAnalysis) -> str:
    """Render a markdown report for stock analysis."""
    v = analysis.valuation
    f = analysis.fundamentals
    lines = [
        f"# Stock Research Report: {v.ticker}",
        "",
        "> **Educational disclaimer:** This report is for educational purposes only and is **not financial advice**.",
        "",
        "## 1) Current price and valuation",
        f"- Current price: **${v.current_price:.2f}**",
        f"- Trailing P/E: **{v.pe_ratio}**",
        f"- Forward P/E: **{v.forward_pe}**",
        f"- Market cap: **{v.market_cap}**",
        f"- Valuation view: **{v.valuation_label}**",
        "",
        "## 2) Latest fundamentals",
        f"- Revenue growth: **{f.revenue_growth}**",
        f"- Earnings growth: **{f.earnings_growth}**",
        f"- Gross margins: **{f.gross_margins}**",
        f"- Operating margins: **{f.operating_margins}**",
        f"- Debt-to-equity: **{f.debt_to_equity}**",
        f"- Return on equity: **{f.return_on_equity}**",
        "",
        "## 3) Growth drivers",
    ]
    lines.extend([f"- {item}" for item in analysis.growth_drivers])
    lines.extend(["", "## 4) Growth risks"])
    lines.extend([f"- {item}" for item in analysis.growth_risks])
    lines.extend(
        [
            "",
            "## 5) Practical trim and re-entry zones",
            f"- Trim zone: **${analysis.zones.trim_zone[0]} - ${analysis.zones.trim_zone[1]}**",
            f"- Re-entry zone: **${analysis.zones.reentry_zone[0]} - ${analysis.zones.reentry_zone[1]}**",
            f"- Support: **${analysis.zones.support}**",
            f"- Resistance: **${analysis.zones.resistance}**",
        ]
    )
    if analysis.ai_summary:
        lines.extend(["", "## 6) Optional AI summary", analysis.ai_summary])
    return "\n".join(lines) + "\n"
