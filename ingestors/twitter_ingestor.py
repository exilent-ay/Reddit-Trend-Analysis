"""
twitter_ingestor.py — Placeholder for a future Twitter/X data ingestor.

Not in scope for the initial release. Stub is provided for structural
completeness and future expansion.
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


class TwitterIngestor:
    """Placeholder ingestor for Twitter/X trend data (not yet implemented)."""

    async def run(self, queries: list[str]) -> None:
        """
        Fetch trending data from Twitter/X for the given search queries.

        Args:
            queries: List of search terms or hashtags to monitor.
        """
        # TODO: Implement Twitter/X API integration in a future milestone.
        raise NotImplementedError("TwitterIngestor is not yet implemented.")
