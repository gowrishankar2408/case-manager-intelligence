# Security

CMI may process confidential customer and operational records. Treat all live case content as sensitive unless the data owner classifies it otherwise.

- Apply least privilege and verify user authorization for every case lookup and retrieval request.
- Do not treat model instructions or agent prompts as an authorization boundary.
- Minimize fields sent to embedding, model, logging, and analytics systems; redact where feasible.
- Protect secrets with an approved secret manager. Never place tokens or credentials in source control, prompts, or logs.
- Encrypt data in transit and at rest, including backups and vector indexes.
- Apply retention and deletion requirements to raw records, derived chunks, embeddings, caches, and backups.
- Audit access and administrative actions while avoiding unnecessary sensitive payloads in audit records.
- Test prompt injection, cross-case retrieval leakage, attachment handling, and unsafe tool invocation.
- Use synthetic or approved de-identified data for development and tests.

Complete a threat model and privacy/security review before connecting production data.
