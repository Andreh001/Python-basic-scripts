class Cuenta():

    def __init__(self, numero_cuenta, tipo_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = saldo

    def ConsultarSaldo(self):
        print(f"Número de cuenta: {self.numero_cuenta}\nSaldo disponible: {self.saldo}")
    def depositar(self, monto):
        self.saldo += monto
        print(f"Se ha depositado ${monto} en su cuenta.")

    def girar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print("Giro realizado correctamente...")
        else:
            print("No cuenta con saldo suficiente para realizar esta operación")