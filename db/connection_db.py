import psycopg2
from psycopg2 import OperationalError

def create_connection(**db_config):
    try:
        connection = psycopg2.connect(**db_config)
        cursor = connection.cursor()
        print("Connection success")
        return connection, cursor
    except OperationalError as e:
        print(f"Error '{e}' ")
        return None, None
