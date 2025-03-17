import click
from datetime import datetime
from click_default_group import DefaultGroup

from logit.models import ensure_db, db_path, LogEntry


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
