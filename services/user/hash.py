import bcrypt


def get_hashed_password(plain_password: str) -> str:
    return bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def check_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(str.encode(plain_password), str.encode(hashed_password))
