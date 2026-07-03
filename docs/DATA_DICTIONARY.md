# Data Dictionary

## Core concepts

### Market snapshot

A timestamped observation of market data from a provider such as CMC or Bitfinex.

### Feature snapshot

A timestamped derived record calculated from raw or validated market data.

### Signal

A deterministic output from the signal engine indicating a possible entry, exit or neutral state.

### Trade

A simulated or real operation generated from signals and execution assumptions.

### Experiment

A named research hypothesis or strategy family.

### Run

A concrete execution of an experiment with a specific code version, parameter set and data window.

## Suggested important fields

### experiments

```text
experiment_id
name
description
research_question
created_at
status
```

### runs

```text
run_id
experiment_id
strategy_version
code_version
config_hash
data_start
data_end
mode
created_at
notes
```

### parameters

```text
run_id
parameter_name
parameter_value
parameter_type
```

### signals

```text
signal_id
run_id
timestamp
symbol_pair
signal_type
reason
feature_context_json
```

### trades

```text
trade_id
run_id
entry_timestamp
exit_timestamp
symbol_pair
entry_price
exit_price
position_size
fee_cost
spread_cost
slippage_cost
net_result_pct
exit_reason
```

### ai_analysis

```text
analysis_id
run_id
analysis_type
model_name
prompt_version
summary
created_at
human_reviewed
```
