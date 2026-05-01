from stock_agent.analysis.valuation import classify_valuation


def test_valuation_labels() -> None:
    assert classify_valuation(10) == "possibly undervalued"
    assert classify_valuation(20) == "fairly valued"
    assert classify_valuation(40) == "possibly overvalued"
    assert classify_valuation(None) == "unknown"
