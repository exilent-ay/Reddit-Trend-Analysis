"""
tiktok_ingestor.py — Placeholder for a future TikTok trend ingestor.

Not in scope for the initial release. Stub is provided for structural
completeness and future expansion.
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


class TikTokIngestor:
    """Placeholder ingestor for TikTok trend data (not yet implemented)."""

    async def run(self, hashtags: list[str]) -> None:
        """
        Fetch trending data from TikTok for the given hashtags.

        Args:
            hashtags: List of hashtag strings (without the ``#`` prefix).
        """
        # TODO: Implement TikTok API integration in a future milestone.
        raise NotImplementedError("TikTokIngestor is not yet implemented.")
