from pydantic import BaseModel, Field


class UserRequest(BaseModel):
    sity: str = Field(min_length=3, max_length=20)