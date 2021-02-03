from dataclasses import dataclass
from .base import RefId
from .errors import InvalidUsernameError


@dataclass(frozen=True)
class Username:
    __create_key = object()

    value: str
    create_key: object

    def __post_init__(self):
        class_name = self.__class__.__name__
        assert self.create_key == Username.__create_key, (
            f"{class_name} instance must be created by "
            + f"using the '{class_name}.create' method."
        )

    @classmethod
    def create(cls, value: str) -> "Username":
        if not isinstance(value, str):
            raise InvalidUsernameError("'value' must be a string value.")

        value = value.strip()

        if not (3 < len(value) < 21):
            raise InvalidUsernameError(
                "'value must be a string with at least 4 and a maximum of 20 characters."
            )

        return Username(value=value, create_key=cls.__create_key)


@dataclass(frozen=True)
class User:
    ref_id: RefId
    username: Username

    def __post_init__(self):
        assert isinstance(self.ref_id, RefId), "'ref_id' must be an instance of RefId."
        assert isinstance(
            self.username, Username
        ), "'username' must be an instance of Username."
