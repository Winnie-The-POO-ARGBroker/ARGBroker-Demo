import mysql.connector
from models.usuario import Usuario

class UsuarioDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def insertar(self, usuario):
        try:
            cursor = self.conexion.cursor()
            sql = """
            INSERT INTO usuarios 
            (nombre, apellido, cuil, email, contrasena, saldo, total_invertido, rendimiento_total) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (usuario.nombre, usuario.apellido, usuario.cuil, usuario.email, usuario.contrasena, usuario.saldo, usuario.total_invertido, usuario.rendimiento_total)
            cursor.execute(sql, valores)
            self.conexion.commit()
            print("Usuario registrado exitosamente.")
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
        finally:
            cursor.close()

    def obtener_por_email(self, email):
        try:
            # Usamos MySQLCursorDict para devolver los resultados como diccionario
            cursor = self.conexion.cursor(dictionary=True)
            cursor.execute("SELECT nombre, apellido, cuil, email, contrasena, saldo, total_invertido, rendimiento_total FROM usuarios WHERE email = %s", (email,))
            row = cursor.fetchone()
            
            if row:
                # Ahora accedemos a los valores usando los nombres de las columnas
                return Usuario(
                    row['nombre'], 
                    row['apellido'], 
                    row['cuil'], 
                    row['email'], 
                    row['contrasena'], 
                    row['saldo'], 
                    row['total_invertido'], 
                    row['rendimiento_total']
                )
            return None
        except Exception as e:
            print(f"Error al obtener usuario por email: {e}")
            return None
        finally:
            cursor.close()


    def actualizar_usuario(self, usuario):
        try:
            cursor = self.conexion.cursor()
            sql = """
            UPDATE usuarios 
            SET saldo = %s, total_invertido = %s, rendimiento_total = %s 
            WHERE email = %s
            """
            valores = (usuario.saldo, usuario.total_invertido, usuario.rendimiento_total, usuario.email)
            cursor.execute(sql, valores)
            self.conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
