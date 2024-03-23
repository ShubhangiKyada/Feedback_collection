from sqlalchemy import VARCHAR, Boolean, String, Column,DateTime,ForeignKey
from database.database import Base
from datetime import datetime
from src.resource.user.model import User
from src.resource.services.model import Service

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(String(256),primary_key=True)
    feedback=Column(VARCHAR(500))
    service_id=Column(VARCHAR(256),ForeignKey(Service.id,ondelete="CASCADE"))
    user_id = Column(VARCHAR(256),ForeignKey(User.id,ondelete="CASCADE"))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    