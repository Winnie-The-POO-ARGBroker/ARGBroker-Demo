import mysql.connector

class GestorDB:
    def connect(self):
        try:
            conexion = mysql.connector.connect(
                host="bntfytnw6iyhnscbbysh-mysql.services.clever-cloud.com",
                user="uryn6gsp8xxtqtx8",
                password="5XkCTptUFnSHg8DQribd",
                database="bntfytnw6iyhnscbbysh"
            )
            return conexion
        except mysql.connector.Error as e:
            print(f"Error conectando a la base de datos: {e}")
            return None
