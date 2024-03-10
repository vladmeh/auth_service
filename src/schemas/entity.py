from uuid import UUID

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserInDB(BaseModel):
    id: UUID
    username: str
    email: str
