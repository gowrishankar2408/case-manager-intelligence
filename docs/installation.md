# Installation

## Prerequisites

- Python 3.11 or later
- PowerShell 7 recommended for the helper scripts
- Access to an approved Case Manager API is not required to inspect the scaffold; credentials and API configuration are not included

## MCP Server

From the repository root, create and activate a virtual environment, then install the server dependency:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r mcp-server\requirements.txt
```

Run the stdio server from its source directory:

```powershell
Push-Location mcp-server\src
py server.py
Pop-Location
```

The tool signatures are scaffolding only and intentionally raise `NotImplementedError` until service integrations are implemented. Configure secrets through a managed secret store or local environment variables; never commit them.

## Tests

Install a test runner when test files are added, then run the selected test suite from the repository root. No production integrations or test data are bundled in this scaffold.
