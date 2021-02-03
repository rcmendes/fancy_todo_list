import abc
from fancy_todo_list.application.entities.user import User
from fancy_todo_list.application.entities.base import RefId


class UserRepository(abc.ABC):
    @abc.abstractmethod
    def insert(self, user: User) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_by_ref_id(self, ref_id: RefId) -> User:
        raise NotImplementedError()

    @abc.abstractmethod
    def list_all(self) -> [User]:
        raise NotImplementedError()
