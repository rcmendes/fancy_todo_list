import pytest

from fancy_todo_list.application.usecases import (
    CreateUser,
    FindUserByRefId,
)
from fancy_todo_list.adapters.database.sqlite import (
    SQLiteUserRepository,
    create_database,
    drop_database,
)


@pytest.fixture(autouse=True)
def init_database():
    print("creating database")
    create_database()
    yield
    print("dropping database")
    drop_database()


@pytest.fixture
def user_repository():
    return SQLiteUserRepository()


@pytest.fixture
def create_user_uc(user_repository):
    return CreateUser(user_repository)


@pytest.fixture
def find_user_by_ref_id_uc(user_repository):
    return FindUserByRefId(user_repository)