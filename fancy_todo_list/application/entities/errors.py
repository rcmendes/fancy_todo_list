class InvalidUsernameError(Exception):
    error_id = "error:username:invalid"

    def __init__(self, detail: str):
        message = f"'username' is invalid. Detail:{detail}"
        self._detail = detail

        super(InvalidUsernameError, self).__init__(message)

    @property
    def detail(self):
        return self._detail
