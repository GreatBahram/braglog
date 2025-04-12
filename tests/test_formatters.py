import json
from dataclasses import dataclass
from datetime import date
from textwrap import dedent

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


def test_json_formatter_no_entries():
    formatter_resp = formatters.JSONFormatter(entries=[])
    expected = dedent("""\
        {
          "count": 0,
          "entries": []
        }""")
    assert str(formatter_resp) == expected


def test_json_formatter_one_day_multiple_achievements():
    entries = [
        _LogEntry(message="Message 1", log_date=date.today()),
        _LogEntry(message="Message 2", log_date=date.today()),
    ]
    expected = {
        "count": len(entries),
        "entries": [
            {"message": "Message 1", "date": date.today().strftime("%Y-%m-%d")},
            {"message": "Message 2", "date": date.today().strftime("%Y-%m-%d")},
        ],
    }
    formatter_resp = formatters.JSONFormatter(entries=entries)

    assert json.loads(str(formatter_resp)) == expected


def test_foldable_html_formatter_no_entries():
    formatter_resp = formatters.FodableHTMLFormatter(entries=[])
    expected = formatters.foldable_html.TEMPLATE_HTML.format(
        style=formatters.foldable_html.STYLE,
        content="",
        script=formatters.foldable_html.SCRIPT,
    )
    assert str(formatter_resp) == expected


def test_foldable_html_formatter_one_day_multiple_achievements():
    entries = [
        _LogEntry(message=f"Message {idx}", log_date=date.today())
        for idx in range(1, 5)
    ]

    formatter_resp = formatters.FodableHTMLFormatter(entries=entries)

    assert str(formatter_resp).count("Message") == len(entries)


def test_markdown_formatter_no_entries():
    formatter_resp = formatters.MarkdownFormatter(entries=[])
    expected = formatters.MarkdownFormatter.footer
    assert str(formatter_resp) == expected


def test_markdown_formatter_one_day_multiple_achievements():
    entries = [
        _LogEntry(message=f"Message {idx}", log_date=date.today())
        for idx in range(1, 5)
    ]
    expected = [
        f"# {date.today().year}",
        f"## {date.today().strftime('%B')}",
        f"- {date.today().strftime('%Y-%m-%d')}",
        "    - Message 1",
        "    - Message 2",
        "    - Message 3",
        "    - Message 4" + formatters.MarkdownFormatter.footer,
    ]
    formatter_resp = str(formatters.MarkdownFormatter(entries=entries))

    assert formatter_resp == "\n".join(expected)
