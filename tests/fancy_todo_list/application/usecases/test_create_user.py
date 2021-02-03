import pytest
import uuid
from fancy_todo_list.application.usecases import CreateUserRequest


class TestCreateUser:
    def test_should_create(self, create_user_uc):
        request = CreateUserRequest(username="usr1")
        response = create_user_uc.execute(request)

        assert response.ref_id is not None

        assert isinstance(uuid.UUID(response.ref_id, version=4), uuid.UUID)
