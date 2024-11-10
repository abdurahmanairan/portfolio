"""Модуль авторизации через JWT"""
import jwt
from jwt import InvalidTokenError
from fastapi import HTTPException, status, Depends, WebSocket, Query, WebSocketException
from fastapi.security import OAuth2PasswordBearer
from typing import Union
from datetime import datetime, timedelta, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from config import settings
from db import get_db
from users.models import User
from users.crud import get
from typing import Annotated

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/v1/auth")

async def create_access_token(data: dict, 
                        expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, 
        settings.authjwt_secret_key, 
        algorithm=settings.JWT_ALGORITHM
    )
    return encoded_jwt

async def authorize(token: str, db: AsyncSession):
    try:
        decoded_jwt = jwt.decode(
            token, 
            settings.JWT_SECRET_KEY, 
            algorithms=[settings.JWT_ALGORITHM]
        )
        credentials = decoded_jwt.get("id")
        print(credentials)
        users_data = await get(credentials, db)
        if users_data == None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail={"msg": "Invalid token data"}
            )
        return {"id": credentials}
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail={"msg":"Invalid token"}
        )

async def websocket_authorize(websocket: WebSocket, 
                              db: AsyncSession = Depends(get_db), 
                              token: Annotated[str | None, Query()] = None):
    try:
        decoded_jwt = jwt.decode(
            token, 
            settings.JWT_SECRET_KEY, 
            algorithms=[settings.JWT_ALGORITHM]
        )
        credentials = decoded_jwt.get("id")
        users_data = await get(credentials, db)
        if users_data == None:
            raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
        return credentials
    except InvalidTokenError:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
