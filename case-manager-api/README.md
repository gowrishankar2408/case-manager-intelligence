# Case Manager API Adapter

Owns the authenticated client and normalized contracts for the system of record. Keep vendor-specific transport and payload details inside `src/clients/`; expose authorized operations through `src/services/` and `src/endpoints/`.

Define pagination, rate-limit handling, retry behavior, permission checks, attachment limits, and error mapping before implementation. Do not store production credentials in this package.
