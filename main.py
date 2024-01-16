from fastapi import FastAPI

from typing import Optional

from pydantic import BaseModel

app = FastAPI() #instance


@app.get('/blog') # / is localhost base @ is decorator
def index(limit=10,published:bool=True, sort: Optional[str] = None):
    # only get 10 public blog
    if published:
        return {'data':f'{limit} published blogs from the db'}
    else:
        return {'data':f'{limit} blogs from the db'}

@app.get('/blog/unpublished') # 순서 중요 line by line
def unpublished():
    return {'data' : 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int):    
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{'1','2'}}

class Blog(BaseModel):
    title: str
    body: str
    published : Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return {'data' : f"Blog is created with title as {Blog.title}"}

'''
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
'''