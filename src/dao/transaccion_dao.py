import mysql.connector

class TransaccionDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def registrar_transaccion(self, transaccion, usuario_dao):
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

            # Actualizar total invertido si es una compra
            if transaccion.tipo == 'compra':
                self.actualizar_total_invertido(transaccion.usuario_id, transaccion.cantidad, transaccion.precio)

            # Actualizar rendimiento total
            usuario_dao.actualizar_rendimiento_total(transaccion.usuario_id)

        except mysql.connector.Error as err:
            print(f"Error al registrar la transacción: {err}")
        finally:
            cursor.close()
