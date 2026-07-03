# Runbook

## Purpose

This runbook describes how to operate BotTradeNC as a system rather than as a set of isolated scripts.

## Daily checks

- Confirm market data capture is running.
- Confirm latest snapshot timestamp is recent.
- Confirm no duplicate process is running.
- Confirm no major data gaps were detected.
- Confirm log files are growing normally.
- Confirm disk space is sufficient.
- Confirm backtest reports can be generated.

## Operational risks

### Capture script appears running but log is frozen

Action:

1. Check latest log timestamp.
2. Check latest database snapshot timestamp.
3. Stop duplicate/stuck process.
4. Restart capture engine.
5. Register a system event.

### Internet outage

Action:

1. Wait for connectivity recovery.
2. Resume capture.
3. Register missing intervals as data quality events.
4. Do not silently interpolate critical trading data.

### Duplicate execution

Action:

1. Use a lock file or process lock.
2. Prevent a second capture process from writing simultaneously.
3. Log the blocked duplicate start.

## Watchdog target

The watchdog should detect:

- stale logs,
- stale database snapshots,
- duplicate processes,
- repeated API errors,
- disk-space warnings,
- configuration errors.
