from dataclasses import dataclass
from typing import Union

from loguru import logger
from models import UserModel, UserSignUpModel
from repository.user import UserRepo

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
    user_repo: UserRepo = UserRepo()

    async def run(self) -> Union[UserModel, UserServiceException]:
        # Check for None
        if self.user is None:
            raise UserServiceException('user is None')
        # Check unique username
        user = await self.user_repo.get_user(self.user.username)
        if user is not None:
            raise UserServiceException(
                f'{self.user.username} user already exists')

        # hash password
        self.user.password = get_hashed_password(self.user.password)

        # create user
        user_model = UserModel(
            **self.user.dict()
        )
        return await self.user_repo.create_user(user_model)
