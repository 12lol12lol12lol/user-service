from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import collection_router, user_router

# create application
app = FastAPI()

# mount static directory
app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(router=user_router)
app.include_router(router=collection_router)
