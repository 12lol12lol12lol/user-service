import secrets
from .hash import get_hashed_password, check_password


def test_check_password():
    rand_str = secrets.token_hex(nbytes=16)
    hashed_pwd = get_hashed_password(rand_str)
    assert check_password(rand_str, hashed_pwd) is True
