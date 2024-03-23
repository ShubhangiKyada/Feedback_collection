import jwt
from datetime import datetime,timedelta
from src.config import Config


def generate_token(user_data, exp=7):
    expired_time=timedelta(days=exp)
    user_data["exp"] = datetime.now() + expired_time
    
    return jwt.encode(user_data, Config.JWT_SECRET_KEY, algorithm="HS256")