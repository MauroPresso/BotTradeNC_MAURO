from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class MarketSnapshot:
    provider: str
    symbol: str
    timestamp_utc: datetime
    price: Optional[float] = None
    bid: Optional[float] = None
    ask: Optional[float] = None
    volume_24h_usd: Optional[float] = None
    volume_24h_token: Optional[float] = None
    market_cap: Optional[float] = None


@dataclass(frozen=True)
class FeatureSnapshot:
    symbol_pair: str
    timestamp_utc: datetime
    ratio_value: float
    sma_ratio: Optional[float] = None
    ema_ratio: Optional[float] = None
    volatility_value: Optional[float] = None
    e_pct: Optional[float] = None
    volume_ratio: Optional[float] = None
    regime: Optional[str] = None


@dataclass(frozen=True)
class Signal:
    timestamp_utc: datetime
    symbol_pair: str
    signal_type: str
    reason: str


@dataclass(frozen=True)
class Trade:
    symbol_pair: str
    entry_timestamp_utc: datetime
    entry_price: float
    position_size: float
    exit_timestamp_utc: Optional[datetime] = None
    exit_price: Optional[float] = None
    exit_reason: Optional[str] = None
