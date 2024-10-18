import bcrypt
from servicio.gestor_db import GestorDB  # Asegúrate de que esta clase exista y funcione
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario
from dao.portafolio_dao import PortafolioDAO

def main():
    # Inicializa la conexión a la base de datos
    gestor_db = GestorDB()  # Asegúrate de que esta clase exista y funcione
    conexion = gestor_db.connect()  # Método para establecer la conexión

    # Inicializa usuario_dao y portafolio_dao con la conexión
    usuario_dao = UsuarioDAO(conexion)  
    portafolio_dao = PortafolioDAO(conexion)  

    while True:
        print("\nMENÚ")
        print("1. Registrar")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario(usuario_dao)
        elif opcion == '2':
            iniciar_sesion(usuario_dao, portafolio_dao)
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def registrar_usuario(usuario_dao):
    print("=== Registro de Nuevo Usuario ===")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    cuil = input("Ingrese su CUIL: ")
    email = input("Ingrese su email: ")
    contrasena = input("Ingrese su contraseña: ")
    
    # Hash de la contraseña
    contrasena_hash = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
    
    nuevo_usuario = Usuario(
        id=None,
        nombre=nombre,
        apellido=apellido,
        cuil=cuil,
        email=email,
        contrasena=contrasena_hash
    )

    try:
        if usuario_dao.insertar(nuevo_usuario):
            print("Registro exitoso.")
        else:
            print("Error al registrar el usuario. Verifique los datos ingresados.")
    except Exception as e:
        print(f"Error al registrar el usuario: {e}")

def iniciar_sesion(usuario_dao, portafolio_dao):
    email = input("Ingrese su email: ")
    contrasena = input("Ingrese su contraseña: ")
    
    usuario = usuario_dao.obtener_por_email(email)

    if usuario:
        if usuario.bloqueado:
            print("Su cuenta está bloqueada. No puede iniciar sesión.")
            return
        
        print(f"Hash almacenado: {usuario.contrasena.decode('utf-8')}")
        print(f"Contraseña ingresada: {contrasena}")

        es_correcta = bcrypt.checkpw(contrasena.encode('utf-8'), usuario.contrasena)
        print(f"La contraseña es {'correcta' if es_correcta else 'incorrecta'}.")
        
        if es_correcta:
            print("Inicio de sesión exitoso.")
            usuario.intentos_fallidos = 0  # Reiniciar intentos fallidos
            usuario_dao.actualizar_intentos(usuario)
            # Pasa también la conexión aquí
            menu_principal(usuario_dao, portafolio_dao, usuario, usuario_dao.conexion)
        else:
            print("Contraseña incorrecta.")
            usuario.intentos_fallidos += 1
            usuario_dao.actualizar_intentos(usuario)
            if usuario.intentos_fallidos >= 3:
                usuario.bloqueado = True
                usuario_dao.bloquear_usuario(usuario)
                print("Su cuenta ha sido bloqueada tras 3 intentos fallidos.")
    else:
        print("Usuario no encontrado.")


def mostrar_datos_cuenta(usuario_dao, usuario_id, conexion):
    datos_cuenta = usuario_dao.obtener_datos_cuenta(usuario_id)

    if datos_cuenta:
        total_invertido = usuario_dao.calcular_total_invertido(usuario_id, conexion)  # Asegúrate de pasar la conexión
        print("=== Datos de la cuenta ===")
        print(f"Nombre: {datos_cuenta[0]}")
        print(f"Apellido: {datos_cuenta[1]}")
        print(f"CUIL: {datos_cuenta[2]}")
        print(f"Email: {datos_cuenta[3]}")
        print(f"Saldo: ${datos_cuenta[4]:,.2f}")
        print(f"Total Invertido: ${total_invertido:,.2f}")
        print(f"Rendimiento Total: ${datos_cuenta[6]}")
    else:
        print("No se encontraron datos para este usuario.")


def listar_activos_portafolio(usuario, portafolio_dao):
    print("\n=== Activos del Portafolio ===")
    activos = portafolio_dao.listar_activos_portafolio(usuario.id)

    if not activos:
        print("No hay activos en el portafolio.")
        return

    for activo in activos:
        nombre_empresa, cantidad, precio_compra_actual, precio_venta_actual, rendimiento = activo
        print(f"Empresa: {nombre_empresa}")
        print(f"Cantidad de acciones: {cantidad}")
        print(f"Precio de compra actual: ${precio_compra_actual:.2f}")
        print(f"Precio de venta actual: ${precio_venta_actual:.2f}")
        print(f"Rendimiento: {rendimiento:.2f}%")
        print("--------------------------")

def menu_principal(usuario_dao, portafolio_dao, usuario, conexion):
    while True:
        print("\nMENÚ PRINCIPAL")
        print("1. Mostrar datos de la cuenta")
        print("2. Listar activos del portafolio")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_datos_cuenta(usuario_dao, usuario.id, conexion)
        elif opcion == '2':
            listar_activos_portafolio(usuario, portafolio_dao)
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
