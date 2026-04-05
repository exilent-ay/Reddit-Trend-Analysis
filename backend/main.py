"""
main.py — FastAPI application entry point for Reddit Trend Analysis Tool.

Provides a healthcheck endpoint and wires up routers for future modules.
"""

from fastapi import FastAPI

app = FastAPI(
    title="Reddit Trend Analysis Tool",
    description=(
        "Analyzes public subreddit posts to identify trending topics in "
        "Tech Gadgets & Electronics, Home & Kitchen, and Fitness & Health. "
        "Generates internal summaries only — does not redistribute Reddit content."
    ),
    version="0.1.0",
)


@app.get("/health", tags=["Health"])
async def healthcheck() -> dict:
    """Return a simple health status for the service."""
    return {"status": "ok", "service": "reddit-trend-analysis"}


# ---------------------------------------------------------------------------
# Future routers — uncomment as modules are implemented
# ---------------------------------------------------------------------------
# from backend.routers import trends, summaries
# app.include_router(trends.router, prefix="/trends", tags=["Trends"])
# app.include_router(summaries.router, prefix="/summaries", tags=["Summaries"])
