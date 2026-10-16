# MCP Server

<<<<<<< HEAD
A local MCP scaffold for retrieving synthetic case data from `src/data/sample_cases.json`. The JSON-backed service is for development only; replace it with an authenticated, authorization-aware Case Manager API before using real case records.
=======
This Python scaffold exposes case-intelligence tools over the Model Context Protocol using stdio transport. It is not connected to a live Case Manager API.
>>>>>>> c0e1a89e4037a27593ef36b0736587fd7459782d

## Run

From this directory:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
<<<<<<< HEAD
py -m src.server
```

The server uses stdio transport. It exposes `get_case_details`, `get_case_notes`, `get_case_activities`, and `explain_case_closure`. Example case IDs are `CMI-1001` and `CMI-1002`.
=======
Push-Location src
py server.py
Pop-Location
```

The tool functions in `src/tools/` are registered by `src/server.py`. They currently raise `NotImplementedError`; implement service calls only after defining API contracts, authentication, case-level authorization, validation, and audit behavior.
>>>>>>> c0e1a89e4037a27593ef36b0736587fd7459782d
