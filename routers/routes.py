"""
Route definitions
"""
from db import db
from fastapi import APIRouter, HTTPException
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordRequestForm
from loguru import logger
from models import Token, UserModel, UserSignUpModel
from services.user import SignUpUserService, UserServiceException, auth_user

router = APIRouter()


@router.post('/auth/sign_up', response_model=UserModel, response_model_exclude={'password'})
async def sign_up(user: UserSignUpModel):
    user_sign_up_service = SignUpUserService(user=user, db=db)
    try:
        res = await user_sign_up_service.run()
    except UserServiceException as ex:
        raise HTTPException(status_code=404, detail=ex.get_message())
    return res


@router.post('/auth/token', response_model=Token)
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await auth_user(form_data.username, form_data.password)
    logger.info(user)
    return {}
