class Inversor:
    def __init__(self, nombre, apellido, cuil, email, contrasena, saldo=1000000.00):
        self.nombre = nombre
        self.apellido = apellido
        self.cuil = cuil
        self.email = email
        self.contrasena = contrasena
        self.saldo = saldo
        self.portafolio = []

    def mostrar_datos_cuenta(self):
        return {
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "CUIL": self.cuil,
            "Saldo": f"${self.saldo:,.2f}"
        }

    def actualizar_saldo(self, monto):
        self.saldo += monto

    def agregar_accion_al_portafolio(self, accion):
        self.portafolio.append(accion)

    def listar_portafolio(self):
        return self.portafolio
