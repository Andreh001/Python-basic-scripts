class Persona():

    def __init__(self, rut_p=None, nombre_p=None,
                 edad_p=None, direccion_p=None, ciudad_p=None, lugar_v=None):
        self.rut = rut_p
        self.nombre = nombre_p
        self.edad = edad_p
        self.direccion = direccion_p
        self.ciudad = ciudad_p
        self.lugar_votacion = lugar_v

    def mostrar(self):
        print(f"RUT: {self.rut}")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Ciudad: {self.ciudad}")
        print(f"Dirección: {self.direccion}")
        print(f"Lugar de votación: {self.lugar_votacion}")

    def puedeVotar(self):
        return self.edad >= 18