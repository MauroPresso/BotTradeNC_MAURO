from datetime import datetime
from pathlib import Path

from bottradenc.ops.watchdog import Watchdog


def main() -> None:
    log_path = Path("logs/bitfinex_capture.log")
    stale = Watchdog.is_log_stale(log_path, datetime.utcnow(), max_stale_minutes=15)
    print(f"log_path={log_path} stale={stale}")


if __name__ == "__main__":
    main()
