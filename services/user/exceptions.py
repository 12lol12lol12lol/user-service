from exceptions import BaseException


class UserServiceException(BaseException):
    exception_type = "user_service_exception"
