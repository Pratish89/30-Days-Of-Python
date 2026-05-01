"""Data models for stock analysis results."""

from dataclasses import dataclass


@dataclass
class PriceValuation:
    ticker: str
    current_price: float
    pe_ratio: float | None
    forward_pe: float | None
    market_cap: float | None
    valuation_label: str


@dataclass
class FundamentalsSnapshot:
    revenue_growth: float | None
    earnings_growth: float | None
    gross_margins: float | None
    operating_margins: float | None
    debt_to_equity: float | None
    return_on_equity: float | None


@dataclass
class PriceZones:
    trim_zone: tuple[float, float]
    reentry_zone: tuple[float, float]
    support: float
    resistance: float


@dataclass
class StockAnalysis:
    valuation: PriceValuation
    fundamentals: FundamentalsSnapshot
    growth_drivers: list[str]
    growth_risks: list[str]
    zones: PriceZones
    ai_summary: str | None = None
