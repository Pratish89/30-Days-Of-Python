from stock_agent.analysis.risks import growth_risks
from stock_agent.models import FundamentalsSnapshot


def test_growth_risks_detects_red_flags() -> None:
    f = FundamentalsSnapshot(
        revenue_growth=0.2,
        earnings_growth=0.2,
        gross_margins=0.5,
        operating_margins=0.08,
        debt_to_equity=200,
        return_on_equity=0.2,
    )
    risks = growth_risks(f, 40)
    assert len(risks) >= 2
