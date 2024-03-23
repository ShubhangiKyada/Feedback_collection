from pydantic import BaseModel
from typing import Optional

class UserLoginSchema(BaseModel):
    email : Optional[str] = None
    phone_no : Optional[str] = None
    password : str

class UserChangePasswordSchema(BaseModel):
    password:str
    new_password:str


