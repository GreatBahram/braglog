import pytest


# @pytest.fixture
# def user_path(tmpdir):
#     dir = tmpdir / "logit"
#     dir.mkdir()
#     return dir


# @pytest.fixture
# def logs_db(user_path):
#     return sqlite_utils.Database(str(user_path / "logs.db"))

from peewee import SqliteDatabase
from logit import models


@pytest.fixture
def db():
    test_db = SqliteDatabase(":memory:")
    with test_db.bind_ctx(models.tables):
        test_db.create_tables(models.tables)
        yield db
        test_db.drop_tables(models.tables)
        test_db.close()
