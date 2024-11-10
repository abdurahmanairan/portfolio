import jwt
import pickle
from fastapi import HTTPException, WebSocket
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import User
from .schema import *
from base_schema import *
from config import settings, redis
from .userbot import manager

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")             #Создание экземпляра модуля хэширования, шифрования и 
                                                                              #проверки паролей
async def create(user: UserCreate, db: AsyncSession):
    user_add = User(
        name=user.name,
        email=user.email,
        password=pwd_context.hash(user.password)
    )
    db.add(user_add)
    await db.commit()
    return Created

async def get(id: str, db: AsyncSession):
    users_query = await db.execute(select(User).where(User.id == id))
    user = users_query.scalars().first()
    return UserBase.model_validate(user)

async def auth(user: UserAuth, db: AsyncSession):
    user_query = await db.execute(select(User))
    credentials = user_query.scalars().first()
    if credentials != None:
        if pwd_context.verify(user.password, credentials.password):
            token = jwt.encode(
                {"id": credentials.id},
                settings.JWT_SECRET_KEY,
                settings.JWT_ALGORITHM
            )
            return {
                "id": credentials.id,
                "name": credentials.name,
                "email": credentials.email,
                "access_token": token,
                "msg": "OK"
            }
        else:
            raise HTTPException(
            status_code=401,
            detail="Not authorized" 
        )
    else:
        raise HTTPException(
            status_code=401,
            detail="Not authorized" 
        )
    
async def connect(id: str, websocket: WebSocket, db: AsyncSession):
    await manager.connect(id, websocket, db)