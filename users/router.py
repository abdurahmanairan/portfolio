from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .schema import *
from base_schema import *
from crud import *
from db import get_db

users_router = APIRouter()

@users_router.post('', response_model=Created, status_code=201)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create(user, db)

@users_router.get('')
async def user_list(db: AsyncSession = Depends(get_db)):
    return await get_all(db)

@users_router.post('/auth')
async def auth(user: UserAuth, db: AsyncSession = Depends(get_db)):
    return await auth(user, db)