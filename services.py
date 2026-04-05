from sqlalchemy.orm import Session
from models import Contact, Visitor, Post
from datetime import datetime


def create_contact(db: Session, name: str, email: str, message: str):
    contact = Contact(name=name, email=email, message=message)

    db.add(contact)

    db.commit()
    db.refresh(contact)
    return contact


def get_all_contacts(db: Session):
    all_contacts = db.query(Contact).order_by(Contact.created_at.desc()).all()
    return all_contacts


def create_post(db: Session, title: str, category: str, content: str):
    post = Post(title=title, category=category, content=content)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get_all_posts(db: Session):
    all_posts = db.query(Post).order_by(Post.created_at.desc()).all()
    return all_posts


def find_post_by_id(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()


def update_post_by_id(db: Session, post_id: int, title: str, category: str, content: str):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        return None
    if title:
        post.title = title  # type: ignore
    if category:
        post.category = category  # type: ignore
    if content:
        post.content = content  # type: ignore

    post.updated_at = datetime.utcnow()  # type: ignore
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def delete_post_by_id(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
        return True
    return False


def log_vistor(db: Session, ip_address: str, user_agent: str, endpoint: str):
    visitor = Visitor(ip_addr=ip_address,
                      user_agent=user_agent, endpoints=endpoint)
    db.add(visitor)
    db.commit()
    db.refresh(visitor)


def get_visitors_stats(db: Session):
    return db.query(Visitor).order_by(Visitor.visited_at.desc()).all()
