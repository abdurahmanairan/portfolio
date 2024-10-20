from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .schema import *
from base_schema import *
from crud import UserBot
from db import get_db

users_router = APIRouter()

@users_router.post('', response_model=Created, status_code=201)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await UserBot.create(user, db)