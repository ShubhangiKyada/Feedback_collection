from database.database import Sessionlocal
from src.resource.user.model import User
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import or_
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.resource.authentication.serializer import user_detail_serializer
from src.utils.jwt_token import generate_token


db = Sessionlocal()


def login(user_details):
    email = user_details.get("email")
    phone_no = user_details.get("phone_no")
    password = user_details.get("password")

    if email or phone_no:
        user_data = (
            db.query(User)
            .filter(
                or_((User.email == email), (User.phone_no == phone_no)),
                User.is_active == True,
                User.is_deleted == False,
            )
            .first()
        )

        if user_data:
            if check_password_hash(user_data.password, password):
                user_information = user_detail_serializer(user_data)
                access_token = generate_token(user_information, 7)
                refresh_token = generate_token(user_information, 30)
                db.commit()
                db.close()
                return JSONResponse(
                    {"acess_token": access_token, "refresh_token": refresh_token},
                    status_code=200,
                )
            else:
                raise HTTPException(status_code=401, detail="Incorrect Password")
        else:
            raise HTTPException(status_code=404, detail="User not found")
    else:
        raise HTTPException(status_code=400, detail="Email or Phone no Required")


def change_password(user_details, user_id):
    password = user_details.get("password")
    new_password = generate_password_hash(user_details.get("new_password"))

    if user_id:
        user_data = (
            db.query(User)
            .filter_by(id=user_id, is_active=True, is_deleted=False)
            .first()
        )
    else:
        raise HTTPException(status_code=404, detail="User Not Found")

    if user_data:
        if check_password_hash(user_data.password, password):
            if password == user_details.get("new_password"):
                raise HTTPException(
                    status_code=409, detail="New and Old Passwords cannot be the same."
                )
            user_data.password = new_password
            db.commit()
            db.close()
            return JSONResponse(
                {"massage": "Password successfully Changed"}, status_code=200
            )
        else:
            raise HTTPException(status_code=401, detail="Current Password is Incorrect")
