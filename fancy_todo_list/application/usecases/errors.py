class RepositoryError(Exception):
    error_id = "error:repository"

    def __init__(self, repository: str, message: str):
        self._repository = repository
        self._message = message

        super(RepositoryError, self).__init__(message)

    @property
    def repository(self):
        return self._repository

    @property
    def message(self):
        return self._message


class UserNotFoundByRefIdError(Exception):
    error_id = "error:user:not_found:ref_id"

    def __init__(self, ref_id: str):
        message = f"User with ref ID '{ref_id}' was not found."
        self._message = message

        super(UserNotFoundByRefIdError, self).__init__(message)

    @property
    def message(self):
        return self._message
