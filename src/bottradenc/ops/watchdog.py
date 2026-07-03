from datetime import datetime, timedelta
from pathlib import Path


class Watchdog:
    """Operational health checks for capture and logging processes."""

    @staticmethod
    def is_log_stale(log_path: Path, now_utc: datetime, max_stale_minutes: int) -> bool:
        if not log_path.exists():
            return True
        last_modified = datetime.utcfromtimestamp(log_path.stat().st_mtime)
        return now_utc - last_modified > timedelta(minutes=max_stale_minutes)
