from pydantic import BaseModel


class Register(BaseModel):
    username: str
    password: str
    email: str
    name: str


class Login(BaseModel):
    username: str
    password: str
