from src.services.case_service import CaseService

_case_service = CaseService()


def get_case_details(case_id: str) -> dict[str, object]:
    """Get details for a sample case by its case ID."""
    return _case_service.get_case_details(case_id)
