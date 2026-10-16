import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from src.services.case_service import CaseService

service = CaseService()

print(service.get_case_details("CMI-1001"))