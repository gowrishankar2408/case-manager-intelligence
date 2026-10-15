# Deployment

This scaffold does not define a production deployment target. Before deployment, choose the hosting platform and document network boundaries, identity integration, secrets management, scaling, health checks, and rollback procedures.

Deployment checklist:

- Use separate development, test, and production environments.
- Keep the MCP endpoint private to trusted clients and require authenticated transport appropriate to the host.
- Enforce case-level authorization in the trusted API/service layer, not only in prompts.
- Store credentials in a managed secret store and rotate them on a defined schedule.
- Set resource, timeout, and rate limits for API calls and model requests.
- Define logging, monitoring, alerting, retention, and incident response.
- Validate RAG quality and closure-analysis behavior against an approved, de-identified evaluation set before release.
