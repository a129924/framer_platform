from dotenv import dotenv_values

DATABSE_URL: str = dotenv_values().get("DATABASE_URL", "")  # type: ignore
