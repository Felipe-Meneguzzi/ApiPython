import mariadb
import os
from dotenv import load_dotenv

load_dotenv()


class DatabaseConnection:
    _instance = None  # Atributo de classe para armazenar a instância única

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
        print(os.getenv("DB_HOST"),
              os.getenv("DB_USER"),
              os.getenv("DB_PASSWORD"),
              os.getenv("DB_NAME"),
              os.getenv("DB_PORT"))
        try:
            self.connection = mariadb.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME"),
                port=int(os.getenv("DB_PORT"))
            )
            print("Database connection established successfully.")
        except mariadb.Error as err:
            print("Error connecting to MariaDB Platform: ", err)
            exit(1)

    def get_connection(self):
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
        else:
            print("No connection to close.")
