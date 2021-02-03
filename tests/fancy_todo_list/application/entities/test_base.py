import pytest
import uuid
from fancy_todo_list.application.entities.base import RefId


class TestRefId:
    def test_should_create(self):
        ref = uuid.uuid4()
        instance = RefId.create(ref)
        assert isinstance(instance, RefId)
        assert instance.value == ref

    def test_should_not_create_from_constructor(self):
        ref = uuid.uuid4()
        with pytest.raises(AssertionError):
            RefId(ref, None)

        with pytest.raises(AssertionError):
            RefId(ref, object())

    def test_should_not_create(self):
        ref = ""
        with pytest.raises(ValueError):
            RefId.create(ref)

        ref = None
        with pytest.raises(ValueError):
            RefId.create(ref)
