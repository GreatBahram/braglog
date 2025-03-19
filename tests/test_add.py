from datetime import date
from click.testing import CliRunner

from braglog.cli import cli
from braglog import models


def test_version():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert result.output.startswith("cli, version ")


def test_add(db):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["life is good"])

        assert result.exit_code == 0

        entries = models.LogEntry.select()
        assert len(entries) == 1

        log_entry = entries.first()
        assert (log_entry.message, log_entry.log_date) == ("life is good", date.today())


def test_add_with_date(db):
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["life is good", "-d", "2024-05-13"])

        assert result.exit_code == 0

        entries = models.LogEntry.select()
        assert len(entries) == 1

        log_entry = entries.first()
        assert (log_entry.message, log_entry.log_date) == (
            "life is good",
            date(year=2024, month=5, day=13),
        )


def test_add_without_options_print_help_message(db):
    runner = CliRunner()
    with runner.isolated_filesystem():
        default_command_result = runner.invoke(cli, [])
        help_command_result = runner.invoke(cli, ["--help"])

        assert default_command_result.exit_code == 0
        assert help_command_result.exit_code == 0

        assert default_command_result.output == help_command_result.output
