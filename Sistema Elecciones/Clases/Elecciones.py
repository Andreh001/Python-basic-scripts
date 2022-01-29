class Elecciones():

    def __init__(self, rut_v=None, identificador_c=None, lista_v=None, lista_c=None):
        self.rut_votante = rut_v
        self.identificador_candidato = identificador_c
        self.lista_votantes = lista_v
        self.lista_candidatos = lista_c

    def votar(self, rut_v, identificador_c=None):
        for votante in self.lista_votantes:
            if rut_v == votante.rut:
                for candidato in self.lista_candidatos:
                    if identificador_c == candidato.identificador:
                        candidato.votos_totales += 1
                        print("¡Tu voto ha sido enviado!")
                        break
            break