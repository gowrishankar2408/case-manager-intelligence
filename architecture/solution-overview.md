# Solution Overview

## Purpose

CMI combines case-system data, retrieval-augmented generation (RAG), and a reasoning layer to help authorized case managers understand case history, locate comparable cases, and review evidence behind a closure explanation.

## Logical Flow

1. The extraction service obtains approved case records and attachments through the Case Manager API.
2. The knowledge repository stores controlled raw, processed, and metadata artifacts.
3. The RAG service normalizes, chunks, embeds, indexes, and retrieves approved content.
4. The reasoning engine builds case timelines, ranks evidence, and computes confidence.
5. The MCP server exposes case tools to an approved Copilot agent.
6. The agent presents sourced explanations to the user; case-system actions remain out of scope until explicitly designed and governed.

## Trust Boundaries

Case data and identity tokens are sensitive. Authenticate every user and service, authorize access at the case level, minimize retrieved fields, and preserve source references in generated answers. See [security](../docs/security.md) and [governance](../docs/governance.md).

## Diagram Sources

Editable Mermaid sources are in `diagrams/`. Render them to PNG during documentation publishing when Mermaid CLI is available.

## Open Design Items

- Select the system-of-record API and document its pagination, rate limits, and access model.
- Define data classifications, retention periods, and deletion propagation.
- Select the embedding model and vector store deployment mode.
- Establish evaluation metrics for retrieval quality, groundedness, and closure-analysis accuracy.
