from typing import TypedDict
from pytest import fixture, mark, FixtureRequest


class UserInfo(TypedDict):
    user: str
    password: int


user_infos: list[UserInfo] = [
    {"user": "AAA", "password": 123},
    {"user": "bbb", "password": 456},
]


@fixture()
def login(request: FixtureRequest) -> UserInfo:
    print(f"request: {request.param:}")

    return request.param


@mark.parametrize("login", user_infos, indirect=True)
def test_one_param(login: UserInfo) -> None:
    assert login["user"] == "AAA" and login["password"] == 123
