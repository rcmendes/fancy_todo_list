import pytest
import uuid
from fancy_todo_list.application.entities import RefId, Username, User
from fancy_todo_list.application.usecases import (
    FindUserByRefId,
    FindUserByRefIdRequest,
)
from fancy_todo_list.adapters.database.sqlite import SQLiteUserRepository


@pytest.fixture
def user_repository():
    return SQLiteUserRepository()


@pytest.fixture
def find_user_by_ref_id_uc(user_repository):
    return FindUserByRefId(user_repository)

@pytest.fixture
def user():
    ref_id = RefId.new()
    username = Username.create("user")
    return User(ref_id, username)

class TestFindUserByRefId:
    def test_should_find(self, find_user_by_ref_id_uc, user_repository, user):
        user_repository.insert(user)
        
        request = FindUserByRefIdRequest(str(user.ref_id))
        response = find_user_by_ref_id_uc.execute(request)

        assert response.ref_id == str(user.ref_id)
        assert response.username == user.username.value
