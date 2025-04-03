from dbConnection import DatabaseConnection

class BaseRepository:
    def __init__(self):
        self.db_connection = DatabaseConnection()  
        self.connection = self.db_connection.get_connection()
        self.cursor = self.connection.cursor(dictionary=True)

