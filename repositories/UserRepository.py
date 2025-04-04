from repositories.BaseRepository import BaseRepository
from entities.UserEntity import UserEntity
from enums.UserTypeEnum import UserTypeEnum


class UserRepository(BaseRepository):
    def map_row_to_user_entity(self, row) -> UserEntity:
        if row is None:
            return None
        return UserEntity(
            name=row['name'],
            login=row['login'],
            password=row['password'],
            user_type=UserTypeEnum.from_value(row['user_type']),
            active=row['active'],
            id=row['id'],
        )

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        users = []
        for row in rows:
            user = self.map_row_to_user_entity(row)
            users.append(user)
        return users

    def get_user_by_id(self, user_id: int):
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = self.cursor.fetchone()
        return self.map_row_to_user_entity(row)

    def get_user_by_login(self, login: str):
        self.cursor.execute("SELECT * FROM users WHERE login like ?", (login,))
        row = self.cursor.fetchone()
        return self.map_row_to_user_entity(row)

    def create_user(self, user: UserEntity):
        self.cursor.execute("INSERT INTO users (name, login, password, user_type, active) VALUES (?, ?, ?, ?, ?)",
                            (user.name, user.login, user.password, user.user_type, user.active))
        user.id = self.cursor.lastrowid
        return user
