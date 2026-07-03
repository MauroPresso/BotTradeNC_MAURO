import sqlite3
from pathlib import Path
from typing import Iterable

from bottradenc.domain.models import MarketSnapshot


class DataRepository:
    """SQLite repository for market data, experiments and results."""

    def __init__(self, database_path: Path):
        self.database_path = Path(database_path)

    def connect(self) -> sqlite3.Connection:
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(self.database_path)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def save_market_snapshots(self, snapshots: Iterable[MarketSnapshot]) -> int:
        rows = [
            (
                s.provider,
                s.symbol,
                s.timestamp_utc.isoformat(),
                s.price,
                s.bid,
                s.ask,
                s.volume_24h_usd,
                s.volume_24h_token,
                s.market_cap,
            )
            for s in snapshots
        ]
        if not rows:
            return 0
        with self.connect() as conn:
            conn.executemany(
                """
                INSERT OR IGNORE INTO market_snapshots_raw
                (provider, symbol, capture_timestamp_utc, price, bid, ask,
                 volume_24h_usd, volume_24h_token, market_cap)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                rows,
            )
            return conn.total_changes
