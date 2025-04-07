import jwt
import entities.UserEntity as UserEntity
from datetime import datetime, timedelta

SECRET_KEY: str = "vamo_vamo_inter_2006"
ALGORITHM: str = "HS256"
MINUTES_TO_EXPIRE: int = 5


def create_token(user: UserEntity):
    info = {
        "id": user.id,
        "name": user.name,
        "login": user.login,
        "user_type": user.user_type,
        "active": user.active,
        "exp": datetime.utcnow() + timedelta(minutes=MINUTES_TO_EXPIRE)
    }
    token = jwt.encode(payload=info, key=SECRET_KEY, algorithm=ALGORITHM)
    return token


def decode_token(token: str):
    try:
        info = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        return info
    except jwt.ExpiredSignatureError:
        return "E"
    except jwt.InvalidTokenError:
        return "I"
