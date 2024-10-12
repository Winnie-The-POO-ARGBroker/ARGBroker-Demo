class Transaccion:
    def __init__(self, usuario, accion, tipo, cantidad, precio, comision=0.015):
        self.usuario = usuario
        self.accion = accion
        self.tipo = tipo  # 'compra' o 'venta'
        self.cantidad = cantidad
        self.precio = precio
        self.comision = comision
        self.total = self.calcular_total()

    def calcular_total(self):
        costo_total = self.cantidad * self.precio
        costo_comision = costo_total * self.comision
        return costo_total + costo_comision if self.tipo == 'compra' else costo_total - costo_comision
