import os
import sys

from pydantic.error_wrappers import ValidationError
from .settings import Settings
from loguru import logger

# Initialize settings class
def init_settings() -> Settings:
    try:
        settings = Settings(
            MONGODB_URL=os.environ.get('MONGODB_URL'),
            SECRET_KEY=os.environ.get('SECRET_KEY'),
            TOKEN_EXPIRED=os.environ.get('TOKEN_EXPIRED'),
        )
    except ValidationError as e:
        sys.exit(str(e))

    for key, value in settings.dict().items():
        logger.info(f'{key} = {value}')
    return settings
