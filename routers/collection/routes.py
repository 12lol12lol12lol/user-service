"""
Card collection route definitions
"""
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.datastructures import UploadFile
from loguru import logger
from models import CardCollectionModel, User
from services import user_is_admin

collection_router = APIRouter()


@collection_router.post("/collection")
async def create_collection(collection: CardCollectionModel, user: User = Depends(user_is_admin)):
    logger.info(collection)
    logger.info(user)
    return {}


@collection_router.post("/collection/image")
async def upload_card_image(file: UploadFile = File(...), user: User = Depends(user_is_admin)):
    logger.info(file.filename)
    logger.info(user)
    return {}
