import mysql.connector
from models.accion import Accion
<<<<<<< HEAD
=======
from decimal import Decimal
>>>>>>> Magali

class AccionDAO:
    def __init__(self, conexion):
        self.conexion = conexion

<<<<<<< HEAD
    def obtener_acciones(self):
        activos = []
        try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM activos")
            rows = cursor.fetchall()
            for row in rows:
                activo = Accion(row[1], row[2], row[3])  # Asumiendo que el orden de las columnas es correcto
=======
    def obtener_por_nombre(self, nombre_empresa):
        cursor = self.conexion.cursor()
        query = """
            SELECT id, simbolo, nombre_empresa, ultimo_operado, cantidad_compra_diaria, 
                   precio_compra, precio_venta, cantidad_venta_diaria, apertura, 
                   minimo_diario, maximo_diario, ultimo_cierre
            FROM acciones 
            WHERE nombre_empresa = %s
        """
        cursor.execute(query, (nombre_empresa,))
        result = cursor.fetchone()

        if result:
            return Accion(
                id=result[0],
                simbolo=result[1],
                nombre_empresa=result[2],
                ultimo_operado=Decimal(result[3]),
                cantidad_compra_diaria=result[4],
                precio_compra=Decimal(result[5]),
                precio_venta=Decimal(result[6]),
                cantidad_venta_diaria=result[7],
                apertura=Decimal(result[8]),
                minimo_diario=Decimal(result[9]),
                maximo_diario=Decimal(result[10]),
                ultimo_cierre=Decimal(result[11])
            )
        else:
            return None

    def obtener_precio_actual_compra(self, nombre_empresa):
        try:
            cursor = self.conexion.cursor(dictionary=True)
            query = "SELECT precio_compra FROM acciones WHERE nombre_empresa = %s"
            cursor.execute(query, (nombre_empresa,))
            resultado = cursor.fetchone()

            if resultado:
                return Decimal(resultado['precio_compra'])
            else:
                raise ValueError(f"No se encontró el activo {nombre_empresa} en la base de datos.")
        
        except mysql.connector.Error as e:
            print(f"Error al obtener el precio de compra: {e}")
        finally:
            cursor.close()

    def obtener_precio_actual_venta(self, nombre_empresa):
        try:
            cursor = self.conexion.cursor(dictionary=True)
            query = "SELECT precio_venta FROM acciones WHERE nombre_empresa = %s"
            cursor.execute(query, (nombre_empresa,))
            resultado = cursor.fetchone()

            if resultado:
                return Decimal(resultado['precio_venta'])
            else:
                raise ValueError(f"No se encontró el activo {nombre_empresa} en la base de datos.")
        
        except mysql.connector.Error as e:
            print(f"Error al obtener el precio de venta: {e}")
        finally:
            cursor.close()

    def obtener_acciones(self):
        """Obtiene todas las acciones de la base de datos."""
        activos = []
        try:
            cursor = self.conexion.cursor()
            query = """
                SELECT id, simbolo, nombre_empresa, ultimo_operado, cantidad_compra_diaria, 
                       precio_compra, precio_venta, cantidad_venta_diaria, apertura, 
                       minimo_diario, maximo_diario, ultimo_cierre
                FROM acciones
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                activo = Accion(
                    id=row[0],
                    simbolo=row[1],
                    nombre_empresa=row[2],
                    ultimo_operado=Decimal(row[3]),
                    cantidad_compra_diaria=row[4],
                    precio_compra=Decimal(row[5]),
                    precio_venta=Decimal(row[6]),
                    cantidad_venta_diaria=row[7],
                    apertura=Decimal(row[8]),
                    minimo_diario=Decimal(row[9]),
                    maximo_diario=Decimal(row[10]),
                    ultimo_cierre=Decimal(row[11])
                )
>>>>>>> Magali
                activos.append(activo)
            return activos
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        finally:
            cursor.close()
<<<<<<< HEAD
    
    def actualizar_accion(self, accion):
        pass
=======

    def insertar_accion(self, accion):
        """Inserta una nueva acción en la base de datos."""
        cursor = self.conexion.cursor()
        query = """
            INSERT INTO acciones (simbolo, nombre_empresa, ultimo_operado, cantidad_compra_diaria, 
                                  precio_compra, precio_venta, cantidad_venta_diaria, apertura, 
                                  minimo_diario, maximo_diario, ultimo_cierre)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (
                accion.simbolo,
                accion.nombre_empresa,
                accion.ultimo_operado,
                accion.cantidad_compra_diaria,
                accion.precio_compra,
                accion.precio_venta,
                accion.cantidad_venta_diaria,
                accion.apertura,
                accion.minimo_diario,
                accion.maximo_diario,
                accion.ultimo_cierre
            ))
            self.conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error al insertar acción: {err}")
        finally:
            cursor.close()

    def actualizar_accion(self, accion):
        """Actualiza la información de una acción existente en la base de datos."""
        cursor = self.conexion.cursor()
        query = """
            UPDATE acciones 
            SET nombre_empresa = %s, ultimo_operado = %s, cantidad_compra_diaria = %s, 
                precio_compra = %s, precio_venta = %s, cantidad_venta_diaria = %s, 
                apertura = %s, minimo_diario = %s, maximo_diario = %s, ultimo_cierre = %s
            WHERE simbolo = %s
        """
        try:
            cursor.execute(query, (
                accion.nombre_empresa,
                accion.ultimo_operado,
                accion.cantidad_compra_diaria,
                accion.precio_compra,
                accion.precio_venta,
                accion.cantidad_venta_diaria,
                accion.apertura,
                accion.minimo_diario,
                accion.maximo_diario,
                accion.ultimo_cierre,
                accion.simbolo
            ))
            self.conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error al actualizar acción: {err}")
        finally:
            cursor.close()
>>>>>>> Magali
