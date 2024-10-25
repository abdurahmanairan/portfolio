from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .schema import *
from base_schema import *
from crud import *
from db import get_db

messages_router = APIRouter()

@messages_router.get('')
async def register(db: AsyncSession = Depends(get_db)):
    return await get_all(db)
