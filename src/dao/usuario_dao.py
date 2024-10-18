import mysql.connector
import bcrypt
from models.usuario import Usuario

class UsuarioDAO:
    def __init__(self, conexion):
        self.conexion = conexion

    # INSERTAR NUEVO USUARIO EN LA BD
    def insertar(self, usuario):
        # Genera el hash de la contraseña solo si es un string
        if isinstance(usuario.contrasena, str):
            hashed = bcrypt.hashpw(usuario.contrasena.encode('utf-8'), bcrypt.gensalt())
        else:
            hashed = usuario.contrasena  # La contraseña ya está hasheada en bytes

        try:
            with self.conexion.cursor() as cursor:
                consulta = """
                INSERT INTO usuarios (nombre, apellido, cuil, email, contrasena, saldo, total_invertido, rendimiento_total)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(consulta, (usuario.nombre, usuario.apellido, usuario.cuil, usuario.email, hashed, 1000000, 0, 0))
            self.conexion.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error al insertar usuario: {err}")
            return False


    # VERIFICAR MAIL EXISTENTE
    def obtener_por_email(self, email):
        with self.conexion.cursor() as cursor:
            query = "SELECT * FROM usuarios WHERE email = %s"
            cursor.execute(query, (email,))
            resultado = cursor.fetchone()

            if resultado:
                return Usuario(
                    resultado[0],
                    resultado[1],
                    resultado[2],
                    resultado[3],
                    resultado[4],
                    resultado[5].encode('utf-8'),  # Convertimos el hash a bytes
                    resultado[6],
                    resultado[7],
                    resultado[8],
                    resultado[9],  # intentos_fallidos
                    resultado[10]  # bloqueado
                )
        return None

    # VERIFICAR CONTRASEÑA
    def verificar_contrasena(self, email, contrasena_ingresada):
        usuario = self.obtener_y_verificar_bloqueo(email)
        if usuario:
            print(f"Hash almacenado: {usuario.contrasena.decode('utf-8')}")
            print(f"Contraseña ingresada: {contrasena_ingresada}")

            es_correcta = bcrypt.checkpw(contrasena_ingresada.encode('utf-8'), usuario.contrasena)
            print(f"La contraseña es {'correcta' if es_correcta else 'incorrecta'}.")
            return es_correcta
        return False


    # ACTUALIZAR INTENTOS Y BLOQUEAR USUARIO
    def actualizar_intentos(self, usuario):
        try:
            with self.conexion.cursor() as cursor:
                query = """
                    UPDATE usuarios 
                    SET intentos_fallidos = %s, bloqueado = %s 
                    WHERE email = %s
                """
                bloqueado = usuario.intentos_fallidos >= 3
                cursor.execute(query, (usuario.intentos_fallidos, bloqueado, usuario.email))
                self.conexion.commit()
        except mysql.connector.Error as err:
            print(f"Error al actualizar intentos: {err}")

    # BLOQUEAR USUARIO
    def bloquear_usuario(self, usuario):
        self.actualizar_intentos(usuario)  # Llama a actualizar_intentos para bloquear si es necesario

    def obtener_y_verificar_bloqueo(self, email):
        usuario = self.obtener_por_email(email)
        if usuario and usuario.bloqueado:
            print("La cuenta está bloqueada. No se puede iniciar sesión.")
            return None
        return usuario
    
    def obtener_datos_cuenta(self, usuario_id):
        with self.conexion.cursor() as cursor:
            query = """
            SELECT nombre, apellido, cuil, email, saldo, total_invertido, rendimiento_total 
            FROM usuarios 
            WHERE id = %s
            """
            cursor.execute(query, (usuario_id,))
            resultado = cursor.fetchone()
            return resultado

    def calcular_total_invertido(self, usuario_id, conexion):
        try:
            with conexion.cursor() as cursor:
                # Selecciona todas las transacciones de tipo 'compra' del usuario
                query = """
                SELECT cantidad, precio 
                FROM transacciones 
                WHERE id_usuario = %s AND tipo = 'compra'  # Asegúrate de que sea id_usuario
                """
                cursor.execute(query, (usuario_id,))
                transacciones = cursor.fetchall()

                # Calcula el total invertido sumando (cantidad * precio) para cada transacción
                total_invertido = sum(cantidad * precio for cantidad, precio in transacciones)
                return total_invertido
        except mysql.connector.Error as err:
            print(f"Error al calcular el total invertido: {err}")
            return 0
    
    def actualizar_total_invertido(self, usuario_id, nuevo_total):
        try:
            with self.conexion.cursor() as cursor:
                query = """
                UPDATE usuarios
                SET total_invertido = %s
                WHERE id = %s
                """
                cursor.execute(query, (nuevo_total, usuario_id))
                self.conexion.commit()  # Asegúrate de hacer commit para guardar los cambios
                print("Total invertido actualizado correctamente.")
        except Exception as e:
            print(f"Error al actualizar el total invertido: {e}")
