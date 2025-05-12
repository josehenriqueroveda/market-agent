from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import tool


@tool("DuckDuckGo News Search")
def search_grain_market_news(query: str) -> str:
    """Search recent news about grain markets like corn, soy, and sorghum"""
    search = DuckDuckGoSearchRun(backend="news")
    return search.run(query)
