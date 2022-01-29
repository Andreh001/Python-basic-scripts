class Candidato():

    def __init__(self, identificador_c=None, nombre_c=None, partido_p=None, votos_t=0):
        self.identificador = identificador_c
        self.nombre = nombre_c
        self.partido = partido_p
        self.votos_totales = votos_t

    def mostrar(self):
        print(f"Identificador: {self.identificador}")
        print(f"Nombre: {self.nombre}")
        print(f"Partido Politico: {self.partido}")

    def mostrarVotos(self):
        print(f"Candidato : {self.nombre}")
        print(f"Numero de votos obtenidos: {self.votos_totales}")