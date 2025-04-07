from repositories.BaseRepository import BaseRepository
from entities.UserEntity import UserEntity
from enums.UserTypeEnum import UserTypeEnum
from valueObjects.PageObject import PageObject


class UserRepository(BaseRepository):
    table_name = 'users'
    primary_key = 'id'

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

    def get_total_count(self):
        query = f"SELECT COUNT(*) AS total_count FROM {self.table_name}"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result["total_count"] if result else 0

    def get_all_users(self, page_obj: PageObject):
        page_obj = page_obj or PageObject()

        params = []
        where_clauses = []

        # Filtros
        if page_obj.filters:
            for field, value in page_obj.filters.items():
                where_clauses.append(f"{field} = ?")
                params.append(value)

        # Busca (search em múltiplos campos com LIKE)
        if page_obj.search:
            for field, value in page_obj.search.items():
                where_clauses.append(f"{field} LIKE ?")
                params.append(f"%{value}%")

        # Monta cláusula WHERE
        where_sql = ""
        if where_clauses:
            where_sql = " WHERE " + " AND ".join(where_clauses)

        # Ordenação
        sort_column = page_obj.sort or "id"
        sort_direction = page_obj.sort_direction.upper() if page_obj.sort_direction else "ASC"
        if sort_direction not in ("ASC", "DESC"):
            sort_direction = "ASC"

        # Paginação
        limit = page_obj.page_size or 10
        offset = ((page_obj.page or 1) - 1) * limit

        # Query final
        query = f"""
            SELECT * FROM {self.table_name}
            {where_sql}
            ORDER BY {sort_column} {sort_direction}
            LIMIT ? OFFSET ?
        """
        params.extend([limit, offset])

        self.cursor.execute(query, tuple(params))
        rows = self.cursor.fetchall()
        return [self.map_row_to_user_entity(row) for row in rows]

    def get_user_by_id(self, user_id: int):
        query = f"SELECT * FROM {self.table_name} WHERE id = ?"
        self.cursor.execute(query, (user_id,))
        row = self.cursor.fetchone()
        return self.map_row_to_user_entity(row) if row else None

    def get_user_by_login(self, login: str):
        query = f"SELECT * FROM {self.table_name} WHERE login = ?"
        self.cursor.execute(query, (login,))
        row = self.cursor.fetchone()
        return self.map_row_to_user_entity(row) if row else None

    def create_user(self, user: UserEntity):
        query = f"""
            INSERT INTO {self.table_name} (name, login, password, user_type, active)
            VALUES (?, ?, ?, ?, ?)
        """
        self.cursor.execute(query, (user.name, user.login,
                                    user.password, user.user_type, user.active))
        user.id = self.cursor.lastrowid
        return user
