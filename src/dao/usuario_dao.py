import mysql.connector
import bcrypt
from models.usuario import Usuario

class UsuarioDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    def insertar(self, usuario):
        try:
            cursor = self.conexion.cursor()
            query = """
                INSERT INTO usuarios (nombre, apellido, cuil, email, contrasena)
                VALUES (%s, %s, %s, %s, %s)
            """
            # Aquí no hasheamos la contraseña porque ya debería estar hasheada en el objeto Usuario
            contrasena_hash = usuario.contrasena.decode('utf-8')  # Almacenamos el hash como string
            cursor.execute(query, (usuario.nombre, usuario.apellido, usuario.cuil, usuario.email, contrasena_hash))
            self.conexion.commit()  # Confirmar los cambios
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
        finally:
            cursor.close()

    def verificar_usuario(self, email):
        cursor = self.conexion.cursor()
        query = "SELECT saldo FROM usuarios WHERE email = %s"
        cursor.execute(query, (email,))
        saldo = cursor.fetchone()
        cursor.close()
        return saldo[0] if saldo else None

    def obtener_por_email(self, email):
        cursor = self.conexion.cursor()
        query = "SELECT * FROM usuarios WHERE email = %s"
        cursor.execute(query, (email,))
        resultado = cursor.fetchone()
        cursor.close()
        
        if resultado:
            return Usuario(
                resultado[0],
                resultado[1],
                resultado[2],
                resultado[3],
                resultado[4],
                resultado[5].encode('utf-8'),  # Convertimos el hash de vuelta a bytes
                resultado[6],
                resultado[7],
                resultado[8]
            )
        
        return None

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

    def verificar_contrasena(self, email, contrasena_ingresada):
        usuario = self.obtener_por_email(email)
        if usuario:
            # Compara la contraseña ingresada (convertida a bytes) con el hash almacenado (ya en bytes)
            if bcrypt.checkpw(contrasena_ingresada.encode('utf-8'), usuario.contrasena):
                return True  # La contraseña es correcta
            else:
                return False  # La contraseña es incorrecta
        return False  # El usuario no existe
