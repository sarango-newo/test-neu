# main.py
from db.connection_db import create_connection
from db import querys_db
from functions import calculate_functions

def main():
    # Detalles de conexión
    db_config = {
        'dbname': 'test',
        'user': 'postgres',
        'password': 'admin',
        'host': 'localhost',
        'port': '5432',
    }

    # Mes a procesar
    mes = 9

    # Conexión a la base de datos
    connection, cursor = create_connection(**db_config)
    if connection:
        try:
            datos = querys_db.obtener_datos(cursor, mes)
            resultados = calculate_functions.calcular_factura_septiembre(datos)

            for id_service, valores in resultados.items():
                print(f"id_service: {id_service}")
                print(f"ea: {valores['ea']}")
                print(f"ee1: {valores['ee1']}")
                print(f"ee2: {valores['ee2']}")
                print(f"ec: {valores['ec']}")
                print()

        except Exception as e:
            print("Error:", e)

        finally:
            # Cerrar la conexión a la base de datos
            connection.close()

    else:
        print("No se pudo establecer la conexión a la base de datos.")


if __name__ == "__main__":
    main()