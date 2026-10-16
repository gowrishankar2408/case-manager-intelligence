def rank_evidence(
    evidence: list[dict[str, object]],
    query: str,
) -> list[dict[str, object]]:
    """Rank evidence for relevance while preserving provenance."""
    raise NotImplementedError("Define evidence features and ranking evaluation criteria first.")
