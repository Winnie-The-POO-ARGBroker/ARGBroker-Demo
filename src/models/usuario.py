class Usuario:
    def __init__(self, nombre, apellido, cuil, email, contrasena, saldo=0, total_invertido=0, rendimiento_total=0):
        self.nombre = nombre
        self.apellido = apellido
        self.cuil = cuil
        self.email = email
        self.contrasena = contrasena
        self.saldo = 1000000
        self.total_invertido = total_invertido
        self.rendimiento_total = rendimiento_total
        self.portafolio = {}  # Diccionario para almacenar activos y cantidades

    def agregar_accion(self, nombre_accion, cantidad, precio_compra):
        if nombre_accion in self.portafolio:
            self.portafolio[nombre_accion]['cantidad'] += cantidad
        else:
            self.portafolio[nombre_accion] = {
                'cantidad': cantidad,
                'precio_compra': precio_compra,
                'precio_venta': precio_compra  # Inicialmente el precio de venta es igual al precio de compra
            }
        # Actualizar el saldo y el total invertido
        self.saldo -= cantidad * precio_compra
        self.total_invertido += cantidad * precio_compra

    def quitar_accion(self, nombre_accion, cantidad):
        if nombre_accion in self.portafolio:
            self.portafolio[nombre_accion]['cantidad'] -= cantidad
            if self.portafolio[nombre_accion]['cantidad'] <= 0:
                del self.portafolio[nombre_accion]

    def mostrar_datos_cuenta(self):
        print("=== Datos de la cuenta ===")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"CUIL: {self.cuil}")
        print(f"Email: {self.email}")
        print(f"Saldo: {self.saldo}")
        print(f"Total Invertido: {self.total_invertido}")
        print(f"Rendimiento Total: {self.rendimiento_total}")
