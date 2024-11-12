import uuid
from datetime import datetime
from db import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(50), primary_key=True, default=str(uuid.uuid4()))
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(200))
    online: Mapped[bool] = mapped_column(nullable=True)
    logged_at: Mapped[datetime] = mapped_column(nullable=True)