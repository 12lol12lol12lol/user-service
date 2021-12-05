from db import db
from models import CardCollection


class CardCollectionRepo:
    db = db

    async def create_card_collection(self, card_collection: CardCollection) -> CardCollection:
        pass
    
