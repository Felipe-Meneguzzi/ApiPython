import jwt
import src.entities.UserEntity as UserEntity
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os


load_dotenv()


SECRET_KEY: str = "vamo_vamo_inter_2006"
ALGORITHM: str = "HS256"
MINUTES_TO_EXPIRE: int = int(os.getenv("TOKEN_DURATION"))


def create_token(user: UserEntity):
    info = {
        "user": user.model_dump(),
        "exp": datetime.now(timezone.utc) + timedelta(minutes=MINUTES_TO_EXPIRE)
    }
    token = jwt.encode(payload=info, key=SECRET_KEY, algorithm=ALGORITHM)
    return token


def decode_token(token: str):
    try:
        info = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        return dict(info)
    except jwt.ExpiredSignatureError:
        return str("E")
    except jwt.InvalidTokenError:
        return str("I")
