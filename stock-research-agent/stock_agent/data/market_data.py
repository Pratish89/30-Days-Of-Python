"""Market data fetching utilities built on yfinance."""

from __future__ import annotations

import yfinance as yf


def get_stock_info(ticker: str) -> dict:
    """Return info dictionary for a ticker symbol."""
    try:
        return yf.Ticker(ticker).info
    except Exception as exc:  # pragma: no cover
        raise RuntimeError(f"Failed to fetch data for {ticker}: {exc}") from exc
