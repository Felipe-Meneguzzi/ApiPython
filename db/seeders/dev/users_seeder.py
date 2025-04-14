from dotenv import load_dotenv
import mariadb
import random
from src.utils.DbConnectionScript import get_db_connection
from faker import Faker

fake = Faker('pt_BR')

try:

    connection = get_db_connection()
    cursor = connection.cursor()

    sql_query = "INSERT INTO users (id,name,password,user_type,active,login) VALUES"

    cursor.execute(
        sql_query + "(1,'Admin','$2b$12$rkhNoWhPez3Le8GgxDfe9OXVDg3LaBgYqNVISJQpnP88hNp0q1a6.',1,1,'admin')")

    for entry in range(99):
        dados = (
            f"({entry+2}, '{fake.name()}', '{fake.password()}', {random.randint(1, 3)}, {random.randint(0, 1)}, '{fake.user_name()}')")
        cursor.execute(
            sql_query + dados)

    connection.commit()

except mariadb.Error as e:
    print(f"Erro ao executar o seeder da tabela users: {e}")
    connection.rollback()

if connection:
    connection.close()
    print("Conexão com o banco de dados encerrada.")
