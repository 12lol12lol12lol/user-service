from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field

from .pyobject_id import PyObjectId


class UserModel(BaseModel):  # pylint: disable=too-few-public-methods
    """
    User model for database
    """
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    created_at: datetime = Field(default=datetime.now())
    last_login: Optional[datetime] = Field(default=datetime.now())
    is_admin: bool = Field(default=False)

    class Config:  # pylint: disable=too-few-public-methods
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example': {
                'username': 'MyUsername',
                'email': 'my@email.com',
                'created_at': '1996-02-01T00:00:00',
                'last_login': '1996-02-01T00:00:00',
                'is_admin': 'false'

            }
        }


class UserSignUpModel(BaseModel):
    """
    User model for validate sign up data
    """
    username: str = Field(..., min_length=3, max_length=100)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=6)
