import logging
from fancy_todo_list.application.usecases.ports import UserRepository
from fancy_todo_list.application.entities import User, RefId
from .config import session
from .models import UserModel


_logger = logging.Logger(__name__)


class SQLiteUserRepository(UserRepository):
    def insert(self, user: User) -> None:
        _logger.debug(f"Preparing to insert User:{user}")

        model = UserModel.create_from(user)
        session.add(model)
        session.commit()

    def get_by_ref_id(self, ref_id: RefId) -> User:
        _logger.debug(f"Preparing to get User by ref ID:{ref_id}")

        model = session.query(UserModel).get(str(ref_id))

        if model:
            return model.to_entity()

        return None

    def list_all(self) -> [User]:
        _logger.debug(f"Preparing to list all Users")

        result = session.query(UserModel).all()

        if result:
            return [model.to_entity() for model in result]

        return None
