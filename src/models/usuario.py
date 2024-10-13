import bcrypt

class Usuario:
    def __init__(self, id, nombre, apellido, cuil, email, contrasena, saldo=0, total_invertido=0, rendimiento_total=0):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cuil = cuil
        self.email = email
        # Si la contraseña parece ser un hash (en bytes), no la hashees nuevamente
        if isinstance(contrasena, bytes):
            self.contrasena = contrasena  # Ya es un hash
        else:
            self.contrasena = self.hash_password(contrasena)  # Hashea solo si es una contraseña en texto plano
        self.saldo = saldo
        self.total_invertido = total_invertido
        self.rendimiento_total = rendimiento_total
        self.portafolio = {}

    def hash_password(self, password):
        # Hashea la contraseña y devuelve el hash en formato bytes
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def check_password(self, password):
        # Compara una contraseña en texto plano con el hash almacenado
        return bcrypt.checkpw(password.encode('utf-8'), self.contrasena)

    def agregar_accion(self, nombre_accion, cantidad, precio_compra):
        total_costo = cantidad * precio_compra
        if self.saldo < total_costo:
            print("No tienes suficiente saldo para realizar esta compra.")
            return
        
        if nombre_accion in self.portafolio:
            self.portafolio[nombre_accion]['cantidad'] += cantidad
        else:
            self.portafolio[nombre_accion] = {
                'cantidad': cantidad,
                'precio_compra': precio_compra,
                'precio_venta': precio_compra  # Inicialmente el precio de venta es igual al precio de compra
            }

        # Actualizar el saldo y el total invertido
        self.saldo -= total_costo
        self.total_invertido += total_costo

    def quitar_accion(self, nombre_accion, cantidad):
        if nombre_accion in self.portafolio:
            if self.portafolio[nombre_accion]['cantidad'] < cantidad:
                print("No tienes suficientes acciones para vender.")
                return
            
            self.portafolio[nombre_accion]['cantidad'] -= cantidad
            if self.portafolio[nombre_accion]['cantidad'] <= 0:
                del self.portafolio[nombre_accion]

    def mostrar_datos_cuenta(self):
        print("=== Datos de la cuenta ===")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"CUIL: {self.cuil}")
        print(f"Email: {self.email}")
        print(f"Saldo: ${self.saldo:.2f}")
        print(f"Total Invertido: ${self.total_invertido:.2f}")
        print(f"Rendimiento Total: ${self.rendimiento_total:.2f}")

    def calcular_rendimiento_acciones(self):
        rendimiento_total = 0
        for nombre_accion, info in self.portafolio.items():
            precio_venta = info.get('precio_venta', 0)  # Cambia el valor predeterminado a 0
            if precio_venta is None:  # Si el precio de venta no ha sido establecido
                precio_venta = 0  # Asignar un valor de 0 o manejar como desees

            rendimiento = (precio_venta - info['precio_compra']) * info['cantidad']
            rendimiento_total += rendimiento
            print(f"Activo: {nombre_accion}, Cantidad: {info['cantidad']}, Rendimiento: ${rendimiento:.2f}")
        return rendimiento_total


    def agregar_al_portafolio(self, accion, cantidad, precio_compra):
        if accion in self.portafolio:
            self.portafolio[accion]['cantidad'] += cantidad
        else:
            self.portafolio[accion] = {'cantidad': cantidad, 'precio_compra': precio_compra}

    def eliminar_del_portafolio(self, accion, cantidad):
        if accion in self.portafolio:
            self.portafolio[accion]['cantidad'] -= cantidad
            if self.portafolio[accion]['cantidad'] <= 0:
                del self.portafolio[accion]