class Cliente():
    def __init__(self, rut, nombre, edad):
        self.rut = rut
        self.nombre = nombre
        self.edad = edad

    def infoCliente(self):
        print(f"RUT:{self.rut}")
        print(f"Nombre:{self.nombre}")
        print(f"Edad:{self.edad}")