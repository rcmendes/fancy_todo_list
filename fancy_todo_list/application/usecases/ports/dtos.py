from dataclasses import dataclass


@dataclass(frozen=True)
class CreateUserRequest:
    username: str


@dataclass(frozen=True)
class CreateUserResponse:
    ref_id: str


@dataclass(frozen=True)
class FindUserByRefIdRequest:
    ref_id: str


@dataclass(frozen=True)
class FindUserByRefIdResponse:
    ref_id: str
    username: str
