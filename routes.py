from fastapi import APIRouter, Depends
from pydantic import BaseModel
from database import get_db
from sqlalchemy.orm import Session
from typing import List

import services


class ContactMessage(BaseModel):
    id: int
    name: str
    email: str
    content: str


class PostCreate(BaseModel):
    id: int
    title: str
    topic: str
    date: str
    tags: List[str]
    content: str


class PostUpdate(BaseModel):
    title: str = None  # type: ignore
    tags: List[str] = None  # type: ignore
    content: str = None  # type: ignore


router = APIRouter()


@router.post("/api/contact")
def submit_contact(data: ContactMessage, db: Session = Depends(get_db)):
    return {
        "id": data.id,
        "name": data.name,
        "status": "message srnt succesfully"
    }


@router.get('/api/list_contacts')
def list_contact(db: Session = Depends(get_db)):
    pass


@router.post("/api/post")
def create_new_post(post: PostCreate):
    pass


@router.get('/api/posts')
def list_all_posts(db: Session = Depends(get_db)):
    pass


@router.get('/api/posts{post_id}')
def find_post(post_id: int, db: Session = Depends(get_db)):
    pass


@router.put('/api/posts/{post_id}')
def update_post(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
    pass


@router.delete('/api/posts/{post_id}')
def delete_post(post_id: int, db: Session = Depends(get_db)):
    pass


@router.post("/api/log-visitor")
def log_visitor(request_data: dict, db: Session = Depends(get_db)):
    pass


@router.post("/api/stats")
def get_stats(db: Session = Depends(get_db)):
    pass
