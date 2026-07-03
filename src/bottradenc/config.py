from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DatabaseConfig:
    database_path: Path


@dataclass(frozen=True)
class StrategyConfig:
    name: str
    version: str
    capital_base: float
    trade_fraction: float
    profit_target_pct: float
    stop_loss_pct: float
    require_entry_still_cheap_at_trigger: bool = True
    max_entry_above_mnow_pct: float = 0.30
    max_entry_e_pct: float = 0.00


@dataclass(frozen=True)
class BacktestConfig:
    mode: str
    fee_pct: float
    spread_pct: float
    slippage_pct: float
