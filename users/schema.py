from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserAuth(BaseModel):
    email: EmailStr
    password: str

class UserBase(BaseModel):
    id: str
    name: str
    email: str

    class Config:
        from_attributes = True

class MessageBase(BaseModel):
    text: str
    recipient: str

class MessageReceive(BaseModel):
    text: str
    sender: str
    time: datetime