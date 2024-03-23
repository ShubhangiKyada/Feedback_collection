from database.database import Sessionlocal
from src.resource.user.model import User
from werkzeug.security import generate_password_hash
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.resource.authentication.serializer import getuser_serializer
import uuid
from src.config import Config

db = Sessionlocal()

def create_user(user_details):
    id=str(uuid.uuid4())

    if  user_details.get('email') is None and user_details.get('phone_no') is None:
        raise HTTPException(status_code=422,detail="Please enter emial or phone no")
    if not user_details.get('password'):
        raise HTTPException(status_code=422,detail="Please enter Password")

    
    user_info = User(
        id=id,
        first_name=user_details.get("first_name"),
        last_name=user_details.get("last_name"),
        name=user_details.get("name"),
        email=user_details.get("email"),
        phone_no=user_details.get("phone_no"),
        password=generate_password_hash(user_details.get("password")),
        role='user',
    )
    
    db.add(user_info)
    db.commit()
    db.close()

    return JSONResponse({"Message": "User successfully created","User_id":str(id)})
    
def create_admin(admin_details):
    id=str(uuid.uuid4())
    admin_key= admin_details.get('admin_key')==Config.ADMIN_KEY

    if  admin_details.get('email') is None and admin_details.get('phone_no') is None:
        raise HTTPException(status_code=422,detail="Please enter email or phone no")
    
    if not admin_details.get('password'):
        raise HTTPException(status_code=422,detail="Please enter Password")
    
    if admin_key:
        admin_info = User(
                id=id,
                first_name=admin_details.get("first_name"),
                last_name=admin_details.get("last_name"),
                name=admin_details.get("name"),
                email=admin_details.get("email"),
                phone_no=admin_details.get("phone_no"),
                password=generate_password_hash(admin_details.get("password")),
                role='admin',
            )
        
        db.add(admin_info)
        db.commit()
        db.close()

        return JSONResponse({"Message": "Admin successfully created","Admin_id":str(id)})
    
    else:
        raise HTTPException(status_code=403,detail= "Admin key is invalid")

def get_user_info(user_id):

    user_data = (
        db.query(User).filter_by(id=user_id, is_active=True, is_deleted=False).first()
    )

    if user_data:
        filter_data=getuser_serializer(user_data)
        db.commit()
        db.close()
        return JSONResponse({"Data": filter_data})
    else:
        raise HTTPException(status_code=404, detail="User Not Found")
    
def get_all_user(admin_data):
    if admin_data.get("role")=="admin":
        user_data=db.query(User).all()
        if user_data:

            filter_data=getuser_serializer(user_data)
            db.commit()
            db.close()
            return JSONResponse({"Data": filter_data})
        else:
            raise HTTPException(status_code=404, detail="User Not Found")
    else:
        raise HTTPException(status_code=403,detail="You are not Authorized")
    
def  delete_user(user_id,user_details):
    if user_id==user_details.get("id"):

        user_data = (
            db.query(User).filter_by(id=user_id, is_active=True, is_deleted=False).first()
        )
        if user_data:
            user_data.is_active=False
            user_data.is_deleted=True
            db.commit()
            db.close()
            return JSONResponse({"message":"User deleted Successfully"})
    else:
        raise HTTPException(status_code=409,detail="Invalid User id")