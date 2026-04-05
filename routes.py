from fastapi import APIRouter, Depends
from pydantic import BaseModel
from database import get_db
from sqlalchemy.orm import Session


import services


class ContactMessage(BaseModel):
    name: str
    email: str
    message: str


class PostCreate(BaseModel):
    title: str
    category: str
    content: str


class PostUpdate(BaseModel):
    title: str = None  # type: ignore
    content: str = None  # type: ignore


router = APIRouter()


@router.post("/contact")
def submit_contact(data: ContactMessage, db: Session = Depends(get_db)):
    contact = services.create_contact(db, data.name, data.email, data.message)
    return {
        "id": contact.id,
        "name": contact.name,
        "status": "Contact saved succesfully"
    }


@router.get('/list_contacts')
def list_contact(db: Session = Depends(get_db)):
    contacts = services.get_all_contacts(db)
    return {
        "total": len(contacts),
        "contacts": [{
            "id": c.id,
            "name": c.name,
            "email": c.email,
            "message": c.message,
            "created_at": c.created_at
        } for c in contacts]
    }


@router.post("/post")
def create_new_post(data: PostCreate, db: Session = Depends(get_db)):
    post = services.create_post(db, data.title, data.category, data.content)
    return {
        "id": post.id,
        "title": post.title,
        "details": "post sucessfull"
    }


@router.get('/posts')
def list_all_posts(db: Session = Depends(get_db)):
    return {"message": "hello!!"}


@router.get('/posts{post_id}')
def find_post(post_id: int, db: Session = Depends(get_db)):
    pass


@router.put('/posts/{post_id}')
def update_post(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
    pass


@router.delete('/posts/{post_id}')
def delete_post(post_id: int, db: Session = Depends(get_db)):
    pass


@router.post("/log-visitor")
def log_visitor(request_data: dict, db: Session = Depends(get_db)):
    pass


@router.post("/stats")
def get_stats(db: Session = Depends(get_db)):
    pass
