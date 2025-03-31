import os
import pathlib

from click.testing import CliRunner

from braglog import models
from braglog.cli import cli


def test_change_config_dir(tmp_path: pathlib.Path):
    runner = CliRunner()

    os.environ["BRAGLOG_CONFIG_DIR"] = str(tmp_path)

    models.ensure_db()

    result = runner.invoke(cli, ["show"])

    assert result.exit_code == 0

    files = [entry.name for entry in tmp_path.iterdir()]
    assert len(files) == 1
    assert "database.db" in files
