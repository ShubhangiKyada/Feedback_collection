from database.database import Sessionlocal
from src.resource.feedback.model import Feedback
from fastapi import HTTPException
import uuid
from src.resource.feedback.serializer import view_feedback_serializer
from fastapi.responses import JSONResponse

db = Sessionlocal()

def create_feedback(feedback_details,user_details):
    id=str(uuid.uuid4())
    try:
        feedback_info=Feedback(
            id=id,
            feedback=feedback_details.get("feedback"),
            service_id=feedback_details.get("service_id"),
            user_id=user_details.get("id"),
        )
        db.add(feedback_info)
        db.commit()
        db.close()

        return JSONResponse({"Message":"Feedback Created Successfully","Feedback_id":str(id)})
    except Exception:
        raise HTTPException(status_code=404,detail="Service not found")

def get_feedback():
    feedback_data=db.query(Feedback).all()

    if feedback_data:
        filter_data = view_feedback_serializer(feedback_data)

        return JSONResponse({"Data": filter_data})
    
    else:
        raise HTTPException(status_code=404,detail="Feedback not found")

def get_service_feedback(service_id):
    feedback_data=db.query(Feedback).filter_by(service_id=service_id).all()

    if feedback_data:
        filter_data = view_feedback_serializer(feedback_data)

        return JSONResponse({"Data": filter_data})
    
    else:
        raise HTTPException(status_code=404,detail="Feedback not found")
    
def update_feedback(feedback_id,feedback_details,user_id):
    feedback_data=db.query(Feedback).filter_by(id=feedback_id).first()
    if not feedback_data:
        raise HTTPException(status_code=404,detail="Feedback Id is  invalid.")
    else:
        if feedback_data.user_id==user_id:

            feedback_data.feedback=feedback_details.get("feedback")  if feedback_details.get("feedback") is not None else feedback_data.feedback

            filter_data = view_feedback_serializer(feedback_data)
            db.commit()
            db.close()
            return JSONResponse({
                "Message":"Feedback Updated Successfully",
                "Data": filter_data
                })
        else:
            raise HTTPException(status_code=403,detail="You are not authorized to perform this action.")
    

def delete_feedback(feedback_id, user_id):
    feedback_data=db.query(Feedback).filter_by(id=feedback_id).first()
    if not feedback_data:
        raise HTTPException(status_code=404,detail="Feedback Id is  invalid.")
    else:
        if feedback_data.user_id==user_id:
            db.delete(feedback_data)
            db.commit()
            db.close()
            return JSONResponse({
                "Message":"Feedback Deleted Successfully"
                })
        else:
            raise HTTPException(status_code=403,detail="You are not authorized to perform this action.")
    