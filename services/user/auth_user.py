from typing import Union

from models import UserModel

from .hash import check_password


async def auth_user(user_repo, username: str, password: str) -> Union[UserModel, bool]:
    user = await user_repo.get_user(username)
    if user is None:
        return False
    if not check_password(password, user.password):
        return False
    return user
