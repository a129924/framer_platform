from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from framer_platform.database.database_urls import select_database_url
from framer_platform.database.models.base import BASE  # noqa: F401

DATABASE_URL: str = select_database_url("postgresql")
engine = create_async_engine(DATABASE_URL, future=True, echo=True)
async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
