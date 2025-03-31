import os
import pathlib
from datetime import date

import click
from peewee import DateField, Model, SqliteDatabase, TextField

BRAGLOG_CONFIG_ENV_VAR = "BRAGLOG_CONFIG_DIR"


def user_dir() -> pathlib.Path:
    app_dir = pathlib.Path(
        os.environ.get(BRAGLOG_CONFIG_ENV_VAR) or click.get_app_dir("braglog")
    )
    app_dir.mkdir(exist_ok=True, parents=True)
    return app_dir


def db_path() -> pathlib.Path:
    return user_dir() / "database.db"


def get_database() -> SqliteDatabase:
    return SqliteDatabase(db_path())


class LogEntry(Model):
    log_date = DateField(default=date.today)
    message = TextField()

    class Meta:
        database = get_database()


tables = [
    LogEntry,
]


def ensure_db() -> None:
    db = get_database()

    with db:
        db.create_tables(tables)
