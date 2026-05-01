"""Price zone calculations for trimming and re-entry."""

from stock_agent.models import PriceZones


def calculate_price_zones(current_price: float) -> PriceZones:
    """Calculate practical zones using simple percentage bands.

    This is intentionally simple and educational.
    """
    if current_price <= 0:
        raise ValueError("Current price must be greater than zero.")

    trim_low = current_price * 1.1
    trim_high = current_price * 1.2
    reentry_low = current_price * 0.85
    reentry_high = current_price * 0.95

    return PriceZones(
        trim_zone=(round(trim_low, 2), round(trim_high, 2)),
        reentry_zone=(round(reentry_low, 2), round(reentry_high, 2)),
        support=round(reentry_low, 2),
        resistance=round(trim_high, 2),
    )
