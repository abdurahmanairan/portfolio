from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import User
from .schema import *
from base_schema import *

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
    return users