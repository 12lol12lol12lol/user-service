from pydantic import BaseModel, Field, EmailStr
from models import PyObjectId
from datetime import datetime
from typing import Optional

class UserModel(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    created_at: datetime = Field(default=datetime.now())
    last_login: Optional[datetime] = Field(default=None)
    is_admin: bool = Field(default=False)


class UserSignUpModel(BaseModel):
    """
    
    """
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)