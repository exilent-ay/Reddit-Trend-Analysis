"""
summarizer.py — Placeholder LLM-based summariser.

Generates short, original internal summaries of trending topics.
Summaries are derived from aggregated metadata — NOT copied Reddit content.
"""

from __future__ import annotations


class TrendSummarizer:
    """
    Generates concise internal summaries of trending topics per niche.

    Uses an LLM (e.g. OpenAI GPT or a local model) to produce original
    text. No Reddit content is included verbatim in the output.
    """

    def __init__(self, provider: str = "openai", model: str = "gpt-4o-mini") -> None:
        """
        Initialise the summariser with LLM provider settings.

        Args:
            provider: LLM provider name (e.g. ``"openai"``).
            model: Model identifier to use for generation.
        """
        self.provider = provider
        self.model = model
        # TODO: Initialise the LLM client (e.g. openai.AsyncOpenAI).

    async def summarize_niche(self, niche: str, trending_titles: list[str]) -> str:
        """
        Produce an original internal summary for a single niche.

        Args:
            niche: The niche name (e.g. ``"tech_gadgets"``).
            trending_titles: List of trending post titles from the niche.
                             Used as signals only — not reproduced verbatim.

        Returns:
            An original plain-text summary suitable for internal reporting.
        """
        # TODO: Build a prompt and call the LLM API.
        raise NotImplementedError("summarize_niche() is not yet implemented.")

    async def summarize_all(self, niche_data: dict[str, list[str]]) -> dict[str, str]:
        """
        Summarise all niches in a single call.

        Args:
            niche_data: Mapping of niche name → list of trending titles.

        Returns:
            Mapping of niche name → original summary string.
        """
        # TODO: Implement concurrent summarisation across niches.
        raise NotImplementedError("summarize_all() is not yet implemented.")
