<<<<<<< HEAD
import mysql.connector

=======
import os
from dotenv import load_dotenv
import mysql.connector

# Cargar variables de entorno desde el archivo .env
load_dotenv()

>>>>>>> Magali
class GestorDB:
    def connect(self):
        try:
            conexion = mysql.connector.connect(
<<<<<<< HEAD
                host="bntfytnw6iyhnscbbysh-mysql.services.clever-cloud.com",
                user="uryn6gsp8xxtqtx8",
                password="5XkCTptUFnSHg8DQribd",
                database="bntfytnw6iyhnscbbysh"
=======
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
>>>>>>> Magali
            )
            return conexion
        except mysql.connector.Error as e:
            print(f"Error conectando a la base de datos: {e}")
            return None
