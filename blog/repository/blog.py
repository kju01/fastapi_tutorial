from sqlalchemy.orm import Session
import models, schemas, database
from fastapi import Depends, status, HTTPException

def get_all(db):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request:schemas.Blog, db : Session = Depends(database.get_db)):
    new_blog = models.Blog(title = request.title, body = request.body, user_id=1)
    db.add(new_blog)
    db.commit() # db update?
    db.refresh(new_blog)
    return new_blog

def destroy(id:int, db:Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int, request:schemas.Blog, db : Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    blog.update(request)
    db.commit()
    return 'updated'

def show(id:int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available")
    return blog
