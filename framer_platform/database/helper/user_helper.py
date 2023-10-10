from typing import Sequence
from sqlalchemy import select, and_
from sqlalchemy.engine import Row

from . import BaseHelper
from .. import AsyncSession
from ..models.regester_model import User


class UserHelper(BaseHelper):
    def __init__(self, async_session: AsyncSession) -> None:
        self.async_session = async_session

    async def get_one(self, username: str, password: str) -> tuple[str] | None:
        result = await self.async_session.execute(
            select(User).where(
                and_(User.username == username, User.password == password)
            )
        )

        return user[0] if (user := result.fetchone()) else None

    async def get_all(self) -> Sequence[Row[User]]:
        result = await self.async_session.execute(select(User))

        return result.fetchall()

    async def update(self, *args, **kwagrs):
        return await super().update(*args, **kwagrs)

    async def delete_one(self, *args):
        return await super().delete_one(*args)
