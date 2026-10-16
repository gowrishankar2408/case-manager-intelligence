<<<<<<< HEAD
from src.services.case_service import CaseService

_case_service = CaseService()


def explain_case_closure(case_id: str) -> dict[str, object]:
    """Explain the recorded closure status and return supporting case evidence."""
    return _case_service.explain_case_closure(case_id)
=======
def explain_case_closure(case_id: str) -> dict[str, object]:
    """Explain a case closure with supporting evidence and calibrated confidence."""
    raise NotImplementedError("Connect this tool to the approved reasoning service.")
>>>>>>> c0e1a89e4037a27593ef36b0736587fd7459782d
