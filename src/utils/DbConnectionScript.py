import os
import mariadb
from dotenv import load_dotenv

load_dotenv()

db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "port": int(os.getenv("DB_PORT")),
}


def get_db_connection():
    try:
        connection = mariadb.connect(**db_config)
        print("Conexão com o banco de dados estabelecida.")
        return connection
    except mariadb.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
