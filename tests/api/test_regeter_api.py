# import pytest
from base.http_base import HttpClient

client = HttpClient()


def test_register_user():
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    # 定义测试数据
    data_list = [
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

    for data in data_list:
        response = client.post(
            "http://localhost:8000/userRegister", headers=headers, json=data
        )
        assert response.status_code == 201, print(f"{data:}")

    # 进一步检查响应内容，根据实际需求编写断言
    # assert response.json() == expected_data


# 添加更多测试用例...
