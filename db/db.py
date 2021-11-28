import motor.motor_asyncio
from loguru import logger
from settings import settings

# Initalize database connection
client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URL)
db = client.college
logger.info('Database initialization completed!')
