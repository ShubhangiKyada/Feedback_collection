from fastapi import APIRouter, Depends
from typing import Annotated
from src.utils.validator import authorization
from src.resource.user.schema import UserRequest,AdminRequest
from src.functionality.user.user import get_user_info, create_user ,delete_user,get_all_user,create_admin

user_router = APIRouter()

@user_router.post("/signup", status_code=201)
def create_user_api(user_data: UserRequest):
    user_info = create_user(user_data.model_dump())
    return user_info

@user_router.post("/admin_signup", status_code=201)
def create_admin_api(admin_data:AdminRequest):
    admin_info = create_admin(admin_data.model_dump())
    return admin_info

@user_router.get("/user_info", status_code=200)
def get_user_info_api(user_information: Annotated[dict, Depends(authorization)]):
    user_info = get_user_info(user_information.get("id"))
    return user_info

@user_router.get("/all_user_info", status_code=200)
def get_user_info_api(user_information: Annotated[dict, Depends(authorization)]):
    user_info = get_all_user(user_information)
    return user_info

@user_router.delete("/user_delete/{user_id}",status_code=204)
def delete_user_api(user_id:str,user_information: Annotated[dict, Depends(authorization)]):
    user_info = delete_user(user_id,user_information)
    return user_info
