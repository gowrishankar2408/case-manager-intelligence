import json
from pathlib import Path


class CaseService:
    def __init__(self):
        data_file = (
            Path(__file__).parent.parent
            / "data"
            / "sample_cases.json"
        )

        with open(data_file, "r", encoding="utf-8") as f:
            self.cases = json.load(f)

    def get_case_details(self, case_id: str):
        case = self.cases.get(case_id)

        if not case:
            return None

        return {
            "case_id": case_id,
            "status": case.get("status"),
            "summary": case.get("summary")
        }

    def get_case_notes(self, case_id: str):
        case = self.cases.get(case_id)

        if not case:
            return []

        return case.get("notes", [])

    def get_case_activities(self, case_id: str):
        case = self.cases.get(case_id)

        if not case:
            return []

        return case.get("activities", [])

    def explain_case_closure(self, case_id: str):
        case = self.cases.get(case_id)

        if not case:
            return {
                "case_id": case_id,
                "reason": "Case not found",
                "confidence": "Low",
                "evidence": []
            }

        return {
            "case_id": case_id,
            "reason": case.get("summary"),
            "confidence": "High",
            "evidence": [
                "Case Notes",
                "Activity History"
            ]
        }