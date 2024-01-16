from fastapi import APIRouter, Depends, status
import schemas, database, oauth2
import repository.blog as blog
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/blog",
    tags=['blog']
)

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db : Session = Depends(database.get_db),get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post('/' , status_code=status.HTTP_201_CREATED) # status_code에 따라 뜻이 다름, 201 = create fastapi.status에서 뭔지 확인 가능
def create(request : schemas.Blog, db : Session = Depends(database.get_db),get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request,db)
    

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db : Session = Depends(database.get_db),get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)
    

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db : Session = Depends(database.get_db),get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)

@router.get('/{id}', status_code=200,response_model=schemas.ShowBlog) # in sql, where / schemas로 데이터 불러오는 형태 지정
def show(id, db: Session = Depends(database.get_db),get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id,db)
