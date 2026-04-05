"""
scheduler.py — Placeholder for cron-triggered ingestion jobs.

Uses APScheduler to run periodic data ingestion pipelines.
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


def run_ingestion_pipeline() -> None:
    """
    Entry point for a single ingestion cycle.

    Steps (to be implemented):
      1. Authenticate with the Reddit API.
      2. Fetch hot posts from configured subreddits.
      3. Classify each post into a niche.
      4. Persist minimal metadata to the database.
      5. Trigger summary generation if thresholds are met.
    """
    logger.info("Starting ingestion pipeline run.")
    # TODO: Implement full pipeline orchestration.
    raise NotImplementedError("run_ingestion_pipeline() is not yet implemented.")


def start_scheduler(interval_minutes: int = 60) -> None:
    """
    Configure and start the APScheduler background scheduler.

    Args:
        interval_minutes: How often (in minutes) to trigger
                          :func:`run_ingestion_pipeline`.
    """
    try:
        from apscheduler.schedulers.background import BackgroundScheduler

        scheduler = BackgroundScheduler()
        scheduler.add_job(
            run_ingestion_pipeline,
            trigger="interval",
            minutes=interval_minutes,
            id="ingestion_pipeline",
            replace_existing=True,
        )
        scheduler.start()
        logger.info(
            "Scheduler started — ingestion every %d minute(s).", interval_minutes
        )
        return scheduler
    except Exception as exc:
        logger.error("Failed to start scheduler: %s", exc)
        raise
