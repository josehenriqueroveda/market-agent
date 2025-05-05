from langchain_community.tools import DuckDuckGoSearchResults
from crewai.tools import tool

news_tool = DuckDuckGoSearchResults(backend="news")


@tool("DuckDuckGoSearch")
def news_tool(search_query: str):
    """Search the web for news of a given topic"""
    return DuckDuckGoSearchResults().run(search_query)
