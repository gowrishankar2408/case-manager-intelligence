from src.services.case_service import CaseService

_case_service = CaseService()


def get_case_notes(case_id: str) -> list[str]:
    """Get notes for a sample case by its case ID."""
    return _case_service.get_case_notes(case_id)
