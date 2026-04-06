-- schema.sql — Canonical DDL for the Reddit Trend Analysis database.
-- This file documents the intended schema.
-- Tables are also created automatically via SQLAlchemy (storage.py).

-- Minimal Reddit post metadata (no full content stored or redistributed)
CREATE TABLE IF NOT EXISTS post_records (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id     TEXT    NOT NULL UNIQUE,   -- Reddit post ID (e.g. "t3_abc123")
    subreddit   TEXT    NOT NULL,
    niche       TEXT    NOT NULL,          -- tech_gadgets | home_kitchen | fitness_health
    title       TEXT    NOT NULL,
    score       INTEGER NOT NULL DEFAULT 0,
    created_utc REAL    NOT NULL,          -- Unix timestamp from Reddit API
    excerpt     TEXT    NOT NULL DEFAULT '',
    ingested_at TEXT    NOT NULL DEFAULT (datetime('now'))
);

-- Internally generated trend summaries (original text, not Reddit content)
CREATE TABLE IF NOT EXISTS trend_summaries (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    niche        TEXT    NOT NULL,
    summary_text TEXT    NOT NULL,
    generated_at TEXT    NOT NULL DEFAULT (datetime('now'))
);

-- Indexes for common query patterns
CREATE INDEX IF NOT EXISTS idx_post_records_niche       ON post_records (niche);
CREATE INDEX IF NOT EXISTS idx_post_records_ingested_at ON post_records (ingested_at);
CREATE INDEX IF NOT EXISTS idx_trend_summaries_niche    ON trend_summaries (niche);
