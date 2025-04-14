from dotenv import load_dotenv
from src.utils.DbConnectionScript import get_db_connection

load_dotenv()


class DatabaseConnection:
    _instance = None  # Atributo de classe para armazenar a instancia unica

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Evita reexecutar o __init__ em chamadas subsequentes
        if not hasattr(self, "connection"):
            self.connection = None
            self.connect()

    def connect(self):
        self.connection = get_db_connection()

    def get_connection(self):
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
        else:
            print("No connection to close.")
