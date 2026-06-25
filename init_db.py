import psycopg2
from helpers.application import app 
from helpers.enviroment import enviroment
from helpers.logger import logger

DATABASE_NAME = enviroment.get("DB_NAME")
DATABASE_USER = enviroment.get("DB_USER")
DATABASE_PASS = enviroment.get("DB_PASSWORD")
DATABASE_PORT = enviroment.get("DB_PORT")
DATABASE_HOST = enviroment.get("DB_HOST")

try:
    conn = psycopg2.connect(
        database=DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASS,
        host=DATABASE_HOST, port=DATABASE_PORT
    )
    cursor = conn.cursor()
    with open('schema.sql', mode='r') as file:
        cursor.execute(file.read())
    conn.commit()
    logger.info("Tabela tb_galinaceos criada com sucesso no PostgreSQL!")
except psycopg2.Error as e:
    logger.error(f"Erro de Banco de Dados: {e}")
finally:
    if 'conn' in locals() and conn:
        conn.close()