import asyncio
import uuid
import json
from datetime import datetime
from fastapi import WebSocket
from sqlalchemy.ext.asyncio import AsyncSession
from .schema import MessageBase
from config import redis
from messages.models import Message

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, Client] = {}

    async def connect(self, id: str, websocket: WebSocket, db: AsyncSession):
        await websocket.accept()
        if id in self.active_connections:
            await websocket.close()
        else:
            client = Client(
            websocket=websocket,
            id=id,
            db=db
            )
            self.active_connections[id] = client
            await client.run()

    def disconnect(self, id: str):
        self.active_connections.pop(id)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()

class Client:
    def __init__(self, websocket: WebSocket, id: str, db: AsyncSession):
        self._socket = websocket
        self._db = db
        self._id = id
        self.r = redis.pubsub()

    async def _init_connection(self):
        while True:
            data = await self._socket.receive_json()
            message = MessageBase.model_validate(data)
            message_save = Message(
                id=str(uuid.uuid4()),
                text=message.text,
                sender=self._id,
                recipient=message.recipient,
                time=datetime.now()
            )
            self._db.add(message_save)
            await self._db.commit()
            await redis.publish(
                message.recipient, 
                json.dumps(message.model_dump())
            )

    async def _messages_listen(self):
        await self.r.subscribe(self._id)
        while True:
            message = await self.r.get_message(ignore_subscribe_messages=True)
            if message:
                await self.send_message(json.loads(message["data"]))

    async def run(self):
        self._init_conn = asyncio.create_task(self._init_connection())
        self._redis_listen = asyncio.create_task(self._messages_listen())
        await self._init_conn
        await self._messages_listen()

    async def send_message(self, message):
        await self._socket.send_json(message)

