from pydantic import BaseModel
from datetime import datetime

class MessageBase(BaseModel):
    sender: str
    text: str
    time: datetime
    recipient: str

    class Config:
        from_attributes = True