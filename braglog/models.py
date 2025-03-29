import pathlib
from datetime import date

import click
from peewee import DateField, Model, SqliteDatabase, TextField


def user_dir() -> pathlib.Path:
    app_dir = pathlib.Path(click.get_app_dir("braglog"))
    app_dir.mkdir(exist_ok=True, parents=True)
    return app_dir


def db_path() -> pathlib.Path:
    return user_dir() / "database.db"


db = SqliteDatabase(db_path())


class LogEntry(Model):
    log_date = DateField(default=date.today)
    message = TextField()

    class Meta:
        database = db


tables = [
    LogEntry,
]


def ensure_db() -> None:
    with db:
        db.create_tables(tables)
