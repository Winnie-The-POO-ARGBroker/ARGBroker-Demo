<<<<<<< HEAD
class Transaccion:
    def __init__(self, usuario, accion, tipo, cantidad, precio, comision=0.015):
        self.usuario = usuario
        self.accion = accion
        self.tipo = tipo  # 'compra' o 'venta'
        self.cantidad = cantidad
        self.precio = precio
        self.comision = comision
=======
from decimal import Decimal

class Transaccion:
    def __init__(self, usuario_id, accion_id, tipo, cantidad, precio, comision=0.015):
        self.usuario_id = usuario_id  # ID del usuario en lugar del objeto usuario
        self.accion_id = accion_id    # ID de la acción en lugar del objeto acción
        self.tipo = tipo  # 'compra' o 'venta'
        self.cantidad = cantidad
        self.precio = Decimal (precio)
        self.comision = Decimal (comision)
>>>>>>> Magali
        self.total = self.calcular_total()

    def calcular_total(self):
        costo_total = self.cantidad * self.precio
        costo_comision = costo_total * self.comision
        return costo_total + costo_comision if self.tipo == 'compra' else costo_total - costo_comision
