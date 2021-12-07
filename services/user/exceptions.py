from exceptions import AppException


class UserServiceException(AppException):
    exception_type = "user_service_exception"
