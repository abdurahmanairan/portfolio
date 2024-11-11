import uuid
from datetime import datetime
from db import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Message(Base):
    __tablename__ = "messages"

    id: Mapped[str] = mapped_column(primary_key=True, default=uuid.uuid4())
    text: Mapped[str]
    sender: Mapped[str] = mapped_column(ForeignKey('users.id'))
    recipient: Mapped[str] = mapped_column(ForeignKey('users.id'))
    time: Mapped[datetime]

    user = relationship("User")