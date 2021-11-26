import motor
from settings import settings
from loguru import logger


# Initalize database connection
client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URL)
db = client.college
logger.info('Database initialization completed!')
