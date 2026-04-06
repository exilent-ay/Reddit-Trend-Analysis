#!/usr/bin/env bash
# run_ingest.sh — Manually trigger a single ingestion pipeline run.
#
# Usage:
#   ./scripts/run_ingest.sh
#
# Environment variables:
#   CONFIG_PATH   Path to config.yaml (default: config/config.yaml)
#   DATABASE_URL  Override the database URL from config (optional)
#
# This script is intended for local testing and cron-based scheduling.

set -euo pipefail

CONFIG_PATH="${CONFIG_PATH:-config/config.yaml}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

echo "[run_ingest.sh] Starting ingestion — $(date -u '+%Y-%m-%dT%H:%M:%SZ')"

# Activate virtualenv if present
if [ -f "$ROOT_DIR/.venv/bin/activate" ]; then
    # shellcheck source=/dev/null
    source "$ROOT_DIR/.venv/bin/activate"
fi

# TODO: Replace with actual CLI entry point once implemented.
python -c "
from backend.scheduler import run_ingestion_pipeline
run_ingestion_pipeline()
"

echo "[run_ingest.sh] Ingestion complete — $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
