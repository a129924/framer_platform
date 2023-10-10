from pydantic import BaseModel, Field


class UserRegester(BaseModel):
    email: str
    username: str
    password: str
    phone_number: str
    address: str
    is_framer: bool = Field(default=False)


class UserRegesterResponse(BaseModel):
    email: str
    username: str


class UserLogin(BaseModel):
    username: str
    password: str
