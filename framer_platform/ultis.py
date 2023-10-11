import http.cookies

from typing import Any


def get_cookie() -> dict[str, Any]:
    return http.cookies.SimpleCookie()
