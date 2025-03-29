import json

from ..models import LogEntry


class JSONFormatter:
    log_format = "%Y-%m-%d"

    def __init__(self, entries: list[LogEntry]) -> None:
        self.entries = entries

    def __str__(self) -> str:
        obj = {
            "count": len(self.entries),
            "entries": [
                {
                    "message": entry.message,
                    "date": entry.log_date.strftime(self.log_format),
                }
                for entry in self.entries
            ],
        }
        return json.dumps(obj, indent=2)
