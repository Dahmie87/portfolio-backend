from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime


class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(150))
    message = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    category = Column(String(50))
    slug = Column(String(150), unique=True)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)


class Visitors(Base):
    __tablename__ = 'visitors'

    id = Column(Integer, primary_key=True)
    ip_addr = Column(String(45))
    user_agent = Column(String(255))
    endpoints = Column(String(255))
    visited_at = Column(DateTime, default=datetime.utcnow)
