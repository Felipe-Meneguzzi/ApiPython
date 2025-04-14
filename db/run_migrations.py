from src.utils.DbConnectionScript import get_db_connection
import os
import mariadb
from dotenv import load_dotenv


load_dotenv()


def run_migrations():

    migrations_path = os.path.join(os.path.dirname(__file__), "migrations")

    connection = get_db_connection()
    cursor = connection.cursor()

    # Listar arquivos de migrations em ordem
    migrations = sorted(
        f for f in os.listdir(migrations_path) if f.endswith(".sql")
    )

    for migration in migrations:
        migration_file = os.path.join(migrations_path, migration)

        try:
            # Ler o conteúdo do arquivo SQL
            with open(migration_file, "r", encoding="utf-8") as file:
                sql_script = file.read()

            # Executar o script SQL
            for statement in sql_script.split(";"):
                if statement.strip():
                    cursor.execute(statement)

            connection.commit()
            print(f"Migration {migration} executada com sucesso.")

        except mariadb.Error as e:
            print(f"Erro ao executar a migration {migration}: {e}")

    if connection:
        connection.close()
        print("Conexão com o banco de dados encerrada.")


if __name__ == "__main__":
    run_migrations()
