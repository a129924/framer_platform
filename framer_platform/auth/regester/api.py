from framer_platform.auth.schemas import UserRegester, UserRegesterResponse
from framer_platform.database import get_async_session, AsyncSession
from framer_platform.database.models.regester_model import User

from fastapi import APIRouter, Depends, status

# from fastapi.responses import JSONResponse；

regester_router = APIRouter(tags=["regester"])


@regester_router.post(
    "/userRegister",
    status_code=status.HTTP_201_CREATED,
    response_model=UserRegesterResponse,
)
async def regester_user(
    payload: UserRegester, async_session: AsyncSession = Depends(get_async_session)
):
    await User(**payload.model_dump()).save(db_session=async_session)

    return payload
