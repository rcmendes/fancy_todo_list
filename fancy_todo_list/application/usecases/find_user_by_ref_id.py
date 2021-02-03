from .ports import UserRepository, FindUserByRefIdRequest, FindUserByRefIdResponse
from .errors import RepositoryError, UserNotFoundByRefIdError
from fancy_todo_list.application.entities import User, Username, RefId


class FindUserByRefId:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def execute(self, request: FindUserByRefIdRequest) -> FindUserByRefIdResponse:
        ref_id = RefId.create_from_uuid_str(request.ref_id)

        try:
            user = self._user_repository.get_by_ref_id(ref_id)
        except Exception as ex:
            class_name = self.__class__.__name__
            raise RepositoryError(repository=class_name, message=ex)

        if not user:
            raise UserNotFoundByRefIdError(str(ref_id))

        return FindUserByRefIdResponse(
            ref_id=str(user.ref_id), username=user.username.value
        )
