from fastapi import APIRouter

from framer_platform.database import get_async_session
from framer_platform.database.models.regester_model import User

init_db_router = APIRouter(tags=["init_db"])


data = [
    {
        "email": "user1@example.com",
        "username": "user1",
        "password": "password1",
        "phone_number": "1234567891",
        "address": "123 Main St, City1",
        "is_framer": True,
    },
    {
        "email": "user2@example.com",
        "username": "user2",
        "password": "password2",
        "phone_number": "1234567892",
        "address": "456 Elm St, City2",
        "is_framer": False,
    },
    {
        "email": "user3@example.com",
        "username": "user3",
        "password": "password3",
        "phone_number": "1234567893",
        "address": "789 Oak St, City3",
        "is_framer": True,
    },
    {
        "email": "user4@example.com",
        "username": "user4",
        "password": "password4",
        "phone_number": "1234567894",
        "address": "101 Pine St, City4",
        "is_framer": False,
    },
    {
        "email": "user5@example.com",
        "username": "user5",
        "password": "password5",
        "phone_number": "1234567895",
        "address": "202 Maple St, City5",
        "is_framer": True,
    },
]


@init_db_router.on_event("startup")
async def init_db() -> None:
    async for async_session in get_async_session():
        for user_info in data:
            if not User().find(db_session=async_session, **user_info):
                await User(**user_info).save(db_session=async_session)
