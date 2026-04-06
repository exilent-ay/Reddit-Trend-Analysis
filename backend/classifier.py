"""
classifier.py — Placeholder niche classifier.

Classifies Reddit post titles/excerpts into one of three predefined niches:
  - Tech Gadgets & Electronics
  - Home & Kitchen
  - Fitness & Health
"""

from __future__ import annotations

from enum import Enum


class Niche(str, Enum):
    """Supported niche categories for trend analysis."""

    TECH_GADGETS = "tech_gadgets"
    HOME_KITCHEN = "home_kitchen"
    FITNESS_HEALTH = "fitness_health"
    UNKNOWN = "unknown"


class NicheClassifier:
    """
    Classifies a post into a :class:`Niche` based on its title and excerpt.

    The initial implementation will use simple keyword matching.
    A future version may delegate to an LLM or a trained classifier model.
    """

    def __init__(self) -> None:
        """Initialise the classifier with keyword rules or model weights."""
        # TODO: Load keyword lists or model artefacts.
        pass

    def classify(self, title: str, excerpt: str = "") -> Niche:
        """
        Classify a post into one of the supported niches.

        Args:
            title: The post title as returned by the Reddit API.
            excerpt: Short text excerpt (optional) used as supplementary signal.

        Returns:
            The predicted :class:`Niche` for the post.
        """
        # TODO: Implement classification logic (keyword matching or ML model).
        raise NotImplementedError("classify() is not yet implemented.")

    def batch_classify(self, posts: list[dict]) -> list[Niche]:
        """
        Classify a batch of posts.

        Args:
            posts: List of dicts with at least ``title`` and optionally
                   ``excerpt`` keys.

        Returns:
            A list of :class:`Niche` values in the same order as *posts*.
        """
        # TODO: Implement batch classification.
        raise NotImplementedError("batch_classify() is not yet implemented.")
