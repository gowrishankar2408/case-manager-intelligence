$ErrorActionPreference = 'Stop'

$serverPath = Join-Path $PSScriptRoot '..\mcp-server\src\server.py'
$requirementsPath = Join-Path $PSScriptRoot '..\mcp-server\requirements.txt'

if (-not (Test-Path $requirementsPath)) {
    throw "MCP requirements file not found: $requirementsPath"
}

if (-not (Get-Command py -ErrorAction SilentlyContinue)) {
    throw 'Python launcher (py) was not found. Install Python 3.11 or later.'
}

py -m pip install -r $requirementsPath
Push-Location (Split-Path $serverPath)
try {
    py server.py
}
finally {
    Pop-Location
}
