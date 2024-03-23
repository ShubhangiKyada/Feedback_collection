from fastapi import APIRouter,Depends
from src.resource.services.schema import ServiceRequest
from src.functionality.services.services import  create_service,get_all_services,view_service,update_service,delete_service
from typing import Annotated
from src.utils.validator import authorization

service_router=APIRouter()

@service_router.post("/service",status_code=201)
def create_service_api(service_data:ServiceRequest,user_data:Annotated[dict, Depends(authorization)]):
    service_info = create_service(service_data.model_dump(),user_data)
    return service_info

@service_router.get("/all_service",status_code=200)
def get_service_api():
    service_info=get_all_services()
    return service_info

@service_router.get("/service/{service_id}",status_code=200)
def view_service_api(service_id):
    service_info=view_service(service_id)
    return service_info

@service_router.patch("/service/{service_id}",status_code=200)
def update_service_api(service_id,service_data:ServiceRequest,user_data:Annotated[dict, Depends(authorization)]):
    service_info=update_service(service_id,service_data.model_dump(),user_data)
    return service_info


@service_router.delete("/service/{service_id}",status_code=204)
def delete_service_api(service_id,user_data:Annotated[dict, Depends(authorization)]):
    service_info=delete_service(service_id,user_data)
    return service_info