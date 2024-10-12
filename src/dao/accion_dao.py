import mysql.connector
from models.accion import Activo

class ActivoDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def obtener_acciones(self):
        activos = []
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM activos")
            rows = cursor.fetchall()
            for row in rows:
                activo = Activo(row[1], row[2], row[3])  # Asumiendo que el orden de las columnas es correcto
                activos.append(activo)
            return activos
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        finally:
            cursor.close()
    
    def actualizar_accion(self, accion):
        pass
