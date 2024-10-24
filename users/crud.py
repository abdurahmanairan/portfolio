import jwt
from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import User
from .schema import *
from base_schema import *
from config import settings

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

async def get_all(db: AsyncSession):
    users_query = await db.execute(select(User))
    users = users_query.scalars().all()
    return [User.model_validate(user) for user in users]

async def auth(user: UserAuth, db: AsyncSession):
    user_query = await db.execute(select(User))
    credentials = user_query.scalars().first()
    if user != None:
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
                "access_token": token
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