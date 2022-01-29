class Movimiento():
    def __init__(self, numero_cuenta, fecha, monto, tipo):
        self.numero_cuenta = numero_cuenta
        self.fecha = fecha
        self.monto = monto
        self.tipo = tipo

    def VerMovimiento(self):
        print(f"Nro Cuenta: {self.numero_cuenta}")
        print(f"Fecha: {self.fecha}")
        print(f"Monto: {self.monto}")
        print(f"Tipo: {self.tipo}")