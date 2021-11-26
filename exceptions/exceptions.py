class BaseException(Exception):
    """
    Базовое исключение
    """
    exception_type = ""

    def __init__(self, *args, **kwargs) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None

    def get_message(self):
        return [
            {
                'msg': self.message,
                'type': self.exception_type
            }
        ]
