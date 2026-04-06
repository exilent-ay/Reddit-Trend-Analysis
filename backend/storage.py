"""
storage.py — SQLAlchemy database interface.

Defines ORM models and a repository class for persisting trend analysis
results. Supports SQLite (default) and Postgres.
"""

from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    Integer,
    String,
    Text,
    create_engine,
)
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


# ---------------------------------------------------------------------------
# ORM Base
# ---------------------------------------------------------------------------


class Base(DeclarativeBase):
    """Shared declarative base for all ORM models."""


# ---------------------------------------------------------------------------
# ORM Models
# ---------------------------------------------------------------------------


class PostRecord(Base):
    """Stores minimal Reddit post metadata used for trend analysis."""

    __tablename__ = "post_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(String(32), unique=True, nullable=False, index=True)
    subreddit = Column(String(128), nullable=False)
    niche = Column(String(64), nullable=False)
    title = Column(String(512), nullable=False)
    score = Column(Integer, default=0)
    created_utc = Column(Float, nullable=False)
    excerpt = Column(Text, default="")
    ingested_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


class TrendSummary(Base):
    """Stores generated internal trend summaries per niche."""

    __tablename__ = "trend_summaries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    niche = Column(String(64), nullable=False, index=True)
    summary_text = Column(Text, nullable=False)
    generated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


# ---------------------------------------------------------------------------
# Database engine / session factory
# ---------------------------------------------------------------------------


def create_db_engine(database_url: str = "sqlite:///./reddit_trends.db"):
    """
    Create and return a SQLAlchemy engine.

    Args:
        database_url: SQLAlchemy-compatible connection string.

    Returns:
        A configured :class:`sqlalchemy.engine.Engine` instance.
    """
    connect_args = {"check_same_thread": False} if database_url.startswith("sqlite") else {}
    return create_engine(database_url, connect_args=connect_args)


def init_db(engine) -> None:
    """Create all tables if they do not already exist."""
    Base.metadata.create_all(bind=engine)


# ---------------------------------------------------------------------------
# Repository
# ---------------------------------------------------------------------------


class TrendRepository:
    """
    Data-access layer for reading and writing trend analysis records.

    All methods operate within explicit SQLAlchemy sessions to keep
    transaction control in the caller.
    """

    def __init__(self, session: Session) -> None:
        self.session = session

    def save_post(self, post: PostRecord) -> None:
        """Persist a :class:`PostRecord`, ignoring duplicates by post_id."""
        # TODO: Implement upsert / duplicate check.
        raise NotImplementedError("save_post() is not yet implemented.")

    def save_summary(self, summary: TrendSummary) -> None:
        """Persist a :class:`TrendSummary`."""
        # TODO: Implement insert.
        raise NotImplementedError("save_summary() is not yet implemented.")

    def get_recent_posts(self, niche: str, limit: int = 50) -> list[PostRecord]:
        """
        Retrieve the most recently ingested posts for a given niche.

        Args:
            niche: Niche name to filter by.
            limit: Maximum number of records to return.

        Returns:
            List of :class:`PostRecord` objects ordered by ingestion time.
        """
        # TODO: Implement query.
        raise NotImplementedError("get_recent_posts() is not yet implemented.")

    def get_latest_summary(self, niche: str) -> TrendSummary | None:
        """Return the most recent :class:`TrendSummary` for a given niche."""
        # TODO: Implement query.
        raise NotImplementedError("get_latest_summary() is not yet implemented.")
