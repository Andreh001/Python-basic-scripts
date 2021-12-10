import time
import os
from sys import platform
import ErrorCodes
def cls():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")

def MainMenu():
    cls()
    print()
    print(" ██████╗██████╗ ███████╗██████╗ ██╗████████╗ ██████╗")
    print(" ██╔════╝██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔═══██╗")
    print(" ██║     ██████╔╝█████╗  ██║  ██║██║   ██║   ██║   ██║")
    print(" ██║     ██╔══██╗██╔══╝  ██║  ██║██║   ██║   ██║   ██║")
    print(" ╚██████╗██║  ██║███████╗██████╔╝██║   ██║   ╚██████╔╝")
    print("  ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝   ╚═╝    ╚═════╝")
    print()
    print("       Línea de Crédito")
    print()
    print(" Por favor, seleccione la operación que desea realizar")
    print()
    menuOpciones = [
        " 1. Giro",
        " 2. Consulta de saldo",
        " 3. Volver al menú principal"
    ]
    for menu in menuOpciones:
        print(menu)
    print()
    opcion = int(input("N: "))
    if opcion >= 1 and opcion <= len(menuOpciones):
        if opcion == 1:
            print()
            print(" 1. $10.000")
            print(" 2. $20.000")
            print(" 3. $")
        if opcion == 3:
            from MainMenu import Menu
            return Menu()
    else:
        ErrorCodes.OptionInvalid()