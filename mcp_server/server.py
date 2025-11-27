from mcp.server.fastmcp import FastMCP
from service import RulesSearchService

mcp = FastMCP("rules_lawyer")

_service = RulesSearchService()


@mcp.tool("search_rules_tool")
def get_rules():
    try:
        return _service.search_rules("How does rapid fire work?", top_k=3)
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
     mcp.run(transport="stdio")
