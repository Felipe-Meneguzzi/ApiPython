from enums.UserTypeEnum import UserTypeEnum
from pydantic import BaseModel
from typing import Optional


class UserEntity(BaseModel):
    name: str
    login: str
    password: str
    user_type: UserTypeEnum
    active: bool
    id: Optional[int] = None

    def __str__(self) -> str:
        return f"User(id={self.id}, name={self.name}, login={self.login}, password={self.password}, user_type={self.user_type}, active={bool(self.active)})"

    def model_dump(self, *args, **kwargs) -> dict:
        data = super().model_dump(*args, **kwargs)
        data.pop("password", None)
        return data

    class Config:
        use_enum_values = True  # Converte automaticamente enums para seus valores ao serializar
