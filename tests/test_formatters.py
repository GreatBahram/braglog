from braglog.formatters import BasicFormatter
from dataclasses import dataclass
from datetime import date
from textwrap import dedent


@dataclass
class _LogEntry:
    log_date: date
    message: str


def test_basic_formatter():
    log_date = date(2025, 5, 14)
    entries = [
        _LogEntry(message=f"Message {idx}", log_date=log_date) for idx in range(1, 5)
    ]

    formatter_resp = BasicFormatter(entries=entries)
    assert str(formatter_resp).splitlines() == [
        "2025-05-14: Message 1",
        "2025-05-14: Message 2",
        "2025-05-14: Message 3",
        "2025-05-14: Message 4",
    ]


def test_basic_formatter_no_entries():
    formatter_resp = BasicFormatter(entries=[])
    assert str(formatter_resp) == ""


# def test_html_formatter_no_entries():
#     formatter_resp = HTMLFormatter(entries=[])
#     expected = dedent("""\
#         <html>
#             <body>
#             </body>
#         </html>""")
#     assert str(formatter_resp) == expected


# def test_html_formatter_one_day_multiple_achievements():
#     log_date = date(2025, 5, 14)
#     entries = [
#         _LogEntry(message=f"Message {idx}", log_date=log_date) for idx in range(1, 5)
#     ]

#     formatter_resp = HTMLFormatter(entries=entries)

#     expected = dedent("""\
#         <html>
#             <ul>
#                 <li><a href="#2025-05-14">2025-05-14</a></li>
#             </ul>

#             <section id="2025-05-14">
#                 <h2>2025-05-14</h2>
#                 <ul>
#                     <li>Message 1</li>
#                     <li>Message 2</li>
#                     <li>Message 3</li>
#                     <li>Message 4</li>
#                 </ul>
#             </section>
#         </html>
#     """)
#     assert str(formatter_resp) == expected
