import os
from sys import platform
import random

nombres = ["Jose", "Biel", "Lucas", "Luis", "Narciso", "Jesus", "Tomas", "Jorge", "Fabian", "Celso"]
apellidos = ["Antunez", "Florez", "Martínez", "Andujar", "Montoya", "Andreu", "De la Torre", "Tapia", "Bosch", "Ripoll"]
def cls():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")

def Menu():
    cls()
    print()
    print("  ██████╗ █████╗      ██╗███████╗██████╗  ██████╗")
    print(" ██╔════╝██╔══██╗     ██║██╔════╝██╔══██╗██╔═══██╗")
    print(" ██║     ███████║     ██║█████╗  ██████╔╝██║   ██║")
    print(" ██║     ██╔══██║██   ██║██╔══╝  ██╔══██╗██║   ██║")
    print(" ╚██████╗██║  ██║╚█████╔╝███████╗██║  ██║╚██████╔╝")
    print("  ╚═════╝╚═╝  ╚═╝ ╚════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝")
    print()
    print(" Bienvenido", random.choice(nombres), random.choice(apellidos))
    print()
    print(" Por favor, seleccione el producto con que desea operar")
    print()
    menuProductos = [
        " 1. Cuenta Corriente",
        " 2. Linea de Crédito",
        " 3. Cuenta de Ahorro",
        " 4. Cuenta Vista",
        " 5. Tarjeta de Crédito",
        " 6. Salir"
    ]
    for menu in menuProductos:
        print(menu)
    print()
    opcion = int(input("N: "))
    if opcion >= 1 and opcion <= len(menuProductos):
        if opcion == 1:
            import CuentaCorriente
            CuentaCorriente.MainMenu()
        if opcion == 2:
            import LineaDeCredito
            LineaDeCredito.MainMenu()
        if opcion == 3:
            import CuentaDeAhorro
            CuentaDeAhorro.MainMenu()
        if opcion == 4:
            import CuentaVista
            CuentaVista.MainMenu()
        if opcion == 5:
            import TarjetaDeCredito
            TarjetaDeCredito.MainMenu()
        if opcion == 6:
            exit()
    else:
        print()
        print("Introduzca una opción entre 1 y " + len(menuProductos) + ".")
        print()
        opcion = int(input("N: "))