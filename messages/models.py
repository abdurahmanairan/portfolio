import uuid
from datetime import datetime
from db import Base
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Message(Base):
    __tablename__ = "messages"

    id: Mapped[str] = mapped_column(String(50), primary_key=True, default=uuid.uuid4())
    text: Mapped[str] = mapped_column(String(2000))
    sender: Mapped[str] = mapped_column(String(50), ForeignKey('users.id'))
    recipient: Mapped[str] = mapped_column(String(50), ForeignKey('users.id'))
    time: Mapped[datetime]