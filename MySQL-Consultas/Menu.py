import time
from sys import platform
import os
import Functions
def cls():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")

def MainMenu():
    cls()
    print()
    print(" ███╗   ███╗██╗   ██╗███████╗ ██████╗ ██╗")
    print(" ████╗ ████║╚██╗ ██╔╝██╔════╝██╔═══██╗██║")
    print(" ██╔████╔██║ ╚████╔╝ ███████╗██║   ██║██║")
    print(" ██║╚██╔╝██║  ╚██╔╝  ╚════██║██║▄▄ ██║██║")
    print(" ██║ ╚═╝ ██║   ██║   ███████║╚██████╔╝███████╗")
    print(" ╚═╝     ╚═╝   ╚═╝   ╚══════╝ ╚══▀▀═╝ ╚══════╝")
    print()
    print("           Menú de consultas SQL")
    print()
    menuOptions = [
        "1. Create database",
        "2. Select",
        "3. Roles",
        "4. Drop database",
        "5. Salir"
    ]
    for Menu in menuOptions:
        print(Menu)
    print()
    option = int(input("N: "))
    while option < 1 or option > len(menuOptions):
        print()
        print("Opción errónea.")
        option = int(input("Ingrese opción nuevamente: "))
    else:
        if option == 1:
            Functions.CreateDB()
        if option == 2:
            Functions.Select()
        if option == 3:
            Functions.Roles()
        if option == 4:
            Functions.DropDatabase()
        if option == 5:
            print()
            print("Saliendo...")
            time.sleep(2)
            exit()