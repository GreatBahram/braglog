from datetime import date, datetime

import click
import dateparser
from click_default_group import DefaultGroup

from braglog import formatters
from braglog.models import LogEntry, db_path, ensure_db


@click.group(
    cls=DefaultGroup,
    default="add",
    default_if_no_args=False,
)
@click.version_option()
def cli() -> None:
    """
    Easily log and manage daily work achievements to
    boost transparency and productivity.
    """


@cli.command()
@click.argument(
    "message",
    nargs=-1,
    type=click.STRING,
    required=True,
)
@click.option(
    "--date",
    "-d",
    type=click.DateTime(formats=["%Y-%m-%d", "%Y/%m/%d"]),
    default=datetime.today(),
    help="Specify the date for the log entry.",
)
def add(message: str, date: datetime) -> None:
    ensure_db()
    message = " ".join(message)

    log_entry = LogEntry(message=message, log_date=date.date())
    log_entry.save()


@cli.command()
def logs_path() -> None:
    click.echo(db_path())


def parse_date(
    ctx: click.Context, param: click.Parameter, value: str | None
) -> date | None:
    if not value:
        return None

    parsed = dateparser.parse(value)

    if parsed is None:
        raise click.BadParameter(f"Cannot parse the date: {value}")

    return parsed.date()


@cli.command()
@click.option(
    "--contains",
    "-c",
    "text",
    required=False,
    help="Entries containing specific text.",
)
@click.option(
    "--on",
    callback=parse_date,
    required=False,
    help="Entries with a speicific date.",
)
@click.option(
    "--since",
    "-s",
    callback=parse_date,
    required=False,
    help="Entries since a speicific date.",
)
@click.option(
    "--until",
    "-u",
    callback=parse_date,
    required=False,
    help="Entries until a speicific date.",
)
@click.option(
    "--delete",
    "-d",
    is_flag=True,
    default=False,
    help="Delete filtered records.",
)
@click.option(
    "--number",
    "-n",
    "count",
    type=int,
    default=False,
    help="print the first n records.",
)
@click.option(
    "--reverse",
    "-r",
    is_flag=True,
    default=False,
    help="Reverse the order of the displayed records.",
)
@click.option(
    "--format",
    "-f",
    default="basic",
    type=click.Choice(formatters.FORMATTER_MAP.keys(), case_sensitive=False),
    show_default=True,
    help="Specify the output format for displaying the records.",
)
@click.option(
    "--edit",
    "-e",
    is_flag=True,
    help="Edit the filtered records interactively.",
)
def show(  # noqa: PLR0913,PLR0912
    text: str | None,
    on: date | None,
    since: date | None,
    until: date | None,
    delete: bool = False,
    count: int | None = None,
    reverse: bool = False,
    format: str = "basic",
    edit: bool = False,
) -> None:
    ensure_db()

    entries = LogEntry.select()

    if on and (since or until):
        raise click.BadArgumentUsage("--on not allowed with --since|--until")

    if text:
        entries = entries.where(LogEntry.message.contains(text))
    if on:
        entries = entries.where(LogEntry.log_date == on)
    if since:
        entries = entries.where(LogEntry.log_date >= since)
    if until:
        entries = entries.where(LogEntry.log_date <= until)
    if count:
        entries = entries.limit(value=count)

    order = LogEntry.log_date.desc() if reverse else LogEntry.log_date.asc()
    entries = entries.order_by(order) if entries else entries
    if edit:
        for entry in entries:
            message = click.edit(entry.message)
            if message is not None:
                entry.message = message.rstrip("\n")
                entry.save()
    if not delete:
        fromatter = formatters.FORMATTER_MAP[format]
        formatted_resp = str(fromatter(entries=entries))
        click.echo(formatted_resp, nl=False)
    else:
        delete_count = 0
        for entry in entries:
            preview = entry.message[:40] if len(entry.message) > 40 else entry.message  # noqa: PLR2004
            msg = f"Delete {preview!r}, are you sure?"

            if click.confirm(msg, default=False):
                entry.delete_instance()
                delete_count += 1

        click.echo(f"Deleted {delete_count} record{'' if delete_count == 1 else 's'}!")
