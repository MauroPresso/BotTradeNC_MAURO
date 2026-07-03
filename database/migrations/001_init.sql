-- BotTradeNC AI-Native initial schema
-- SQLite-compatible draft schema.

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS market_snapshots_raw (
    snapshot_id INTEGER PRIMARY KEY AUTOINCREMENT,
    provider TEXT NOT NULL,
    symbol TEXT NOT NULL,
    capture_timestamp_utc TEXT NOT NULL,
    price REAL,
    bid REAL,
    ask REAL,
    volume_24h_usd REAL,
    volume_24h_token REAL,
    market_cap REAL,
    payload_json TEXT,
    created_at_utc TEXT NOT NULL DEFAULT (datetime('now')),
    UNIQUE(provider, symbol, capture_timestamp_utc)
);

CREATE TABLE IF NOT EXISTS data_quality_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    provider TEXT,
    symbol TEXT,
    event_timestamp_utc TEXT NOT NULL,
    event_type TEXT NOT NULL,
    severity TEXT NOT NULL,
    description TEXT,
    context_json TEXT,
    created_at_utc TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS feature_snapshots (
    feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol_pair TEXT NOT NULL,
    feature_timestamp_utc TEXT NOT NULL,
    ratio_value REAL,
    sma_ratio REAL,
    ema_ratio REAL,
    volatility_value REAL,
    e_pct REAL,
    volume_ratio REAL,
    regime TEXT,
    context_json TEXT,
    created_at_utc TEXT NOT NULL DEFAULT (datetime('now')),
    UNIQUE(symbol_pair, feature_timestamp_utc)
);

CREATE TABLE IF NOT EXISTS experiments (
    experiment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    research_question TEXT,
    status TEXT NOT NULL DEFAULT 'draft',
    created_at_utc TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS runs (
    run_id INTEGER PRIMARY KEY AUTOINCREMENT,
    experiment_id INTEGER NOT NULL,
    strategy_version TEXT NOT NULL,
    code_version TEXT,
    config_hash TEXT,
    data_start_utc TEXT,
    data_end_utc TEXT,
    backtest_mode TEXT NOT NULL,
    notes TEXT,
    created_at_utc TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (experiment_id) REFERENCES experiments(experiment_id)
);

CREATE TABLE IF NOT EXISTS parameters (
    parameter_id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id INTEGER NOT NULL,
    parameter_name TEXT NOT NULL,
    parameter_value TEXT NOT NULL,
    parameter_type TEXT,
    FOREIGN KEY (run_id) REFERENCES runs(run_id),
    UNIQUE(run_id, parameter_name)
);

CREATE TABLE IF NOT EXISTS signals (
    signal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id INTEGER,
    signal_timestamp_utc TEXT NOT NULL,
    symbol_pair TEXT NOT NULL,
    signal_type TEXT NOT NULL,
    reason TEXT,
    feature_context_json TEXT,
    created_at_utc TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (run_id) REFERENCES runs(run_id)
);

CREATE TABLE IF NOT EXISTS trades (
    trade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id INTEGER NOT NULL,
    symbol_pair TEXT NOT NULL,
    entry_timestamp_utc TEXT NOT NULL,
    exit_timestamp_utc TEXT,
    entry_price REAL NOT NULL,
    exit_price REAL,
    position_size REAL NOT NULL,
    fee_cost REAL DEFAULT 0,
    spread_cost REAL DEFAULT 0,
    slippage_cost REAL DEFAULT 0,
    gross_result_pct REAL,
    net_result_pct REAL,
    exit_reason TEXT,
    trade_context_json TEXT,
    FOREIGN KEY (run_id) REFERENCES runs(run_id)
);

CREATE TABLE IF NOT EXISTS capital_curve (
    curve_id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id INTEGER NOT NULL,
    curve_timestamp_utc TEXT NOT NULL,
    capital_value REAL NOT NULL,
    drawdown_pct REAL,
    context_json TEXT,
    FOREIGN KEY (run_id) REFERENCES runs(run_id),
    UNIQUE(run_id, curve_timestamp_utc)
);

CREATE TABLE IF NOT EXISTS system_events (
    system_event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_timestamp_utc TEXT NOT NULL,
    component TEXT NOT NULL,
    event_type TEXT NOT NULL,
    severity TEXT NOT NULL,
    description TEXT,
    context_json TEXT,
    created_at_utc TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS ai_analysis (
    analysis_id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id INTEGER,
    analysis_type TEXT NOT NULL,
    model_name TEXT,
    prompt_version TEXT,
    summary TEXT NOT NULL,
    human_reviewed INTEGER NOT NULL DEFAULT 0,
    created_at_utc TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (run_id) REFERENCES runs(run_id)
);

CREATE INDEX IF NOT EXISTS idx_market_snapshots_symbol_time
ON market_snapshots_raw(symbol, capture_timestamp_utc);

CREATE INDEX IF NOT EXISTS idx_features_pair_time
ON feature_snapshots(symbol_pair, feature_timestamp_utc);

CREATE INDEX IF NOT EXISTS idx_trades_run
ON trades(run_id);

CREATE INDEX IF NOT EXISTS idx_signals_run_time
ON signals(run_id, signal_timestamp_utc);
