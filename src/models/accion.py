class Accion:
    def __init__(self, id, simbolo, nombre_empresa, ultimo_operado, cantidad_compra_diaria, precio_compra, precio_venta, cantidad_venta_diaria, apertura, minimo_diario, maximo_diario, ultimo_cierre):
        self.id = id
        self.simbolo = simbolo
        self.nombre_empresa = nombre_empresa
        self.ultimo_operado = ultimo_operado
        self.cantidad_compra_diaria = cantidad_compra_diaria
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.cantidad_venta_diaria = cantidad_venta_diaria
        self.apertura = apertura
        self.minimo_diario = minimo_diario
        self.maximo_diario = maximo_diario
        self.ultimo_cierre = ultimo_cierre
