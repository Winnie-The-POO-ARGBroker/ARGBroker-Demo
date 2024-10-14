from dao.usuario_dao import UsuarioDAO
from dao.accion_dao import AccionDAO
<<<<<<< HEAD
from models.usuario import Usuario
=======
from dao.transaccion_dao import TransaccionDAO
from models.usuario import Usuario
from models.transaccion import Transaccion
>>>>>>> Magali
from servicio.gestor_db import GestorDB

def registrar_inversor():
    print("=== Registrar nuevo inversor ===")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    cuil = input("Ingrese su CUIL: ")
    email = input("Ingrese su email: ")
    contrasena = input("Ingrese su contraseña: ")
<<<<<<< HEAD
=======

    # Validación simple de email
    if "@" not in email or "." not in email:
        print("El email ingresado no es válido.")
        return
>>>>>>> Magali
    
    # Crear un nuevo objeto Usuario
    nuevo_usuario = Usuario(nombre, apellido, cuil, email, contrasena)
    
    # Conectar a la base de datos
    gestor = GestorDB()
    conexion = gestor.connect()
    
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return
    
<<<<<<< HEAD
    # Registrar el usuario en la base de datos
    usuario_dao = UsuarioDAO(conexion)
    if usuario_dao.insertar(nuevo_usuario):
        pass
    else:
        pass
=======
    usuario_dao = UsuarioDAO(conexion)

    try:
        if usuario_dao.insertar(nuevo_usuario):
            print("Usuario registrado exitosamente.")
        else:
            print("Error al registrar el usuario.")
    except Exception as e:
        print(f"Ocurrió un error al registrar el usuario: {e}")
    finally:
        conexion.close()  # Asegúrate de cerrar la conexión
>>>>>>> Magali

def iniciar_sesion():
    print("=== INICIO DE SESIÓN ===")
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
<<<<<<< HEAD
            if usuario.contrasena == contrasena:
=======
            # Verifica la contraseña utilizando el método de UsuarioDAO
            if usuario_dao.verificar_contrasena(email, contrasena):
>>>>>>> Magali
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

<<<<<<< HEAD
=======
    conexion.close()  # Cierra la conexión al final
>>>>>>> Magali
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
<<<<<<< HEAD

def listar_portafolio(usuario):
    print("=== Portafolio de activos ===")
    for nombre_activo, info in usuario.portafolio.items():
        print(f"Activo: {nombre_activo}, Cantidad: {info['cantidad']}, Precio de Compra: {info['precio_compra']}, Precio de Venta: {info['precio_venta']}")
=======
    
    conexion.close()  # Cierra la conexión al final


def listar_portafolio(usuario, accion_dao):
    print("=== Portafolio de activos ===")
    if not usuario.portafolio:
        print("No tienes acciones en tu portafolio.")
        return

    rendimiento_total = 0
    for nombre_empresa, info in usuario.portafolio.items():
        # Verificamos si nombre_empresa se está obteniendo correctamente
        print(f"Obteniendo información para {nombre_empresa}...")

        # Usar el AccionDAO para obtener los precios
        accion = accion_dao.obtener_por_nombre(nombre_empresa)  # Asegúrate de que sea el nombre correcto
        if accion:
            precio_actual_compra = accion.precio_compra
            precio_actual_venta = accion.precio_venta

            # Calcular el rendimiento
            rendimiento = (precio_actual_compra - info['precio_compra']) * info['cantidad']
            rendimiento_total += rendimiento


            print(f"Activo: {accion.nombre_empresa}, Cantidad: {info['cantidad']}, "
                  f"Precio de Compra: {info['precio_compra']:.2f}, "
                  f"Precio Actual de Compra: {precio_actual_compra:.2f}, "
                  f"Precio Actual de Venta: {precio_actual_venta:.2f}, "
                  f"Rendimiento: ${rendimiento:.2f}")
        else:
            print(f"No se encontró la acción con el nombre {nombre_empresa} en la base de datos.")

    print(f"Rendimiento total de tu portafolio: ${rendimiento_total:.2f}")

>>>>>>> Magali

def comprar_acciones(usuario):
    print("=== Comprar Acciones ===")
    activo = input("Ingrese el nombre del activo: ")
    cantidad = int(input("Ingrese la cantidad de acciones a comprar: "))
<<<<<<< HEAD
    precio_compra = float(input("Ingrese el precio de compra por acción: "))
    
    # Validaciones
    total_costo = precio_compra * cantidad
    if total_costo > usuario.saldo:
        print("No tienes suficiente saldo para realizar esta compra.")
        return
    
    # Registrar compra
    usuario.saldo -= total_costo
    usuario.total_invertido += total_costo
    
