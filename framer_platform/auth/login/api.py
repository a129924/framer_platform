from typing import Annotated

from framer_platform.auth.schemas import UserLogin
from framer_platform.database import get_async_session, AsyncSession
from framer_platform.database.models.regester_model import User

from fastapi import APIRouter, Depends, Cookie, Response
from fastapi.responses import JSONResponse

login_router = APIRouter(tags=["login"])


@login_router.post("/userLogin")
async def login(
    user_login: UserLogin, async_session: AsyncSession = Depends(get_async_session)
) -> JSONResponse:
    user_data = await User().user_login(
        async_session=async_session,
        username=user_login.username,
        password=user_login.password,
    )

    if user_data:
        response = JSONResponse(
            content={"status": "OK", "statusText": "success"}, status_code=200
        )
        response.set_cookie(key="userLogin", value=user_login.username, max_age=600)

        return response
    else:
        return JSONResponse(
            content={"status": "Failed", "statusText": "no user found"}, status_code=401
        )


@login_router.post("/userLogout", status_code=200)
def logout(response: Response, userLogin: str = Cookie(None)) -> JSONResponse:
    response.delete_cookie("userLogin")

    return JSONResponse(content={"username": userLogin})


@login_router.get("/get_user_login_cookie")
def get_user_login_cookie(userLogin: Annotated[str | None, Cookie()] = None) -> dict:
    return {"userLogin": userLogin}
