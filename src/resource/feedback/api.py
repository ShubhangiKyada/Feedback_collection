from fastapi import APIRouter,Depends
from src.resource.feedback.schema import FeedbackRequest,UpdatedFeedback
from src.functionality.feedback.feedback import  create_feedback,get_feedback,get_service_feedback,update_feedback,delete_feedback
from typing import Annotated
from src.utils.validator import authorization

feedback_router=APIRouter()

@feedback_router.post("/feedback",status_code=201)
def create_feedback_api(feedback_data:FeedbackRequest,user_data:Annotated[dict, Depends(authorization)]):
    feedback_info = create_feedback(feedback_data.model_dump(),user_data)
    return feedback_info
    

@feedback_router.get("/all_feedback",status_code=201)
def get_feedback_api():
    feedback_info=get_feedback( )
    return feedback_info
    

@feedback_router.get("/feedback/{service_id}",status_code=201)
def get_service_feedback_api(service_id):
    feedback_info=get_service_feedback( service_id)
    return feedback_info
    

@feedback_router.patch("/feedback/{feedback_id}",status_code=201)
def update_feedback_api(feedback_id,feedback_data:UpdatedFeedback,user_data:Annotated[dict, Depends(authorization)]):
    feedback_info=update_feedback(feedback_id,feedback_data.model_dump(),user_data.get("id"))
    return feedback_info
    


@feedback_router.delete("/feedback/{feedback_id}",status_code=201)
def delete_feedback_api(feedback_id,user_data:Annotated[dict, Depends(authorization)]):
    feedback_info=delete_feedback(feedback_id,user_data.get("id"))
    return feedback_info
    