import pytest
import uuid
from fancy_todo_list.application.usecases import CreateUser, CreateUserRequest
from fancy_todo_list.adapters.database.sqlite import SQLiteUserRepository, create_database

@pytest.fixture
def user_repository():
    create_database()
    return SQLiteUserRepository()


@pytest.fixture
def create_user_uc(user_repository):
    return CreateUser(user_repository)


class TestCreateUser:
    def test_should_create(self, create_user_uc):
        request = CreateUserRequest(username="usr1")
        response = create_user_uc.execute(request)

        assert response.ref_id is not None

        print("ref ID:", response.ref_id)
        assert isinstance(uuid.UUID(response.ref_id, version=4), uuid.UUID)
