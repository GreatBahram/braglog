import click
from datetime import datetime, date
from click_default_group import DefaultGroup
import dateparser
from braglog.models import ensure_db, db_path, LogEntry


@click.group(
    cls=DefaultGroup,
    default="add",
    default_if_no_args=False,
)
@click.version_option()
def cli():
    """
    Easily log and manage daily work achievements to boost transparency and productivity.
    """
    pass


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
def add(message: str, date: datetime):
    ensure_db()
    message = " ".join(message)

    log_entry = LogEntry(message=message, log_date=date.date())
    log_entry.save()


@cli.command()
def logs_path():
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
def show(
    text: str | None,
    on: date | None,
    since: date | None,
    until: date | None,
    delete: bool = False,
):
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

    delete_count = 0

    for entry in entries.order_by(LogEntry.log_date.asc()):
        if not delete:
            click.echo(f"{entry.log_date.strftime('%Y-%m-%d')}: {entry.message}")
        else:
            preview = entry.message[:40] if len(entry.message) > 40 else entry.message
            msg = f"Delete {preview!r}, are you sure?"

            if click.confirm(msg, default=False):
                entry.delete_instance()
                delete_count += 1

    if delete:
        click.echo(f"Deleted {delete_count} record{'' if delete_count == 1 else 's'}!")
