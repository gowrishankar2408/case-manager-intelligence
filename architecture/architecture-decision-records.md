# Architecture Decision Records

Record decisions here using the format: **Status**, **Context**, **Decision**, and **Consequences**. Keep superseded decisions for traceability.

## ADR-001: Separate Retrieval from Case Reasoning

- **Status:** Proposed
- **Context:** Case similarity and closure explanations need searchable evidence and deterministic timeline/ranking logic.
- **Decision:** Keep RAG retrieval and reasoning-engine responsibilities as separate modules with explicit data contracts.
- **Consequences:** Components can be evaluated independently; integration schemas and provenance must be maintained between them.

## ADR-002: Expose Agent Capabilities through MCP

- **Status:** Proposed
- **Context:** Copilot-facing case tools need a stable boundary independent of the agent authoring surface.
- **Decision:** Use an MCP server as the tool boundary, with authorization enforced by trusted services and the underlying case system.
- **Consequences:** Tool schemas require versioning, authentication, authorization, and audit design before production deployment.
