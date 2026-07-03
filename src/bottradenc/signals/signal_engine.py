from bottradenc.domain.models import FeatureSnapshot, Signal


class SignalEngine:
    """Generates deterministic entry/exit signals from feature snapshots."""

    def evaluate(self, feature: FeatureSnapshot) -> Signal:
        # Placeholder: replace with conservative ETH/BTC noisy-lateral logic.
        return Signal(
            timestamp_utc=feature.timestamp_utc,
            symbol_pair=feature.symbol_pair,
            signal_type="HOLD",
            reason="Initial placeholder signal engine.",
        )
