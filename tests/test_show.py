from datetime import date, timedelta
from click.testing import CliRunner

from braglog.cli import cli
from braglog import models


def test_show(db):
    runner = CliRunner()
    with runner.isolated_filesystem():
        log_date = date(year=2024, month=5, day=12)

        instances = [
            models.LogEntry(message="Task 1", log_date=log_date),
            models.LogEntry(message="Task 2", log_date=log_date),
            models.LogEntry(message="Task 3", log_date=log_date),
        ]

        models.LogEntry.bulk_create(instances, batch_size=3)

        expected_output = [
            "2024-05-12: Task 1",
            "2024-05-12: Task 2",
            "2024-05-12: Task 3",
        ]

        result = runner.invoke(cli, ["show"])

        assert result.exit_code == 0
        assert result.output == "\n".join(expected_output) + "\n"


def test_show_contains(db):
    runner = CliRunner()
    with runner.isolated_filesystem():
        log_date = date(year=2024, month=5, day=12)

        instances = [
            models.LogEntry(message="Bug fix in the authentication", log_date=log_date),
            models.LogEntry(message="Develop a fantastic feature", log_date=log_date),
            models.LogEntry(message="another bug fix", log_date=log_date),
        ]

        models.LogEntry.bulk_create(instances, batch_size=3)

        expected_output = [
            "2024-05-12: Bug fix in the authentication",
            "2024-05-12: another bug fix",
        ]

        result = runner.invoke(cli, ["show", "--contains", "fix"])

        assert result.exit_code == 0
        assert result.output == "\n".join(expected_output) + "\n"


def test_show_on_specific_date(db):
    runner = CliRunner()
    with runner.isolated_filesystem():
        instances = [
            models.LogEntry(
                message="Bug fix in the authentication", log_date=date(2024, 3, 12)
            ),
            models.LogEntry(
                message="Develop a fantastic feature", log_date=date(2024, 4, 12)
            ),
            models.LogEntry(message="another bug fix", log_date=date(2024, 5, 14)),
        ]

        models.LogEntry.bulk_create(instances, batch_size=3)

        expected_output = ["2024-05-14: another bug fix"]

        result = runner.invoke(cli, ["show", "--on", "2024-05-14"])

        assert result.exit_code == 0
        assert result.output == "\n".join(expected_output) + "\n"


def test_show_on_specific_date_relative(db):
    runner = CliRunner()

    with runner.isolated_filesystem():
        today = date.today()
        yesterday = today - timedelta(days=1)

        instances = [
            models.LogEntry(message="Bug fix in the authentication", log_date=today),
            models.LogEntry(message="another bug fix", log_date=yesterday),
        ]

        models.LogEntry.bulk_create(instances, batch_size=3)

        expected_output = [f"{yesterday.strftime('%Y-%m-%d')}: another bug fix"]

        result = runner.invoke(cli, ["show", "--on", "yesterday"])

        assert result.exit_code == 0
        assert result.output == "\n".join(expected_output) + "\n"


def test_show_since(db):
    runner = CliRunner()

    with runner.isolated_filesystem():
        today = date.today()
        yesterday = today - timedelta(days=1)
        two_days_ago = today - timedelta(days=2)

        instances = [
            models.LogEntry(message="Mentor a new developer", log_date=two_days_ago),
            models.LogEntry(message="another bug fix", log_date=yesterday),
            models.LogEntry(message="Bug fix in the authentication", log_date=today),
        ]

        models.LogEntry.bulk_create(instances, batch_size=3)

        expected_output = [
            f"{yesterday.strftime('%Y-%m-%d')}: another bug fix",
            f"{today.strftime('%Y-%m-%d')}: Bug fix in the authentication",
        ]

        result = runner.invoke(cli, ["show", "--since", "yesterday"])

        assert result.exit_code == 0
        assert result.output == "\n".join(expected_output) + "\n"


def test_show_until(db):
    runner = CliRunner()

    with runner.isolated_filesystem():
        today = date.today()
        yesterday = today - timedelta(days=1)
        two_days_ago = today - timedelta(days=2)

        instances = [
            models.LogEntry(message="Mentor a new developer", log_date=two_days_ago),
            models.LogEntry(message="another bug fix", log_date=yesterday),
            models.LogEntry(message="Bug fix in the authentication", log_date=today),
        ]

        models.LogEntry.bulk_create(instances, batch_size=3)

        expected_output = [
            f"{two_days_ago.strftime('%Y-%m-%d')}: Mentor a new developer",
            f"{yesterday.strftime('%Y-%m-%d')}: another bug fix",
        ]

        result = runner.invoke(cli, ["show", "--until", "yesterday"])

        assert result.exit_code == 0
        assert result.output == "\n".join(expected_output) + "\n"


def test_show_since_until(db):
    runner = CliRunner()

    with runner.isolated_filesystem():
        today = date.today()
        yesterday = today - timedelta(days=1)
        two_days_ago = today - timedelta(days=2)
        three_days_ago = today - timedelta(days=3)

        instances = [
            models.LogEntry(
                message="Give a presentation about TDD", log_date=three_days_ago
            ),
            models.LogEntry(message="Mentor a new developer", log_date=two_days_ago),
            models.LogEntry(message="another bug fix", log_date=yesterday),
            models.LogEntry(message="Bug fix in the authentication", log_date=today),
        ]

        models.LogEntry.bulk_create(instances, batch_size=3)

        expected_output = [
            f"{three_days_ago.strftime('%Y-%m-%d')}: Give a presentation about TDD",
            f"{two_days_ago.strftime('%Y-%m-%d')}: Mentor a new developer",
        ]

        result = runner.invoke(
            cli, ["show", "--since", "3 days ago", "--until", "2 days ago"]
        )

        assert result.exit_code == 0
        assert result.output == "\n".join(expected_output) + "\n"


def test_show_on_since_until_mutually_exclusive(db):
    runner = CliRunner()

    with runner.isolated_filesystem():
        result = runner.invoke(
            cli, ["show", "--on", "3 days ago", "--until", "2 days ago"]
        )
        assert result.exit_code != 0
        assert "not allowed with" in result.output


def test_show_delete_with_no_records(db):
    runner = CliRunner()

    result = runner.invoke(cli, ["show", "--delete"])

    assert result.exit_code == 0
    assert "Deleted 0 records!" in result.output


def test_show_delete_with_one_record(db):
    runner = CliRunner()

    models.LogEntry.create(
        message="Give a presentation about TDD", log_date=date.today()
    )

    result = runner.invoke(cli, ["show", "--delete"], input="y\n")

    assert result.exit_code == 0
    assert "Deleted 1 record!" in result.output
    assert len(models.LogEntry.select()) == 0


def test_show_delete_with_two_record(db):
    runner = CliRunner()

    models.LogEntry.create(message="Message 1", log_date=date.today())  # y
    models.LogEntry.create(message="Message 2", log_date=date.today())  # n

    result = runner.invoke(cli, ["show", "--delete"], input="y\nn\n")

    assert result.exit_code == 0
    assert "Deleted 1 record!" in result.output
    assert models.LogEntry.get().message == "Message 2"
