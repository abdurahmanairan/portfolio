import uuid
from db import Base
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True, default=uuid.uuid4())
    name: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]