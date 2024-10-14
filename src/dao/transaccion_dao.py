<<<<<<< HEAD
class TransaccionDAO:
    def __init__(self):
        self.transacciones = []

    def registrar_transaccion(self, transaccion):
        self.transacciones.append(transaccion)

    def listar_transacciones(self, inversor):
        return [t for t in self.transacciones if t.inversor == inversor]
=======
import mysql

class TransaccionDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def registrar_transaccion(self, transaccion):
        cursor = self.conexion.cursor()
        query = """
        INSERT INTO transacciones (usuario_id, accion_id, tipo, cantidad, precio, comision)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (
            transaccion.usuario_id,
            transaccion.accion_id,
            transaccion.tipo,
            transaccion.cantidad,
            transaccion.precio,
            transaccion.comision
        )
        try:
            cursor.execute(query, valores)
            self.conexion.commit()
            print("Transacción registrada exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al registrar la transacción: {err}")
        finally:
            cursor.close()
>>>>>>> Magali
