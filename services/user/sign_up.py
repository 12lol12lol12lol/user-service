from dataclasses import dataclass
from typing import Union

from loguru import logger
from models import UserModel, UserSignUpModel
from motor.motor_asyncio import AsyncIOMotorClient

from .exceptions import UserServiceException
from .hash import get_hashed_password


@dataclass
class SignUpUserService:
    """
    Service for user sign up logic

    main method is run().
    run() return (status: bool, message: str)
    if user successfully registered return (True, '')
    else return (False, 'error message')
    """
    user: UserSignUpModel
    db: AsyncIOMotorClient

    async def run(self) -> Union[UserModel, UserServiceException]:
        # Check for None
        if self.user is None:
            raise UserServiceException('user is None')
        # Check unique username
        user = await self.db['users'].find_one({'username': self.user.username})
        if user is not None:
            raise UserServiceException(
                f'{self.user.username} user already exists')

        # hash password
        self.user.password = get_hashed_password(self.user.password)

        # create user
        user_model = UserModel(
            **self.user.dict()
        )
        insert_result = await self.db['users'].insert_one(user_model.dict())
        logger.info(f'created user username={user_model.username} with id={insert_result.inserted_id} ')
        # return result from db
        return await self.db['users'].find_one({'_id': insert_result.inserted_id})
