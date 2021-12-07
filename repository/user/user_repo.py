from typing import Optional

from db import db
from loguru import logger
from models import UserModel


class UserRepo:
    @staticmethod
    async def get_user(username: str) -> Optional[UserModel]:
        user = await db['users'].find_one({'username': username})
        return UserModel(**user) if user is not None else user

    @staticmethod
    async def create_user(user: UserModel) -> UserModel:
        insert_result = await db['users'].insert_one(user.dict())
        logger.info(f'created user username={user.username} with id={insert_result.inserted_id} ')
        data = await db['users'].find_one({'_id': insert_result.inserted_id})
        return UserModel(**data)
