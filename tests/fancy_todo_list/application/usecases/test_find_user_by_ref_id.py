import pytest
import uuid
from fancy_todo_list.application.entities import RefId, Username, User
from fancy_todo_list.application.usecases import (
    FindUserByRefIdRequest,
)

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

    @pytest.mark.parametrize("username", [f"user{i}" for i in range(1,11)])
    def te_should_create_and_find_10(self, find_user_by_ref_id_uc, user_repository, username):
        request = CreateUserRequest(username=username)
        response = create_user_uc.execute(request)

        assert response.ref_id is not None

        assert isinstance(uuid.UUID(response.ref_id, version=4), uuid.UUID)