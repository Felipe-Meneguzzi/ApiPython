from repositories.BaseRepository import BaseRepository
from entities.UserEntity import UserEntity 
from enums.UserTypeEnum import UserTypeEnum

class UserRepository(BaseRepository):
    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        users = []
        for row in rows:
            user = UserEntity(
                name=row['name'],
                password=row['password'],
                user_type=UserTypeEnum.from_value(row['user_type']),
                active=row['active'],
                id=row['id'],
            )
            users.append(user)
        return users
    
    def get_user_by_id(self, user_id: int):
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = self.cursor.fetchone()
        if row:
            return UserEntity(
                name=row['name'],
                password=row['password'],
                user_type=UserTypeEnum.from_value(row['user_type']),
                active=row['active'],
                id=row['id'],
            )
        return None
    
    def create_user(self, user: UserEntity):
        self.cursor.execute("INSERT INTO users (name, password, user_type, active) VALUES (?, ?, ?, ?)",
                            (user.name, user.password, user.user_type, user.active))
