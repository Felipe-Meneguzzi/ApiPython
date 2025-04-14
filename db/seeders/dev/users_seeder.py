import mariadb
import random
from src.utils.DbConnectionScript import get_db_connection
from src.utils.PasswordScript import generate_hash
from faker import Faker


fake = Faker('pt_BR')

try:

    connection = get_db_connection()
    cursor = connection.cursor()

    sql_query = "INSERT INTO users (name,password,user_type,active,login) VALUES (%s, %s, %s, %s, %s)"

    cursor.execute(
        sql_query, ('Admin', '$2b$12$rkhNoWhPez3Le8GgxDfe9OXVDg3LaBgYqNVISJQpnP88hNp0q1a6.', 1, 1, 'admin'))

    for entry in range(99):
        name = fake.name()
        login = fake.user_name()
        password = generate_hash(login)
        user_type = random.randint(1, 3)
        active = random.randint(0, 1)

        cursor.execute(sql_query, (name, password, user_type, active, login))

    connection.commit()
    print("users seeder executado com sucesso.")

except mariadb.Error as e:
    print(f"Erro ao executar users seeder: {e}")
    connection.rollback()

if connection:
    connection.close()
    print("Conexão com o banco de dados encerrada.")
