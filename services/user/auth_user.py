from db import db

from .hash import check_password


async def get_user(username: str):
    return await db['users'].find_one({'username': username})

async def auth_user(username: str, password: str):
    user = await get_user(username)
    if user is None:
        return False
    if not check_password(password, user.password):
        return False
    return user
