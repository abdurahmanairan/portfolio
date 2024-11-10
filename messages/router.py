from fastapi import APIRouter, Depends, WebSocket
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from .schema import *
from base_schema import *
from .crud import *
from db import get_db
from auth import authorize

messages_router = APIRouter()
bearer = HTTPBearer()

@messages_router.get('')
async def register(db: AsyncSession = Depends(get_db), token: HTTPAuthorizationCredentials = Depends(bearer)):
    id = await authorize(token.credentials, db)
    return await get_all(id["id"], db)
