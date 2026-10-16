def build_timeline(
    case_record: dict[str, object],
    activities: list[dict[str, object]],
    notes: list[dict[str, object]],
) -> list[dict[str, object]]:
    """Build a normalized, source-linked timeline for a case."""
    raise NotImplementedError("Define the normalized case and event contracts first.")
