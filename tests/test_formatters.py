from dataclasses import dataclass
from datetime import date

from braglog import formatters


@dataclass
class _LogEntry:
    log_date: date
    message: str


def test_basic_formatter():
    log_date = date(2025, 5, 14)
    entries = [
        _LogEntry(message=f"Message {idx}", log_date=log_date) for idx in range(1, 5)
    ]

    formatter_resp = formatters.BasicFormatter(entries=entries)
    assert str(formatter_resp).splitlines() == [
        "2025-05-14: Message 1",
        "2025-05-14: Message 2",
        "2025-05-14: Message 3",
        "2025-05-14: Message 4",
    ]


def test_basic_formatter_no_entries():
    formatter_resp = formatters.BasicFormatter(entries=[])
    assert str(formatter_resp) == ""


def test_html_formatter_no_entries():
    formatter_resp = formatters.HTMLFormatter(entries=[])
    expected = formatters.html.TEMPLATE_HTML.format(
        style=formatters.html.STYLE, navigation="", content=""
    )
    assert str(formatter_resp) == expected


def test_html_formatter_one_day_multiple_achievements():
    entries = [
        _LogEntry(message=f"Message {idx}", log_date=date.today())
        for idx in range(1, 5)
    ]

    formatter_resp = formatters.HTMLFormatter(entries=entries)

    assert str(formatter_resp).count("Message") == len(entries)
