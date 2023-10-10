from typing import Literal
from .config import DATABSE_URL


def select_database_url(database: Literal["postgresql", "sqlite"]) -> str:
    match database:
        case "postgresql":
            # fmt:off
            # return "postgresql+asyncpg://myuser:mypassword@127.0.0.1:5432/mydatabase"
            # "postgresql+asyncpg://myuser:mypassword@127.0.0.1:5432/mydatabase"
            # return "postgresql+asyncpg://myuser:mypassword@host.docker.internal:5432/mydatabase"
            return DATABSE_URL
        case "sqlite":
            return ""
        case _:
            return ""
