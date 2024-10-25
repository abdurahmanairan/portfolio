from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserAuth(BaseModel):
    email: str
    password: str

class UserBase(BaseModel):
    id: str
    name: str
    email: str