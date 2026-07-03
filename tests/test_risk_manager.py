from bottradenc.risk.risk_manager import RiskManager


def test_position_size():
    rm = RiskManager(capital_base=1000, trade_fraction=0.25)
    assert rm.position_size() == 250


def test_apply_costs():
    assert RiskManager.apply_costs(2.0, fee_pct=0.2, spread_pct=0.05, slippage_pct=0.05) == 1.7
