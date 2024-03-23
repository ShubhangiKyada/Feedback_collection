from pydantic import BaseModel

class FeedbackRequest(BaseModel):
    
    service_id: str
    feedback : str

class UpdatedFeedback(BaseModel):
    
    feedback : str      
