<<<<<<< HEAD
from src.services.case_service import CaseService

_case_service = CaseService()


def get_case_details(case_id: str) -> dict[str, object]:
    """Get details for a sample case by its case ID."""
    return _case_service.get_case_details(case_id)
=======
def get_case_details(case_id: str) -> dict[str, object]:
    """Return the authorized details for a case."""
    raise NotImplementedError("Connect this tool to the approved Case Manager API.")
>>>>>>> c0e1a89e4037a27593ef36b0736587fd7459782d
