"""
Route definitions
"""
from db import db
from fastapi import APIRouter, HTTPException
from models.user import UserModel, UserSignUpModel
from services.user import SignUpUserService, UserServiceException

router = APIRouter()


@router.post('/auth/sign_up', response_model=UserModel, response_model_exclude={'password'})
async def sign_up(user: UserSignUpModel):
    user_sign_up_service = SignUpUserService(user=user, db=db)
    try:
        res = await user_sign_up_service.run()
    except UserServiceException as ex:
        raise HTTPException(status_code=404, detail=ex.get_message())
    return res
