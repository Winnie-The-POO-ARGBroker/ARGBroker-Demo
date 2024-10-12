import mysql.connector

class GestorDB:
    def connect(self):
        try:
            conexion = mysql.connector.connect(
                host="127.0.0.1",  # Usa solo la IP o "localhost"
                user="root",  # Cambia esto por tu usuario de MySQL
                password="4413",  # Cambia esto por tu contraseña de MySQL
                database="ARGBroker"  # Cambia esto por el nombre de tu base de datos
            )
            return conexion
        except mysql.connector.Error as e:
            print(f"Error conectando a la base de datos: {e}")
            return None
