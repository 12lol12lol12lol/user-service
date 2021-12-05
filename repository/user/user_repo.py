from typing import Optional

from db import db
from loguru import logger
from models import UserModel
from models.user.user import User


class UserRepo:
    db = db

    async def get_user(self, username: str) -> Optional[UserModel]:
        user = await self.db['users'].find_one({'username': username})
        return UserModel(**user) if user is not None else user


    async def create_user(self, user: UserModel) -> UserModel:
        insert_result = await self.db['users'].insert_one(user.dict())
        logger.info(f'created user username={user.username} with id={insert_result.inserted_id} ')
        data = await db['users'].find_one({'_id': insert_result.inserted_id})
        return UserModel(**data)
