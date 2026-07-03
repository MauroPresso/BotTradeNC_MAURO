# AI-Native Design

## Definition in this project

AI-native does not mean adding a chatbot to an existing bot.

In BotTradeNC, AI-native means the system is intentionally designed so that AI assistants can work with structured context, logs, experiments, metrics, decisions and documentation.

## What AI can do

AI modules may:

- explain why a trade was triggered,
- summarize a backtest run,
- compare two experiments,
- detect suspicious improvements caused by overfitting,
- summarize logs,
- generate daily/weekly reports,
- draft technical documentation,
- propose hypotheses for future tests.

## What AI should not do by default

AI modules should not:

- execute live trades autonomously,
- override risk controls,
- hide uncertainty,
- claim profitability,
- modify strategy rules without versioning,
- make financial decisions without human approval.

## Initial AI assistants

### AI Market Analyst

Explains market behavior, feature movements and trade context.

### AI Backtest Reviewer

Reviews whether a backtest is realistic, robust and free from common methodological errors.

### AI Experiment Manager

Compares experiment runs and detects what changed between versions.

### AI Ops Analyst

Reads logs and health-check data to explain operational issues.

### AI Documentation Assistant

Generates reports, changelog drafts and technical summaries.

## Data required for AI usefulness

The AI layer needs structured data:

```text
experiment_id
run_id
strategy_version
code_version
data_window_start
data_window_end
parameters_used
signals
trades
capital_curve
data_quality_events
system_events
human_notes
ai_summary
```

Without structured data, AI becomes a superficial narrator. With structured data, it becomes an analysis assistant.
