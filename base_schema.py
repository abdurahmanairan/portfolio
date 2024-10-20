from pydantic import BaseModel

class Created(BaseModel):
    msg: str = "Created"