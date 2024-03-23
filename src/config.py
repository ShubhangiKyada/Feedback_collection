import os
from dotenv import load_dotenv


load_dotenv()

class Config():
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"] 
    ADMIN_KEY = os.environ["ADMIN_KEY"]
    JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]