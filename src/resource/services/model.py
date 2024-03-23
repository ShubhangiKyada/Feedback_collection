from sqlalchemy import VARCHAR, Boolean, String, Column,DateTime,ForeignKey,Float
from database.database import Base
from datetime import datetime
from src.resource.user.model import User

class Service(Base):
    __tablename__ = "service"
    id = Column(String(256),primary_key=True)
    service_name=Column(VARCHAR(256))
    description=Column(VARCHAR(500))
    price=Column(Float)
    user_id = Column(VARCHAR(256),ForeignKey(User.id,ondelete="CASCADE"))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    
   
