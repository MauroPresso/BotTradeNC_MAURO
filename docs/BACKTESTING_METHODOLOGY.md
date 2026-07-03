# Backtesting Methodology

## Goal

The goal of backtesting in BotTradeNC is not to prove guaranteed profitability. The goal is to evaluate whether a strategy hypothesis deserves further research under reproducible and realistic assumptions.

## Backtest levels

### Ideal backtest

- Entry and exit at theoretical prices.
- No spread.
- No slippage.
- No execution latency.

Useful only as a baseline.

### Realistic backtest

- Includes exchange fees.
- Includes estimated spread.
- Uses bid/ask-aware execution assumptions when available.
- Includes realistic position sizing.

This should become the default evaluation mode.

### Pessimistic backtest

- Adds adverse slippage.
- Adds execution delay.
- Penalizes incomplete data.
- Stress-tests fragile strategies.

A strategy that only works in the ideal mode should not be trusted.

## Required metrics

Each run should store:

```text
capital_initial
capital_final
net_return_pct
max_drawdown_pct
trade_count
win_rate
profit_factor
expectancy
average_win
average_loss
best_trade
worst_trade
fees_paid
spread_cost_estimate
slippage_cost_estimate
```

## Methodological risks

The system must explicitly check for:

- look-ahead bias,
- overfitting,
- too few trades,
- unrealistic entry/exit prices,
- missing commission model,
- missing spread model,
- missing slippage model,
- parameter sensitivity,
- market regime dependency.

## ETH/BTC research principle

The initial BotTradeNC research logic is conservative and focused on ETH/BTC spot behavior. It should be evaluated as a research hypothesis, not as a trading promise.
