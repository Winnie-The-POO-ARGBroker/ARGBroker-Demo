class TransaccionDAO:
    def __init__(self):
        self.transacciones = []

    def registrar_transaccion(self, transaccion):
        self.transacciones.append(transaccion)

    def listar_transacciones(self, inversor):
        return [t for t in self.transacciones if t.inversor == inversor]
