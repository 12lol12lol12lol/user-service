from datetime import datetime, timedelta

from fastapi import HTTPException, status
from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordBearer
from jose import jwt
from jose.exceptions import JWTError
from loguru import logger
from models import TokenData, User
from repository.user import UserRepo
from settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: timedelta) -> str:
    """Create access token for user

    Args:
        data (dict): Data that put in token, default is sub
        expires_delta (timedelta): Expired time for token

    Returns:
        (str): JWT token for user
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({'exp': expire})
    encode_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encode_jwt

async def check_user_token(token: str = Depends(oauth2_scheme)) -> User:
    """Check user token

    Args:
        token (str, optional): User token in oauth2 form. Defaults to Depends(oauth2_scheme).

    Raises:
        credentials_exception: raise unathorized exception

    Returns:
        User: return user model
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError as ex:
        raise credentials_exception from ex
    user = await UserRepo.get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def user_is_admin(token: str = Depends(oauth2_scheme)) -> User:
    """Check user rights

    Args:
        token (str, optional):  Defaults to Depends(oauth2_scheme).

    Raises:
        forbidden_exception: 403 exception if user is not admin

    Returns:
        User: return user model
    """
    forbidden_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Not enough rights",
        headers={"WWW-Authenticate": "Bearer"},
    )
    user = await check_user_token(token)
    logger.info(user)
    if not user.is_admin:
        raise forbidden_exception
    return user
