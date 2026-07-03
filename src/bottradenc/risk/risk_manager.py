class RiskManager:
    """Centralizes position sizing and execution assumptions."""

    def __init__(self, capital_base: float, trade_fraction: float):
        if capital_base <= 0:
            raise ValueError("capital_base must be greater than zero")
        if not 0 < trade_fraction <= 1:
            raise ValueError("trade_fraction must be in the (0, 1] range")
        self.capital_base = capital_base
        self.trade_fraction = trade_fraction

    def position_size(self) -> float:
        return self.capital_base * self.trade_fraction

    @staticmethod
    def apply_costs(gross_result_pct: float, fee_pct: float, spread_pct: float, slippage_pct: float) -> float:
        return gross_result_pct - fee_pct - spread_pct - slippage_pct
