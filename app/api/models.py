from pydantic import BaseModel, Field, field_validator


class UserRequest(BaseModel):
    
    sity: str = Field(min_length=3, max_length=20)



class AdminKey(BaseModel):

    admin_key: str


    @field_validator("admin_key")
    @classmethod
    def validate_email(cls, value):
        if False:
            raise Exception
        
        return value 