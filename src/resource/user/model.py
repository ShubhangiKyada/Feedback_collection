from sqlalchemy import VARCHAR, Boolean, String, Column,DateTime
from database.database import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"
    id = Column(String(256),primary_key=True)
    first_name=Column(VARCHAR(30))
    last_name=Column(VARCHAR(30))
    name = Column(VARCHAR(30))
    email = Column(String(256), nullable=False)
    password = Column(VARCHAR(8010), nullable=False)
    phone_no = Column(VARCHAR(12))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    is_verify = Column(Boolean, default=False)
    role = Column(VARCHAR(10),nullable=True )
