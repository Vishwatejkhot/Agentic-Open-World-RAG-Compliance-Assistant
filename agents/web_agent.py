import os
from dotenv import load_dotenv
from tavily import TavilyClient

# ✅ Load environment variables FIRST
load_dotenv()

# ✅ Optional safety check
assert os.getenv("TAVILY_API_KEY") is not None, "TAVILY_API_KEY not loaded"

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def web_agent(query: str):
    """
    Performs live web search using Tavily.
    """
    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5,
        include_answer=False
    )

    return [
        {
            "title": r["title"],
            "content": r["content"],
            "url": r["url"]
        }
        for r in response["results"]
    ]
