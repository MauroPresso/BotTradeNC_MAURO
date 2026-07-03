# BotTradeNC AI-Native Quant Research System

**BotTradeNC** is an AI-native quantitative research system for crypto markets.

It is designed to capture market data, validate data quality, build trading features, run reproducible backtests, explain strategy behavior with AI-assisted analysis, and support human-supervised trading research.

> This project is not a promise of profitability and does not provide financial advice. It is a software, data, and research system focused on reproducibility, auditability, and responsible experimentation.

## Strategic positioning

BotTradeNC should not be presented as a “magic trading bot”. The correct positioning is:

> An AI-native quantitative research lab for crypto markets, focused on data quality, strategy experimentation, backtesting methodology, operational reliability, and explainable decision support.

## Current research focus

The first research use case is the **ETH/BTC spot pair**, with a conservative non-conventional strategy originally framed as:

- noisy lateral market behavior,
- mean-reversion logic,
- “buy cheap + EMA trigger + sell expensive / stop loss”,
- human-supervised operation,
- no leverage,
- no margin,
- BTC accumulation as a research objective.

## System layers

```text
1. Deterministic Core
   Data capture, validation, features, rules, backtesting, risk controls and logs.

2. AI-Ready Data Layer
   Structured storage of experiments, parameters, runs, trades, anomalies and decisions.

3. AI-Native Layer
   AI-assisted explanations, experiment comparison, anomaly summaries and documentation.

4. Global Product Layer
   Portfolio-ready, documented, extensible and suitable for future productization.
```

## Repository goals

- Build a professional portfolio-grade project.
- Keep trading logic reproducible and auditable.
- Avoid black-box automated decision-making.
- Separate research, backtesting, risk control and execution.
- Prepare the project for GitHub, LinkedIn, interviews and international positioning.
- Make the system understandable by humans and AI assistants.

## Initial architecture

```text
src/bottradenc/
  capture/       Market data capture engines
  data/          Repositories and database access
  quality/       Data quality checks
  features/      Feature engineering
  signals/       Entry/exit signal generation
  backtesting/   Backtesting engine
  risk/          Risk and execution assumptions
  ai/            AI-assisted analysis modules
  ops/           Watchdog and operational health checks
  reporting/     Reports, summaries and exports
  domain/        Core models

database/
  migrations/    SQL schema and migrations

docs/
  Architecture, methodology, risk, runbook and roadmap

configs/
  Example configuration files

scripts/
  Operational scripts

tests/
  Unit tests
```

## First milestones

1. Create the repository skeleton.
2. Define the database schema for experiments, runs, trades and data quality events.
3. Migrate the current BotTradeNC logic into modular Python/R components.
4. Build a reproducible backtesting pipeline.
5. Add watchdog and operational health checks.
6. Add AI-assisted reports, not autonomous trading decisions.
7. Publish a responsible portfolio case study.

## Responsible use

BotTradeNC must be developed with clear boundaries:

- No guaranteed returns.
- No financial advice.
- No autonomous live trading without explicit human supervision and hard risk controls.
- No hidden optimization or overfitting claims.
- Every experiment must be reproducible.
- Every signal must be explainable.

## Suggested repository name

```text
BotTradeNC-AI-Native
```

Alternative names:

```text
BotTradeNC-QuantLab
BotTradeNC-ResearchLab
BotTradeNC-AI-Quant-Research
```
