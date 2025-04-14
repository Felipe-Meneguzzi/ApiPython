from src.utils.DbConnectionScript import get_db_connection
import os
import mariadb
from dotenv import load_dotenv


load_dotenv()


def run_rollbacks():

    rollbacks_path = os.path.join(os.path.dirname(__file__), "rollbacks")

    connection = get_db_connection()

    cursor = connection.cursor()

    # Listar arquivos de rollbacks em ordem
    rollbacks = sorted(
        f for f in os.listdir(rollbacks_path) if f.endswith(".sql")
    )

    for rollback in rollbacks:
        rollback_file = os.path.join(rollbacks_path, rollback)

        try:
            # Ler o conteúdo do arquivo SQL
            with open(rollback_file, "r", encoding="utf-8") as file:
                sql_script = file.read()

            # Executar o script SQL
            for statement in sql_script.split(";"):
                if statement.strip():
                    cursor.execute(statement)

            connection.commit()
            print(f"Rollback {rollback} executada com sucesso.")

        except mariadb.Error as e:
            print(f"Erro ao executar a rollback {rollback}: {e}")

    if connection:
        connection.close()
        print("Conexão com o banco de dados encerrada.")


if __name__ == "__main__":
    run_rollbacks()
