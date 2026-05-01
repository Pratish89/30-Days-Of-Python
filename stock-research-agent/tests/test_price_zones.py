from stock_agent.analysis.price_zones import calculate_price_zones


def test_calculate_price_zones_basic() -> None:
    zones = calculate_price_zones(100)
    assert zones.trim_zone == (110.0, 120.0)
    assert zones.reentry_zone == (85.0, 95.0)


def test_calculate_price_zones_invalid() -> None:
    import pytest

    with pytest.raises(ValueError):
        calculate_price_zones(0)
