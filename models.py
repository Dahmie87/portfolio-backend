from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
