from src.services.case_service import CaseService

_case_service = CaseService()


def explain_case_closure(case_id: str) -> dict[str, object]:
    """Explain the recorded closure status and return supporting case evidence."""
    return _case_service.explain_case_closure(case_id)
