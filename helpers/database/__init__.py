import psycopg2
from flask import g
from helpers.application import app
from helpers.enviroment import enviroment

def get_conn():
    conn = getattr(g, '_database', None)
    if conn is None:
        conn = g._database = psycopg2.connect(
            database=enviroment.get("DB_NAME"),
            user=enviroment.get("DB_USER"),
            password=enviroment.get("DB_PASSWORD"),
            host=enviroment.get("DB_HOST"),
            port=enviroment.get("DB_PORT")
        )
    return conn

@app.teardown_appcontext
def close_connection(exception):
    conn = getattr(g, '_database', None)
    if conn is not None:
        conn.close()