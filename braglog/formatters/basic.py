from ..models import LogEntry


class BasicFormatter:
    log_format = "%Y-%m-%d"

    def __init__(self, entries: list[LogEntry]) -> None:
        self.entries = entries

    def __str__(self) -> str:
        return "\n".join(
            f"{entry.log_date.strftime(self.log_format)}: {entry.message}"
            for entry in self.entries
        )
