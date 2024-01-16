from fastapi import FastAPI
import models
from database import engine
from routers import blog, user, authentication


app = FastAPI()

models.Base.metadata.create_all(engine) #create table on table

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)