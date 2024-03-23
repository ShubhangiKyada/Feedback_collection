from database.database import Sessionlocal
from src.resource.services.model import Service
from fastapi import HTTPException
import uuid
from src.resource.services.serializer import view_services_serializer,update_services_serializer
from fastapi.responses import JSONResponse


db = Sessionlocal()

def create_service(service_details,admin_data):
    id=str(uuid.uuid4())
    
    if admin_data.get("role")=="admin":
        
        service_info=Service(
            id=id,
            service_name=service_details.get( "service_name" ),
            description=service_details.get('description'),
            price=service_details.get('price'),
            user_id=admin_data['id'],
        )
        db.add(service_info)
        db.commit()
        db.close()

        return JSONResponse({"Message":"Service created Successfully","Service_id":str(id)},status_code=201)
    else:
        raise HTTPException(status_code=403,detail="You are not authorized to perform this action.")
        
def get_all_services():
    services_data=db.query(Service).all()

    if services_data:
        filter_data = view_services_serializer(services_data)
        
        return JSONResponse({"Data": filter_data})
    else:
        raise HTTPException(status_code=404, detail="Services Not Found")
    
def view_service(service_id):
        services_data=db.query(Service).filter_by(id=service_id).first()

        if services_data:
            filter_data = view_services_serializer(services_data)
        
            return JSONResponse({"Data": filter_data})
        else:
            raise HTTPException(status_code=404, detail="Services Not Found")
    
def update_service(service_id,service_details,admin_data):
    if admin_data.get("role")=="admin":
        service_data=db.query(Service).filter_by(id=service_id).first()
        if service_data is None:
            raise HTTPException(status_code=404,detail="Service with the given ID does not exist.")
        else:
            service_data.service_name=service_details.get( "service_name" ) if service_details.get( "service_name" ) is not None else service_data.service_name
            service_data.description=service_details.get('description') if service_details.get('description') is not None else service_data.description
            service_data.price=service_details.get('price') if service_details.get('price') is not None else service_data.price

            filter_data = update_services_serializer(service_data)
            db.commit()
            db.close()
        return JSONResponse({
            "Message":"Service Updated Successfully",
            "Data":filter_data
        },status_code=201)
    else:
        raise HTTPException(status_code=403,detail="Unauthorised Access") 
    
def delete_service(service_id,admin_data):
    if admin_data.get("role")=="admin":
        service_data=db.query(Service).filter_by(id=service_id).first()
        if  not service_data:
            raise HTTPException(status_code=404,detail="Service with the provided id was not found.")
        else:
            db.delete(service_data)
            db.commit()
            db.close()
            return JSONResponse({
                "Message":"Service Deleted Successfully"
            })  
    else:
        raise HTTPException(status_code=403,detail="You are not authorized to perform this action.")
