from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    name: str

    class Config:
        from_attributes = True

class MessageBase(BaseModel):
    sender: str
    text: str
    time: datetime
    recipient: str
    user: User

    class Config:
        from_attributes = True