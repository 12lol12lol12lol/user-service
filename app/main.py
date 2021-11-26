from fastapi import FastAPI

from routers import router


# create application
app = FastAPI()

app.include_router(router=router)
