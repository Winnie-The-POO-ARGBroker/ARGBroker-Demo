from dao.usuario_dao import UsuarioDAO
from dao.accion_dao import AccionDAO
from models.usuario import Usuario
from servicio.gestor_db import GestorDB

def registrar_inversor():
    print("=== Registrar nuevo inversor ===")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    cuil = input("Ingrese su CUIL: ")
    email = input("Ingrese su email: ")
    contrasena = input("Ingrese su contraseña: ")
    
    # Crear un nuevo objeto Usuario
    nuevo_usuario = Usuario(nombre, apellido, cuil, email, contrasena)
    
    # Conectar a la base de datos
    gestor = GestorDB()
    conexion = gestor.connect()
    
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return
    
    # Registrar el usuario en la base de datos
    usuario_dao = UsuarioDAO(conexion)
    if usuario_dao.insertar(nuevo_usuario):
        pass
    else:
        pass

def iniciar_sesion():
    print("=== Inicio de sesión ===")
    email = input("Ingrese su email: ")

    gestor = GestorDB()
    conexion = gestor.connect()

    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return None

    usuario_dao = UsuarioDAO(conexion)

    # Controlar intentos fallidos
    intentos_fallidos = 0
    intentos_maximos = 3
    while intentos_fallidos < intentos_maximos:
        usuario = usuario_dao.obtener_por_email(email)

        if usuario:
            contrasena = input("Ingrese su contraseña: ")
            if usuario.contrasena == contrasena:
                print(f"Bienvenido/a {usuario.nombre} {usuario.apellido}")
                return usuario
            else:
                intentos_fallidos += 1
                if intentos_fallidos < intentos_maximos:
                    intentos_restantes = intentos_maximos - intentos_fallidos
                    print(f"Email o contraseña incorrectos. Quedan {intentos_restantes} intentos.")
                else:
                    print("Ha superado el número máximo de intentos fallidos. Su cuenta está bloqueada.")
        else:
            print("El correo electrónico ingresado no está registrado en la base de datos.")
            return None  # Salir de la función si el correo no existe

    return None

def mostrar_datos_cuenta(usuario):
    usuario.mostrar_datos_cuenta()

def recuperar_contrasena():
    print("=== Recuperación de Contraseña ===")
    email = input("Ingrese su email: ")
    
    gestor = GestorDB()
    conexion = gestor.connect()
    
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return

    usuario_dao = UsuarioDAO(conexion)
    usuario = usuario_dao.obtener_por_email(email)

    if usuario:
        # Aquí deberías enviar un correo con un enlace para recuperar la contraseña
        print("Se ha enviado un enlace de recuperación a su correo electrónico.")
    else:
        print("No se encontró un usuario con ese email.")

def listar_portafolio(usuario):
    print("=== Portafolio de activos ===")
    for nombre_activo, info in usuario.portafolio.items():
        print(f"Activo: {nombre_activo}, Cantidad: {info['cantidad']}, Precio de Compra: {info['precio_compra']}, Precio de Venta: {info['precio_venta']}")

def comprar_acciones(usuario):
    print("=== Comprar Acciones ===")
    activo = input("Ingrese el nombre del activo: ")
    cantidad = int(input("Ingrese la cantidad de acciones a comprar: "))
    precio_compra = float(input("Ingrese el precio de compra por acción: "))
    
    # Validaciones
    total_costo = precio_compra * cantidad
    if total_costo > usuario.saldo:
        print("No tienes suficiente saldo para realizar esta compra.")
        return
    
    # Registrar compra
    usuario.saldo -= total_costo
    usuario.total_invertido += total_costo
    
    # Actualizar portafolio
    if activo in usuario.portafolio:
        usuario.portafolio[activo]['cantidad'] += cantidad
    else:
        usuario.portafolio[activo] = {'cantidad': cantidad, 'precio_compra': precio_compra, 'precio_venta': precio_compra}
    
    print(f"Compra exitosa: {cantidad} acciones de {activo} a ${precio_compra:.2f} cada una.")

def vender_acciones(usuario):
    print("=== Vender Acciones ===")
    activo = input("Ingrese el nombre del activo: ")
    cantidad = int(input("Ingrese la cantidad de acciones a vender: "))
    
    # Validar existencia y cantidad
    if activo not in usuario.portafolio or usuario.portafolio[activo]['cantidad'] < cantidad:
        print("No tienes suficientes acciones para vender.")
        return
    
    precio_venta = float(input("Ingrese el precio de venta por acción: "))
    
    # Registrar venta
    usuario.saldo += precio_venta * cantidad
    usuario.total_invertido -= usuario.portafolio[activo]['precio_compra'] * cantidad
    rendimiento = (precio_venta - usuario.portafolio[activo]['precio_compra']) * cantidad
    usuario.rendimiento_total += rendimiento
    
    # Actualizar portafolio
    usuario.portafolio[activo]['cantidad'] -= cantidad
    if usuario.portafolio[activo]['cantidad'] == 0:
        del usuario.portafolio[activo]
    
    print(f"Venta exitosa: {cantidad} acciones de {activo} a ${precio_venta:.2f} cada una.")

## MAIN
def main():
    usuario = None
    while True:
        print("\n===== Bienvenido a ARGBroker =====")
        if usuario is None:
            print("1. Registrar nuevo inversor")
            print("2. Iniciar sesión")
            print("3. Salir")
        else:
            print("1. Mostrar datos de la cuenta")
            print("2. Listar portafolio de activos")
            print("3. Comprar acciones")
            print("4. Vender acciones")
            print("5. Recuperar contraseña")
            print("6. Cerrar sesión")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            if usuario is None:
                registrar_inversor()
            else:
                mostrar_datos_cuenta(usuario)
        elif opcion == "2":
            if usuario is None:
                usuario = iniciar_sesion()
                if usuario:
                    print(f"Sesión iniciada como {usuario.nombre}")
            else:
                listar_portafolio(usuario)
        elif opcion == "3":
            if usuario is None:
                print("Gracias por utilizar ARGBroker. ¡Hasta pronto!")
                break  # Salir del programa cuando no hay sesión activa
            else:
                comprar_acciones(usuario)
        elif opcion == "4":
            if usuario is None:
                print("Debe iniciar sesión primero.")
            else:
                vender_acciones(usuario)
        elif opcion == "5":
            if usuario is None:
                print("Debe iniciar sesión primero.")
            else:
                recuperar_contrasena()
        elif opcion == "6":
            if usuario is not None:
                print("Cerrando sesión...")
                usuario = None  # Cerrar sesión
            else:
                print("No hay sesión activa.")
        elif opcion == "7":
            print("Gracias por utilizar ARGBroker. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida, por favor seleccione nuevamente.")

if __name__ == "__main__":
    main()
