# MCP Server

This Python scaffold exposes case-intelligence tools over the Model Context Protocol using stdio transport. It is not connected to a live Case Manager API.

## Run

From this directory:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
Push-Location src
py server.py
Pop-Location
```

The tool functions in `src/tools/` are registered by `src/server.py`. They currently raise `NotImplementedError`; implement service calls only after defining API contracts, authentication, case-level authorization, validation, and audit behavior.
