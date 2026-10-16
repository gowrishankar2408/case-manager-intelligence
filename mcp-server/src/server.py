from mcp.server.fastmcp import FastMCP

from src.tools.explain_case_closure import explain_case_closure
from src.tools.get_case_activities import get_case_activities
from src.tools.get_case_details import get_case_details
from src.tools.get_case_notes import get_case_notes

mcp = FastMCP("case-manager-intelligence")

mcp.tool()(get_case_details)
mcp.tool()(get_case_notes)
mcp.tool()(get_case_activities)
mcp.tool()(explain_case_closure)

if __name__ == "__main__":
    print("Starting Case Manager Intelligence MCP Server...")
    print("Registered Tools:")
    print("- get_case_details")
    print("- get_case_notes")
    print("- get_case_activities")
    print("- explain_case_closure")

    mcp.run(transport="streamable-http")
