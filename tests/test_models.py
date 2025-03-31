import os
import pathlib

from braglog import models


def test_change_config_dir(tmp_path: pathlib.Path):
    os.environ["BRAGLOG_CONFIG_DIR"] = str(tmp_path)

    models.ensure_db()

    assert (tmp_path / "database.db").exists()
