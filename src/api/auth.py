from typing import Annotated

from db.postgres import get_session
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from models.entity import User
from schemas.entity import UserCreate, UserInDB
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(tags=["auth"])


@router.post("/signup", response_model=UserInDB, status_code=status.HTTP_201_CREATED)
async def create_user(user_create: UserCreate, db: Annotated[AsyncSession, Depends(get_session)]) -> UserInDB:
    user_dto = jsonable_encoder(user_create)
    user = User(**user_dto)
    db.add(user)
    await db.commit()
    await db.refresh(user)

    return UserInDB(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name
    )
