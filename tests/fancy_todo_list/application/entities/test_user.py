import pytest
import uuid
from fancy_todo_list.application.entities import user, base
from fancy_todo_list.application.entities.errors import InvalidUsernameError


class TestUsername:
    def test_should_create(self):
        username = "1234"
        instance = user.Username.create(username)
        assert isinstance(instance, user.Username)
        assert instance.value == username

        username = "12345678901234567890"
        instance = user.Username.create(username)
        assert isinstance(instance, user.Username)
        assert instance.value == username

    def test_should_not_create(self):
        username = "123"
        with pytest.raises(InvalidUsernameError):
            user.Username.create(username)

        username = "123456789012345678901"
        with pytest.raises(InvalidUsernameError):
            user.Username.create(username)

        username = ""
        with pytest.raises(InvalidUsernameError):
            user.Username.create(username)

        username = None
        with pytest.raises(InvalidUsernameError):
            user.Username.create(username)

    def test_should_not_create_from_constructor(self):
        username = "1234"
        with pytest.raises(AssertionError):
            user.Username(username, None)

        with pytest.raises(AssertionError):
            user.Username(username, object())


class TestUser:
    def test_should_create(self):
        ref_id = base.RefId.create(uuid.uuid4())
        username = user.Username.create("1234")
        instance = user.User(ref_id, username)
        assert isinstance(instance, user.User)
        assert instance.ref_id == ref_id
        assert instance.username == username

    def test_should_not_create(self):
        ref_id = base.RefId.create(uuid.uuid4())
        username = None
        with pytest.raises(AssertionError):
            user.User(ref_id, username)

        ref_id = None
        username = user.Username.create("1234")
        with pytest.raises(AssertionError):
            user.User(ref_id, username)

        ref_id = "123"
        username = user.Username.create("1234")
        with pytest.raises(AssertionError):
            user.User(ref_id, username)

        ref_id = base.RefId.create(uuid.uuid4())
        username = "1234"
        with pytest.raises(AssertionError):
            user.User(ref_id, username)
