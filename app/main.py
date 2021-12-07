from fastapi import FastAPI
from routers import collection_router, user_router

# create application
app = FastAPI()

app.include_router(router=user_router)
app.include_router(router=collection_router)
