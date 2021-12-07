from typing import List, Optional

from bson.objectid import ObjectId
from models.user.pyobject_id import PyObjectId
from pydantic import BaseModel
from pydantic.fields import Field
from pydantic.types import FilePath


class CardModel(BaseModel):
    """
    Model for card
    """
    name: str = Field(...)
    description: str = Field(...)
    image: Optional[FilePath] = Field(default_factory=None)
    population: int = Field(default_factory=10)

    class Config:  # pylint: disable=too-few-public-methods
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            'example': {
                'name': 'Card name',
                'description': 'Card description',
                'image': '/home/static/img.png',
                'population': 10
            }
        }


class CardCollectionModel(BaseModel):
    """
    Model for card collections
    """
    name: str = Field(...)
    description: Optional[str] = Field(default_factory=None)
    image: Optional[FilePath] = Field(default_factory=None)
    population: int = Field(default_factory=10)
    cards: List[CardModel] = Field(default_factory=list)

    class Config:  # pylint: disable=too-few-public-methods
        schema_extra = {
            'example': {
                'name': 'Collection name',
                'description': 'Collection description',
                'image': '/file/path',
                'population': 10,
                'cards': [
                    {
                        'name': 'Card name',
                        'description': 'Card description',
                        'image': '/home/static/img.png',
                        'population': 10
                    }
                ]

            }
        }


class CardCollectionCreateModel(CardCollectionModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config(CardCollectionModel.Config):  # pylint: disable=too-few-public-methods
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
