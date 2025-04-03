from enums.UserTypeEnum import UserTypeEnum
from pydantic import BaseModel

class UserEntity(BaseModel):
    id: int
    name: str
    password: str
    user_type: UserTypeEnum
    active: bool

    def __str__(self) -> str:
        return f"User(id={self.id}, name={self.name}, password={self.password}, user_type={self.user_type.portuguese()}, active={bool(self.active)})"
    
    class Config:
        use_enum_values = True  # Converte automaticamente enums para seus valores ao serializar