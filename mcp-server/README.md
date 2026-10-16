# MCP Server

A local MCP scaffold for retrieving synthetic case data from `src/data/sample_cases.json`. The JSON-backed service is for development only; replace it with an authenticated, authorization-aware Case Manager API before using real case records.

## Run

From this directory:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py -m src.server
```

The server uses stdio transport. It exposes `get_case_details`, `get_case_notes`, `get_case_activities`, and `explain_case_closure`. Example case IDs are `CMI-1001` and `CMI-1002`.
