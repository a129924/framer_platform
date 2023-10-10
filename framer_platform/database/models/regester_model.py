from sqlalchemy import Integer, String, Boolean, BINARY
from sqlalchemy.orm import mapped_column, Mapped

from framer_platform.database import BASE, AsyncSession


class User(BASE):
    __tablename__ = "USER"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    _password: Mapped[bytes] = mapped_column(BINARY, name="password")
    phone_number: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(String)
    is_framer: Mapped[bool] = mapped_column(Boolean)

    @property
    def password(self) -> bytes:
        return self._password

    @password.setter
    def password(self, new_password: str) -> None:
        from bcrypt import hashpw, gensalt

        self._password = hashpw(new_password.encode("utf-8"), gensalt())

    def check_password(self, password: str, hashed_password: bytes) -> bool:
        from bcrypt import checkpw

        return checkpw(password.encode("UTF-8"), hashed_password=hashed_password)

    async def user_login(
        self,
        async_session: AsyncSession,
        username: str,
        password: str,
    ) -> bool:
        result: User = await User().find(
            db_session=async_session, username=username
        )  # type: ignore

        return self.check_password(password, result.password) if result else False
