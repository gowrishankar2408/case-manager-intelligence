<<<<<<< HEAD
from src.services.case_service import CaseService

_case_service = CaseService()


def get_case_notes(case_id: str) -> list[str]:
    """Get notes for a sample case by its case ID."""
    return _case_service.get_case_notes(case_id)
=======
def get_case_notes(case_id: str) -> list[dict[str, object]]:
    """Return notes visible to the requesting user for a case."""
    raise NotImplementedError("Connect this tool to the approved Case Manager API.")
>>>>>>> c0e1a89e4037a27593ef36b0736587fd7459782d
