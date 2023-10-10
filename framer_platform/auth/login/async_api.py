import asyncio
from typing import AsyncGenerator

from sqlalchemy import Column, Integer, String, Boolean, select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# 定義數據庫連接URL
# DATABASE_URL = "postgresql+asyncpg://myuser:mypassword@127.0.0.1:5432/mydatabase"
DATABASE_URL = (
    "postgresql+asyncpg://myuser:mypassword@host.docker.internal:5432/mydatabase"
)


class User(Base):
    __tablename__ = "USER"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    address = Column(String)
    is_framer = Column(Boolean)


async def main():
    # 創建異步數據庫引擎
    engine = create_async_engine(DATABASE_URL, echo=False, future=True)

    # 創建數據庫表格（如果不存在）
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # 創建異步Session
    Session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async def get_async_session(
        async_session: async_sessionmaker,
    ) -> AsyncGenerator[AsyncSession, None]:
        async with async_session() as session:
            yield session

    # async with Session() as session:
    # 創建一個新的User記錄
    # new_user = User(
    #     email="user@example.com",
    #     username="user123",
    #     password="password123",
    #     address="123 Main St",
    #     is_framer=False,
    # )

    # # 將User記錄添加到數據庫
    # session.add(new_user)
    # await session.commit()

    # 查詢所有User記錄
    # 執行查詢並獲取所有User記錄
    async for session in get_async_session(Session):
        # 執行查詢並獲取所有User記錄
        result = await session.execute(select(User))
        users = result.scalars().all()

        # 打印所有User記錄
        for user in users:
            print(
                f"user id: {user.id}, email: {user.email}, username: {user.username}, address: {user.address}, is_framer: {user.is_framer}"
            )


if __name__ == "__main__":
    asyncio.run(main())
