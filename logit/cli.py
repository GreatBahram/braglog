import click
from datetime import datetime
from click_default_group import DefaultGroup


@click.group(
    cls=DefaultGroup,
    default="add",
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
    required=True,
)
# @click.option(
#     "--date", "-d", default=datetime.today(), help="Specify the date for the log entry."
# )
# @click.option("--title", "-t", default="", help="Specify the date for the log entry.")
def add(message: str):
    print(message)
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
