from pydantic import BaseModel, Field, EmailStr
from datetime import date

class UserSchema(BaseModel):
    id : str = Field(default=None)
    name : str = Field(...)
    dob : date = Field(...) #,alias="date"
    email: EmailStr = Field(...)
    password: str = Field(...)  


    class Config:
        schema_extra = {
            "example": {
                "name": "Joelay field",
                "dob": "2000-12-11",
                "email": "joe@xyz.com",
                "password": "any"
            }
        }
        orm_mode = True
        
class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "sitaram@gmail.com",
                "password": "any"
            }
        }    
        orm_mode = True

             
               