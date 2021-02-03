from .ports import UserRepository, CreateUserRequest, CreateUserResponse
from .errors import RepositoryError
from fancy_todo_list.application.entities import User, Username, RefId


class CreateUser:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def execute(self, request: CreateUserRequest) -> CreateUserResponse:
        username = Username.create(request.username)
        ref_id = RefId.new()

        user = User(ref_id=ref_id, username=username)
        try:
            self._user_repository.insert(user)
        except Exception as ex:
            class_name = self.__class__.__name__
            raise RepositoryError(repository=class_name, message=ex)

        return CreateUserResponse(str(ref_id.value))
