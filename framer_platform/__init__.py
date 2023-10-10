from fastapi import FastAPI

from framer_platform.auth import login_router, regester_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(login_router, tags=["login"])
    app.include_router(regester_router, tags=["regester"])

    return app
