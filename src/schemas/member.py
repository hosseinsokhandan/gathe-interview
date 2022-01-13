from pydantic import BaseModel


class MemberSchema(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
