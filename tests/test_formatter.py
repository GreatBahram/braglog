from braglog import formatter
from dataclasses import dataclass
from datetime import date


@dataclass
class _LogEntry:
    log_date: date
    message: str


def test_basic_formatter():
    log_date = date(2025, 5, 14)
    entries = [
        _LogEntry(message=f"Message {idx}", log_date=log_date) for idx in range(1, 5)
    ]

    formatter_resp = formatter.BasicFormatter(entries=entries)
    assert str(formatter_resp).splitlines() == [
        "2025-05-14: Message 1",
        "2025-05-14: Message 2",
        "2025-05-14: Message 3",
        "2025-05-14: Message 4",
    ]


def test_basic_formatter_no_entries():
    formatter_resp = formatter.BasicFormatter(entries=[])
    assert str(formatter_resp) == ""
