from typing import TypedDict

from base.http_base import HttpClient
from pytest import fixture, mark, FixtureRequest

client = HttpClient()


class UserRegisterInfo(TypedDict):
    email: str
    username: str
    password: str
    phone_number: str
    address: str
    is_framer: bool


user_register_info: list[UserRegisterInfo] = [
    {
        "email": "user1@gmail.com",
        "username": "user1",
        "password": "Password1",
        "phone_number": "111-111-1111",
        "address": "Address1",
        "is_framer": False,
    },
    {
        "email": "user2@gmail.com",
        "username": "user2",
        "password": "Password2",
        "phone_number": "222-222-2222",
        "address": "Address2",
        "is_framer": True,
    },
    {
        "email": "user3@gmail.com",
        "username": "user3",
        "password": "Password3",
        "phone_number": "333-333-3333",
        "address": "Address3",
        "is_framer": False,
    },
    {
        "email": "user4@gmail.com",
        "username": "user4",
        "password": "Password4",
        "phone_number": "444-444-4444",
        "address": "Address4",
        "is_framer": True,
    },
    {
        "email": "user5@gmail.com",
        "username": "user5",
        "password": "Password5",
        "phone_number": "555-555-5555",
        "address": "Address5",
        "is_framer": False,
    },
]


@fixture
def register_user(request: FixtureRequest) -> int:
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    response = client.post(
        "http://127.0.0.1:8000/userRegister", json=request.param, headers=headers
    )
    return response.status_code  # type: ignore


@mark.parametrize("register_user", user_register_info, indirect=True)
def test_register_user(register_user):
    assert register_user == 422
