from src.valueObjects.AuthTokenObject import create_token, decode_token
from src.entities.UserEntity import UserEntity

new_user = UserEntity(id=1, name="Lucas", login="lucas",
                      password="123456", user_type=1, active=True)

print(new_user.model_dump())
token = create_token(new_user)
print(token)
print(decode_token(token+"12"))
