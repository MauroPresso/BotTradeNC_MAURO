# Architecture

## Purpose

BotTradeNC is designed as an AI-native quantitative research system. The architecture separates deterministic computation from AI-assisted interpretation.

The core trading research pipeline must remain reproducible, testable and auditable. AI modules are used to assist analysis, summarize experiments, detect anomalies and generate documentation, not to make uncontrolled financial decisions.

## Main layers

### 1. Deterministic Core

Responsible for:

- data capture,
- timestamp normalization,
- duplicate detection,
- gap detection,
- feature calculation,
- signal generation,
- backtesting,
- risk assumptions,
- reports,
- logs,
- watchdog checks.

This layer must work without AI.

### 2. AI-Ready Data Layer

Responsible for storing structured context:

- experiment identifiers,
- run identifiers,
- strategy versions,
- parameter snapshots,
- trade history,
- signal history,
- data quality events,
- system events,
- human notes,
- AI summaries.

The goal is to make the project queryable by humans and AI assistants.

### 3. AI-Native Analysis Layer

Responsible for:

- explaining trades,
- comparing experiments,
- detecting suspicious backtest improvements,
- summarizing daily system behavior,
- generating changelog drafts,
- identifying operational anomalies.

AI output must be stored as analysis, not as ground truth.

### 4. Product / Portfolio Layer

Responsible for making the system understandable externally:

- README,
- diagrams,
- case studies,
- demo reports,
- methodology documents,
- LinkedIn/GitHub positioning.

## Suggested module map

```text
CaptureEngine
DataRepository
DataQualityChecker
FeatureBuilder
SignalEngine
Backtester
RiskManager
ExecutionSimulator
ExperimentManager
AIBacktestReviewer
AIMarketAnalyst
Watchdog
ReportGenerator
ConfigManager
```

## Design principle

The strongest version of BotTradeNC is not a script that claims to trade profitably. It is a documented system that proves the builder can design, implement, test, operate and explain complex AI-native data systems.
