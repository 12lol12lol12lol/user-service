"""
Card collection route definitions
"""
from fastapi import APIRouter, Depends
from loguru import logger
from models import CardCollectionModel, User
from services import user_is_admin

collection_router = APIRouter()


@collection_router.post("/collection")
async def create_collection(collection: CardCollectionModel, user: User = Depends(user_is_admin)):
    logger.info(collection)
    logger.info(user)
    return {}
