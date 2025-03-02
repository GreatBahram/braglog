import click
from datetime import datetime
from click_default_group import DefaultGroup


@click.group(
    cls=DefaultGroup,
    default="add",
    default_if_no_args=True,
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
    "--date", "-d", default=datetime.today(), help="Specify the date for the log entry."
)
@click.option("--title", "-t", default="", help="Specify the date for the log entry.")
def add(message: str, date):
    message = " ".join(message)
    click.echo(date)
    click.echo(message)
    click.echo("Hello")


@cli.command()
@click.option(
    "--since",
    "-s",
    default=datetime.today(),
    help="Specify the date for the log entry.",
)
@click.option(
    "--until",
    "-u",
    default=datetime.today(),
    help="Specify the date for the log entry.",
)
def show():
    click.echo("Hello")
