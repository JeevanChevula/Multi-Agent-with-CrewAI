# tools/tavily_tool.py

from crewai.tools import tool
from tavily import TavilyClient
import os

@tool("Web Search Tool")
def web_search_tool(query: str) -> str:
    """
    Searches the web for current information about a given query.
    Use this tool when you need to find recent or factual information.
    """
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    
    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )
    
    results = []
    for result in response.get("results", []):
        results.append(f"Title: {result['title']}\nURL: {result['url']}\nContent: {result['content']}")
    
    return "\n\n".join(results)