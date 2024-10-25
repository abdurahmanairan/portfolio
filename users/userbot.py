from fastapi import WebSocket
from sqlalchemy.ext.asyncio import AsyncSession

class Client:
    def __init__(self, websocket: WebSocket, db: AsyncSession):
        self._socket = websocket
        self._db = db
