# RAG Service

Owns knowledge ingestion, normalization, chunking, embedding, access-aware retrieval, and vector-store integration. Every indexed unit must retain source and authorization metadata so retrieval can be filtered for the requesting user.

No embedding provider or vector-store client is selected in this scaffold. Choose them only after reviewing data residency, retention, access filtering, quality, and cost requirements.
