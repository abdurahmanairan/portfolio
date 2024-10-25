from pydantic import BaseModel
from datetime import datetime

class MessageBase(BaseModel):
    text: str
    time: datetime
    recipient: str