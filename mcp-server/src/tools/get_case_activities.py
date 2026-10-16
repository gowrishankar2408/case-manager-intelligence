from src.services.case_service import CaseService

_case_service = CaseService()


def get_case_activities(case_id: str) -> list[dict[str, str]]:
    """Get activities for a sample case by its case ID."""
    return _case_service.get_case_activities(case_id)
