def view_feedback_serializer(feedback_data):

    if not isinstance(feedback_data,list):
        feedback_data=[feedback_data]

    sorted_data=[]
    for record in feedback_data:
        sorted_data.append(
            {
                "id":record.id,
                "feedback" :record.feedback,
                "service_id":record.service_id,
                "user_id":record.user_id,
                "updated_at":str(record.updated_at)
                
            }
        )
        
    return sorted_data