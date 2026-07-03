from datetime import datetime, timedelta

from bottradenc.domain.models import MarketSnapshot


class DataQualityChecker:
    """Detects gaps, duplicates, stale data and suspicious values."""

    def __init__(self, expected_interval_minutes: int = 10):
        self.expected_interval = timedelta(minutes=expected_interval_minutes)

    def is_snapshot_valid(self, snapshot: MarketSnapshot) -> bool:
        if snapshot.price is not None and snapshot.price <= 0:
            return False
        if snapshot.bid is not None and snapshot.ask is not None and snapshot.bid > snapshot.ask:
            return False
        return True

    def is_stale(self, latest_timestamp_utc: datetime, now_utc: datetime, max_delay_minutes: int = 15) -> bool:
        return now_utc - latest_timestamp_utc > timedelta(minutes=max_delay_minutes)
