"""
reddit_ingestor.py — Orchestrates fetching and storing Reddit post metadata.

This module ties together :class:`RedditAPIClient`, :class:`NicheClassifier`,
and :class:`TrendRepository` to run a full Reddit ingestion cycle.
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


class RedditIngestor:
    """
    Coordinates a full ingestion cycle for configured Reddit subreddits.

    Retrieves minimal public metadata only — no full post bodies are
    stored or redistributed.
    """

    def __init__(self, client, classifier, repository) -> None:
        """
        Initialise with pre-configured collaborators.

        Args:
            client: An instance of :class:`~backend.reddit_api_client.RedditAPIClient`.
            classifier: An instance of :class:`~backend.classifier.NicheClassifier`.
            repository: An instance of :class:`~backend.storage.TrendRepository`.
        """
        self.client = client
        self.classifier = classifier
        self.repository = repository

    async def run(self, subreddits: dict[str, list[str]]) -> None:
        """
        Execute one ingestion cycle across all configured subreddits.

        Args:
            subreddits: Mapping of niche name → list of subreddit names.
        """
        # TODO: Implement ingestion loop.
        raise NotImplementedError("RedditIngestor.run() is not yet implemented.")
