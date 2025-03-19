import pytest


from peewee import SqliteDatabase
from braglog import models


@pytest.fixture
def db():
    test_db = SqliteDatabase(":memory:")
    with test_db.bind_ctx(models.tables):
        test_db.create_tables(models.tables)
        yield db
        test_db.drop_tables(models.tables)
        test_db.close()
