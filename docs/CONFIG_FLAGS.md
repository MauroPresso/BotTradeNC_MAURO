# Configuration Flags

## Purpose

Every important strategy parameter must be explicit, versioned and stored with each experiment run.

## Example strategy flags

```text
REQUIRE_ENTRY_STILL_CHEAP_AT_TRIGGER
MAX_ENTRY_ABOVE_MNOW_PCT
MAX_ENTRY_E_PCT
TRIANGLE_R_EMA_REBOUND_MIN_BARS
TRIANGLE_R_EMA_REBOUND_EPS_PCT_PER_BAR
PROFIT_TARGET_PCT
STOP_LOSS_PCT
TRADE_FRACTION
CAPITAL_BASE
```

## Configuration principles

- Never change a parameter silently.
- Every backtest run must store a full parameter snapshot.
- Every report must show the strategy version and configuration hash.
- Experimental flags should be documented before being used in comparisons.
