from Clases.Persona import Persona
from Clases.Candidato import Candidato
from Clases.Elecciones import Elecciones
import os
def clear():
    os.system("cls")

persona_1 = Persona('11.111.111-1', 'Juan Toloza', 19, 'Maipu 567', 'Los Ángeles', 'Liceo I - Mesa 45')
persona_2 = Persona('22.222.222-2', 'Andres Cea', 16, 'Freire 400', 'Los Ángeles', 'Liceo I - Mesa 45')
lista_v = [persona_1, persona_2]

candidato_1 = Candidato('A-1', 'Juanito Torres', 'Partido 1')
candidato_2 = Candidato('B-4', 'Esteban Roa', 'Partido 2')
lista_c = [candidato_1, candidato_2]
eleccion_2021 = Elecciones()
eleccion_2021.lista_votantes = lista_v
eleccion_2021.lista_candidatos = lista_c

while True:
    print(" ███████╗██╗     ███████╗ ██████╗ ██████╗██╗ ██████╗ ███╗   ██╗███████╗███████╗")
    print(" ██╔════╝██║     ██╔════╝██╔════╝██╔════╝██║██╔═══██╗████╗  ██║██╔════╝██╔════╝·")
    print(" █████╗  ██║     █████╗  ██║     ██║     ██║██║   ██║██╔██╗ ██║█████╗  ███████╗")
    print(" ██╔══╝  ██║     ██╔══╝  ██║     ██║     ██║██║   ██║██║╚██╗██║██╔══╝  ╚════██║")
    print(" ███████╗███████╗███████╗╚██████╗╚██████╗██║╚██████╔╝██║ ╚████║███████╗███████║")
    print(" ╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝")
    print()
    print("\nLista candidatos")
    print("\n")
    for i in eleccion_2021.lista_candidatos:
        i.mostrar()
        print()

    rut_ingresado = input("Ingrese su RUT: ")
    voto_candidato = input("Ingrese el código: ")
    for v in eleccion_2021.lista_votantes:
        if v.rut == rut_ingresado:
            if v.puedeVotar():
                eleccion_2021.votar(rut_ingresado, voto_candidato)
            else:
                print("No puedes votar ya que no eres mayor de edad.")

    salir = input("Ingrese 's' para salir: ")
    if salir == "s":
        break
clear()
results = input("Ingrese 'resultados' para ver los resultados de la votación, de lo contrario, presione Enter: ")
if results == "resultados":
    print("¡La votación ha finalizado!\nVotos totales: \n")
    for candidato in eleccion_2021.lista_candidatos:
        candidato.mostrarVotos()
elif results == "Resultados":
    print("¡La votación ha finalizado!\nVotos totales: \n")
    for candidato in eleccion_2021.lista_candidatos:
        candidato.mostrarVotos()
else:
    exit()