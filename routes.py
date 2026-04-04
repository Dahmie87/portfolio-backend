from fastapi import APIRouter, Depends
from pydantic import BaseModel
from database import Base
from sqlalchemy.orm import Session
from typing import List

import services

router = APIRouter()


class ContactMessage(BaseModel):
    name: str
    email: str
    content: str


class PostCreate(BaseModel):
    title: str
    topic: str
    date: str
    tags: List[str]
    content: str


class PostUpdate(BaseModel):
    title: str = None  # type: ignore
    tags: List[str] = None  # type: ignore
    content: str = None  # type: ignore
