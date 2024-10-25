from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Message
from .schema import *
from base_schema import *
from config import settings

async def get_all(db: AsyncSession):
    msg_query = await db.execute(select(Message))
    msgs = msg_query.scalars().all()
    return [MessageBase.model_validate(msg) for msg in msgs]