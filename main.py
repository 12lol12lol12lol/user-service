import os
import sys

import motor.motor_asyncio
from fastapi import FastAPI, HTTPException
from models import UserSignUpModel
from settings import init_settings
from services.user import SignUpUserService

# Initialize project settings
settings = init_settings()

# Initalize database connection
client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URL)
db = client.college

# create application
app = FastAPI()

# route definitions

@app.get('/')
async def root():
    return {}


@app.post('/auth/sign_up')
async def sign_up(user: UserSignUpModel):
    user_sign_up_service = SignUpUserService(user=user)

    return {'message': 'Ok'}
