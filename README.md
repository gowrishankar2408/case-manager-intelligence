# Case Manager Intelligence

Case Manager Intelligence (CMI) is an enterprise AI platform leveraging Copilot Studio, MCP, RAG, and Case Manager APIs to provide explainable case intelligence and actionable insights.

## Repository Layout

- `architecture/`: solution design, use cases, decision records, and diagram sources.
- `case-manager-api/`: integration boundary for the case-management system.
- `copilot-agent/`: agent instructions, prompts, tools, and export artifacts.
- `docs/`: installation, deployment, security, governance, and roadmap guidance.
- `extraction-service/` and `knowledge-repository/`: source-data extraction and staged knowledge artifacts.
- `mcp-server/`: MCP interface for case intelligence tools.
- `rag-service/` and `reasoning-engine/`: retrieval and explainable case analysis components.
- `tests/`: unit, integration, MCP, and RAG test suites.
- `vector-db/`: local vector database data and maintenance scripts.

## Getting Started

The MCP server is the first runnable scaffold. See [mcp-server/README.md](mcp-server/README.md) and [docs/installation.md](docs/installation.md). Tool implementations intentionally raise `NotImplementedError` until an approved Case Manager API and data contract are configured.

## Data and Security

Do not commit customer or production case data, credentials, tokens, or locally generated vector indexes. Use synthetic data in `knowledge-repository/samples/`. Review [docs/security.md](docs/security.md) and [docs/governance.md](docs/governance.md) before connecting live systems.

## Project Status

This repository is a starter scaffold, not a production-ready service. Integration contracts, identity and access controls, retention rules, deployment infrastructure, and evaluation datasets must be completed before production use.

## License

License terms have not yet been selected. See [LICENSE](LICENSE).
