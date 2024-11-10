import uuid
from datetime import datetime
from db import Base
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True, default=str(uuid.uuid4()))
    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    online: Mapped[bool] = mapped_column(nullable=True)
    logged_at: Mapped[datetime] = mapped_column(nullable=True)