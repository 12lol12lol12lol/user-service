"""
Route definitions
"""
from db import db
from fastapi import APIRouter, HTTPException, status
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordRequestForm
from models import Token, User, UserModel, UserSignUpModel
from repository.user import UserRepo
from services import (SignUpUserService, UserServiceException, auth_user,
                      check_user_token, create_access_token)
from settings import settings

user_router = APIRouter()


@user_router.post('/auth/sign_up', response_model=UserModel, response_model_exclude={'password'})
async def sign_up(user: UserSignUpModel):
    user_sign_up_service = SignUpUserService(user=user)
    try:
        res = await user_sign_up_service.run()
    except UserServiceException as ex:
        raise HTTPException(status_code=404, detail=ex.get_message()) from ex
    return res


@user_router.post('/auth/token', response_model=Token)
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await auth_user(UserRepo, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={'sub': user.username}, expires_delta=settings.token_expired)
    return {
        'access_token': access_token,
        'token_type': 'bearer'
    }


@user_router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(check_user_token)):
    return current_user
