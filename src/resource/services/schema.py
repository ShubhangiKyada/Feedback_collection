from pydantic import BaseModel
from typing import Optional

class ServiceRequest(BaseModel):
    
    service_name : Optional[str] =None
    description : Optional[str] =None
    price : Optional[float] =None


