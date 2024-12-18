from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from .models import Message
from .schema import *
from users.models import User
from base_schema import *
from config import settings

async def get_all(id: str, db: AsyncSession):
    msg_query = await db.execute(
        select(Message).where(Message.sender == id or Message.recipient == id)
    )
    msgs = msg_query.scalars().all()
    if msgs == []:
        return {"msg": "No messages"}
    return [MessageBase.model_validate(msg) for msg in msgs]