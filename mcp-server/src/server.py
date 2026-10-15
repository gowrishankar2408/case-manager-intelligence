from mcp.server.fastmcp import FastMCP

from tools.download_attachment import download_attachment
from tools.explain_case_closure import explain_case_closure
from tools.get_case_activities import get_case_activities
from tools.get_case_attachments import get_case_attachments
from tools.get_case_details import get_case_details
from tools.get_case_history import get_case_history
from tools.get_case_notes import get_case_notes
from tools.search_similar_cases import search_similar_cases

mcp = FastMCP("case-manager-intelligence")

for tool in (
    get_case_details,
    get_case_notes,
    get_case_activities,
    get_case_history,
    get_case_attachments,
    download_attachment,
    search_similar_cases,
    explain_case_closure,
):
    mcp.tool()(tool)


if __name__ == "__main__":
    mcp.run(transport="stdio")
