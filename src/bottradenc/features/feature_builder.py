class FeatureBuilder:
    """Builds deterministic features such as ETH/BTC ratio, moving averages and volatility."""

    @staticmethod
    def ratio(numerator_price: float, denominator_price: float) -> float:
        if denominator_price <= 0:
            raise ValueError("denominator_price must be greater than zero")
        return numerator_price / denominator_price

    @staticmethod
    def e_pct(ratio_value: float, reference_value: float) -> float:
        if reference_value <= 0:
            raise ValueError("reference_value must be greater than zero")
        return ((ratio_value / reference_value) - 1.0) * 100.0
