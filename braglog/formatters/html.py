from collections import defaultdict
from typing import Iterable

from ..models import LogEntry

TEMPLATE_HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brag Log</title>
    {style}
</head>
<body>
    {navigation}
    {content}
</body>
</html>"""

TEMPLATE_SECTION = """\
<section id="{date}">
    <h2>{date}</h2>
    <ul>
    {achievements_list}
    </ul>
</section>"""


TEMPLATE_NAV = """\
<nav>
    <ul>
    {nav_items}
    </ul>
</nav>"""

STYLE = """\
    <style>
        :root {
            --primary-color: #0366d6;
            --bg-color: #f6f8fa;
            --text-color: #24292e;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            max-width: 800px;
            margin: 2rem auto;
            padding: 0 1rem;
            background: var(--bg-color);
        }
        nav {
            position: sticky;
            top: 0;
            background: white;
            padding: 1rem;
            border-radius: 6px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.12);
            margin-bottom: 2rem;
        }
        nav ul {
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        nav a {
            color: var(--primary-color);
            text-decoration: none;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            background: #f1f8ff;
            transition: background 0.2s;
        }
        nav a:hover {
            background: #dbedff;
        }
        section {
            background: white;
            padding: 1.5rem;
            border-radius: 6px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.12);
            margin-bottom: 1.5rem;
        }
        h2 {
            margin-top: 0;
            color: var(--text-color);
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.5rem;
        }
        ul {
            padding-left: 1.5rem;
            margin: 1rem 0;
        }
        li {
            margin: 0.5rem 0;
        }
    </style>
"""


class HTMLFormatter:
    log_format = "%Y-%m-%d"

    def __init__(self, entries: Iterable[LogEntry]):
        self.entries = entries

    def _get_entries_by_date(self) -> dict[str, list[str]]:
        entries_by_date = defaultdict(list)
        for entry in self.entries:
            date_str = entry.log_date.strftime(self.log_format)
            entries_by_date[date_str].append(entry.message)
        return entries_by_date

    def _render_section(self, date: str, messages: list[str]) -> str:
        achievements_list = "\n".join(f"<li>{msg}</li>" for msg in messages)
        return TEMPLATE_SECTION.format(date=date, achievements_list=achievements_list)

    def _render_navigation(self, dates: list[str]) -> str:
        nav_items = [f'<li><a href="#{date}">{date}</a></li>' for date in sorted(dates)]
        return TEMPLATE_NAV.format(nav_items="\n".join(nav_items))

    def __str__(self) -> str:
        entries_by_date = self._get_entries_by_date()

        navigation = self._render_navigation(list(entries_by_date.keys()))

        sections = [
            self._render_section(date, messages)
            for date, messages in sorted(entries_by_date.items())
        ]

        return TEMPLATE_HTML.format(
            style=STYLE, navigation=navigation, content="\n".join(sections)
        )
