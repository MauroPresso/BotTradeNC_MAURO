from typing import Iterable, Protocol

from bottradenc.domain.models import MarketSnapshot


class CaptureProvider(Protocol):
    def capture(self) -> Iterable[MarketSnapshot]:
        ...


class CaptureEngine:
    """Coordinates one or more market data providers."""

    def __init__(self, providers: list[CaptureProvider]):
        self.providers = providers

    def capture_all(self) -> list[MarketSnapshot]:
        snapshots: list[MarketSnapshot] = []
        for provider in self.providers:
            snapshots.extend(provider.capture())
        return snapshots
