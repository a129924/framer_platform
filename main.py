from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def item(item_id: int, q: Optional[str]) -> dict[str, int | Optional[str]]:
    return {"item_id": item_id, "q": q}
