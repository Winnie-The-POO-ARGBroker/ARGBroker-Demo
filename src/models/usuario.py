import bcrypt

class Usuario:
    def __init__(self, id, nombre, apellido, cuil, email, contrasena, saldo=0, total_invertido=0, rendimiento_total=0, intentos_fallidos=0, bloqueado=False):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cuil = cuil
        self.email = email
        self.saldo = saldo
        self.total_invertido = total_invertido
        self.rendimiento_total = rendimiento_total
        self.intentos_fallidos = intentos_fallidos
        self.bloqueado = bloqueado
        
        # Asigna la contraseña, si es un string la hashea
        if isinstance(contrasena, str):
            self.contrasena = self.hash_password(contrasena)
        else:
            self.contrasena = contrasena  # Asignar directamente si ya está en bytes

    @staticmethod
    def hash_password(password):
        """Hashea la contraseña y devuelve el hash en formato bytes."""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def check_password(self, password):
        """Compara una contraseña en texto plano con el hash almacenado."""
        return bcrypt.checkpw(password.encode('utf-8'), self.contrasena)

    def __repr__(self):
        """Representación legible del objeto Usuario."""
        return f"Usuario(id={self.id}, nombre={self.nombre}, apellido={self.apellido}, email={self.email})"
