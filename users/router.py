from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from .schema import *
from base_schema import *
from .crud import *
from db import get_db
from auth import authorize, websocket_authorize

users_router = APIRouter()
bearer = HTTPBearer()

@users_router.post('', response_model=Created, status_code=201)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create(user, db)

@users_router.get('')
async def user_list(db: AsyncSession = Depends(get_db)):
    return await get(db)

@users_router.post('/auth')
async def login(user: UserAuth, db: AsyncSession = Depends(get_db)):
    return await auth(user, db)

@users_router.websocket('/ws')
async def websocket_connect(websocket: WebSocket, token: str,
                            db: AsyncSession = Depends(get_db)):
    id = await websocket_authorize(websocket, db, token)
    return await connect(id, websocket, db)