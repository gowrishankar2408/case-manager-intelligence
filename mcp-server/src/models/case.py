from dataclasses import asdict, dataclass


@dataclass(slots=True)
class Case:
    case_id: str
    title: str
    status: str
    priority: str
    description: str
    created_at: str
    updated_at: str
    notes: list[str]
    activities: list[dict[str, str]]
    closure_reason: str | None = None

    @classmethod
    def from_dict(cls, data: dict[str, object]) -> "Case":
        return cls(
            case_id=str(data["case_id"]),
            title=str(data["title"]),
            status=str(data["status"]),
            priority=str(data["priority"]),
            description=str(data["description"]),
            created_at=str(data["created_at"]),
            updated_at=str(data["updated_at"]),
            notes=[str(note) for note in data.get("notes", [])],
            activities=[
                {str(key): str(value) for key, value in activity.items()}
                for activity in data.get("activities", [])
            ],
            closure_reason=(
                str(data["closure_reason"])
                if data.get("closure_reason") is not None
                else None
            ),
        )

    def to_dict(self) -> dict[str, object]:
        return asdict(self)