=======

    # Conectar a la base de datos
    gestor = GestorDB()
    conexion = gestor.connect()

    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return

    # Inicializar AccionDAO
    accion_dao = AccionDAO(conexion)

    # Obtener el precio de compra del activo y su ID
    accion = accion_dao.obtener_por_nombre(activo)

    if accion is None:
        print("El activo no se encuentra en la base de datos.")
        return

    # Aquí accedemos al atributo precio_compra de la acción
    precio_compra = accion.precio_compra  # No es necesario convertir a decimal si ya es Decimal
    accion_id = accion.id

    total_costo = precio_compra * cantidad

    if total_costo > usuario.saldo:
        print("No tienes suficiente saldo para realizar esta compra.")
        return

    # Registrar compra
    usuario.saldo -= total_costo
    usuario.total_invertido += total_costo

>>>>>>> Magali
    # Actualizar portafolio
    if activo in usuario.portafolio:
        usuario.portafolio[activo]['cantidad'] += cantidad
    else:
<<<<<<< HEAD
        usuario.portafolio[activo] = {'cantidad': cantidad, 'precio_compra': precio_compra, 'precio_venta': precio_compra}
    
    print(f"Compra exitosa: {cantidad} acciones de {activo} a ${precio_compra:.2f} cada una.")

=======
        usuario.portafolio[activo] = {'cantidad': cantidad, 'precio_compra': precio_compra}

    print(f"Compra exitosa: {cantidad} acciones de {activo} a ${precio_compra:.2f} cada una.")

    # Registrar la transacción en la tabla de transacciones
    transaccion_dao = TransaccionDAO(conexion)
    transaccion = Transaccion(
        usuario_id=usuario.id,  # ID del usuario
        accion_id=accion_id,    # ID de la acción
        tipo='compra',
        cantidad=cantidad,
        precio=precio_compra
    )
    transaccion_dao.registrar_transaccion(transaccion)

    conexion.close()  # Cierra la conexión al final


>>>>>>> Magali
def vender_acciones(usuario):
    print("=== Vender Acciones ===")
    activo = input("Ingrese el nombre del activo: ")
    cantidad = int(input("Ingrese la cantidad de acciones a vender: "))
    
    # Validar existencia y cantidad
    if activo not in usuario.portafolio or usuario.portafolio[activo]['cantidad'] < cantidad:
        print("No tienes suficientes acciones para vender.")
        return
    
<<<<<<< HEAD
    precio_venta = float(input("Ingrese el precio de venta por acción: "))
    
    # Registrar venta
    usuario.saldo += precio_venta * cantidad
    usuario.total_invertido -= usuario.portafolio[activo]['precio_compra'] * cantidad
=======
    # Obtener el precio de venta desde la base de datos
    gestor = GestorDB()
    conexion = gestor.connect()
    accion_dao = AccionDAO(conexion)
    precio_venta = accion_dao.obtener_precio_por_activo(activo)

    if precio_venta is None:
        print("No se encuentra el activo en la base de datos.")
        return
    
    # Registrar venta
    usuario.saldo += precio_venta * cantidad
>>>>>>> Magali
    rendimiento = (precio_venta - usuario.portafolio[activo]['precio_compra']) * cantidad
    usuario.rendimiento_total += rendimiento
    
    # Actualizar portafolio
    usuario.portafolio[activo]['cantidad'] -= cantidad
    if usuario.portafolio[activo]['cantidad'] == 0:
        del usuario.portafolio[activo]
    
    print(f"Venta exitosa: {cantidad} acciones de {activo} a ${precio_venta:.2f} cada una.")
<<<<<<< HEAD
=======
    
    # Registrar la transacción en la tabla de transacciones
    transaccion_dao = TransaccionDAO(conexion)
    transaccion_dao.registrar_transaccion({
        'email': usuario.email,
        'activo': activo,
        'cantidad': cantidad,
        'precio': precio_venta,
        'tipo': 'venta'
    })

>>>>>>> Magali

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

<<<<<<< HEAD
        opcion = input("Seleccione una opción: ")
        
=======
        # Selecciona una opción
        opcion = input("Seleccione una opción: ")
        
        # Inicializar gestor de base de datos y conexión
        gestor = GestorDB()
        conexion = gestor.connect()

>>>>>>> Magali
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
<<<<<<< HEAD
                listar_portafolio(usuario)
=======
                # Aquí instancias AccionDAO con la conexión
                accion_dao = AccionDAO(conexion)
                listar_portafolio(usuario, accion_dao)
                rendimiento = usuario.calcular_rendimiento_acciones()
                print(f"Rendimiento total de tu portafolio: ${rendimiento:.2f}")
>>>>>>> Magali
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
<<<<<<< HEAD
=======
        
        # Asegurarse de cerrar la conexión después de cada iteración
        if conexion:
            conexion.close()
>>>>>>> Magali

if __name__ == "__main__":
    main()
