from dataclasses import dataclass
from typing import Tuple
from models import UserSignUpModel, UserModel


@dataclass
class SignUpUserService:
    """
    Service for user sign up logic

    main method is run().
    run() return (status: bool, message: str)
    if user successfully registered return (True, '')
    else return (False, 'error message')
    """
    user: UserSignUpModel

    async def run(self) -> Tuple[bool, str]:
        if self.user is None:
            return False, 'user is None'
        

        

