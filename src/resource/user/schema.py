from pydantic import BaseModel
from typing import Optional


class UserRequest(BaseModel):
    
    first_name : Optional[str]
    last_name : Optional[str]
    name : Optional[str]
    email : Optional[str]=None
    phone_no : Optional[str]=None
    password :Optional[str]=None

class AdminRequest(BaseModel):
    
    first_name : Optional[str]
    last_name : Optional[str]
    name : Optional[str]
    email : Optional[str]=None
    phone_no : Optional[str]=None
    password :Optional[str]=None 
    admin_key : str   
    