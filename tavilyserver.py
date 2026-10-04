import os
from dotenv import load_dotenv
from tavily import TavilyClient
from mcp.server import MCPServer

load_dotenv()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

mcp = MCPServer("Tavily") ## this is server name

@mcp.tool()
def web_search(query: str, max_results: int = 5) -> dict:
    """this is for searching the internet"""
    return tavily.search(query=query, max_results=max_results, include_answer=True)
@mcp.tool()
def scrape_url(url: str) -> dict:
    """this is for scraping the content of a web page"""
    return tavily.extract(urls=[url], format="markdown")

if __name__=='__main__':
    #mcp.run(transport='streamable-http', host='0.0.0.0', port=int(os.getenv("PORT", 8000)))
    mcp.run(transport='stdio') 
