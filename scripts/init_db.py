from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "bottradenc.db"
MIGRATION = ROOT / "database" / "migrations" / "001_init.sql"


def main() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    sql = MIGRATION.read_text(encoding="utf-8")
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(sql)
    print(f"Database initialized: {DB_PATH}")


if __name__ == "__main__":
    main()
