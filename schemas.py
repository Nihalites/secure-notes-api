from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class NoteCreate(BaseModel):
    content: str

class NoteOut(BaseModel):
    id: int
    content: str

    class Config:
        orm_mode = True

