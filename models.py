# models.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    phone_number = Column(String, unique=True, nullable=False, index=True)
    display_name = Column(String, nullable=True)
    
    tier = Column(String, default="free") 
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Friendship(Base):
    __tablename__ = 'friendships'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id_1 = Column(Integer, index=True)
    user_id_2 = Column(Integer, index=True)
    established_at = Column(DateTime, default=datetime.utcnow)
