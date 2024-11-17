import uuid
from datetime import datetime
from db import Base
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Message(Base):
    __tablename__ = "messages"

    id: Mapped[str] = mapped_column(String(50), primary_key=True, default=uuid.uuid4())
    text: Mapped[str] = mapped_column(String(2000))
    attachment: Mapped[bytes]
    chat: Mapped[str] = mapped_column(String(50), ForeignKey('chats.id'))
    sender: Mapped[str] = mapped_column(String(50), ForeignKey('users.id'))
    created_at: Mapped[datetime]
    readed: Mapped[bool]

class Chats(Base):
    __tablename__ = "chats"

    id: Mapped[str] = mapped_column(String(50), primary_key=True, default=uuid.uuid4())
    created_at: Mapped[datetime]

class ChatsParticipants(Base):
    __tablename__ = "chats_participants"

    id: Mapped[str] = mapped_column(String(50), primary_key=True, default=uuid.uuid4())
    user: Mapped[str] = mapped_column(String(50), ForeignKey('users.id'))
    chat: Mapped[str] = mapped_column(String(50), ForeignKey('users.id'))