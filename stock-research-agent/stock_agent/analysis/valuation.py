"""Valuation analysis helpers."""

from __future__ import annotations

from stock_agent.models import PriceValuation


def classify_valuation(pe_ratio: float | None) -> str:
    """Classify valuation from PE ratio."""
    if pe_ratio is None:
        return "unknown"
    if pe_ratio < 15:
        return "possibly undervalued"
    if pe_ratio <= 30:
        return "fairly valued"
    return "possibly overvalued"


def build_valuation(ticker: str, info: dict) -> PriceValuation:
    """Build valuation object from yfinance info."""
    pe = info.get("trailingPE")
    return PriceValuation(
        ticker=ticker.upper(),
        current_price=float(info.get("currentPrice") or 0.0),
        pe_ratio=float(pe) if pe is not None else None,
        forward_pe=float(info.get("forwardPE")) if info.get("forwardPE") is not None else None,
        market_cap=float(info.get("marketCap")) if info.get("marketCap") is not None else None,
        valuation_label=classify_valuation(float(pe) if pe is not None else None),
    )
