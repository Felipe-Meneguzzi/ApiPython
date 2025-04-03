from enum import Enum

class UserTypeEnum(Enum):
    ADMIN = 1
    COMMON = 2
    SPECTATOR = 3

    @classmethod
    def from_value(cls, value):
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"No UserTypeEnum found for value: {value}")

    def portuguese(self):
        translations = {
            UserTypeEnum.ADMIN: "Administrador",
            UserTypeEnum.COMMON: "Comum",
            UserTypeEnum.SPECTATOR: "Espectador"
        }
        return translations[self]
    
    def english(self):
        translations = {
            UserTypeEnum.ADMIN: "Administrator",
            UserTypeEnum.COMMON: "Common",
            UserTypeEnum.SPECTATOR: "Spectator"
        }
        return translations[self]
    