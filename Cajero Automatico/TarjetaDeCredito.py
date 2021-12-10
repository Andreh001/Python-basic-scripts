import time
import os
import ErrorCodes
import MainMenu
from sys import platform
def cls():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")

saldoCuentaCorriente = 50000
saldoCuentaVista = 20100
saldo = 100000

def MainMenu():
    cls()
    print()
    print("████████╗     ██████╗██████╗ ███████╗██████╗ ██╗████████╗ ██████╗")
    print("╚══██╔══╝    ██╔════╝██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔═══██╗")
    print("   ██║       ██║     ██████╔╝█████╗  ██║  ██║██║   ██║   ██║   ██║")
    print("   ██║       ██║     ██╔══██╗██╔══╝  ██║  ██║██║   ██║   ██║   ██║")
    print("   ██║██╗    ╚██████╗██║  ██║███████╗██████╔╝██║   ██║   ╚██████╔╝")
    print("   ╚═╝╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝   ╚═╝    ╚═════╝ ")
    print()
    menuOpciones = [
        " 1. Avance en cuotas",
        " 2. Avance en efectivo",
        " 3. Consulta de saldo",
        " 4. Pago estado de cuenta",
        " 5. Volver al menú principal"
    ]
    for menu in menuOpciones:
        print(menu)
    print()
    opcion = int(input("N: "))
    if opcion >= 1 and opcion <= len(menuOpciones):
        print()
        if opcion == 1:
            print("En desarrollo...")
        if opcion == 2:
            print("En desarrollo...")
        if opcion == 3:
            print("Su saldo disponible es $" + str(saldo))
            time.sleep(4)
            return MainMenu()
        if opcion == 4:
            print()
            print(" ¿Como desea efectuar este pago?")
            print()
            print(" 1. Con cargo a su Cuenta Corriente")
            print(" 2. Con cargo a su Cuenta Vista")
            print(" 3. Volver al menú principal")
            print()
            opcion = int(input("N: "))
            if opcion >= 1 and opcion <= 3:
                if opcion == 1:
                    print("El monto a pagar es $18.000")
                    print("¿Desea pagarlo?")
                    print()
                    print(" 1. Si")
                    print(" 2. No")
                    print()
                    opcionCargo = int(input("N: "))
                    if opcionCargo == 1 or opcionCargo == 2:
                        if opcionCargo == 1:
                            if saldoCuentaCorriente >= 18000:
                                print("Operación realizada.")
                                print("Gracias por operar con nosotros.")
                                time.sleep(2)
                                MainMenu.exit()
                            else:
                                print("No posee saldo suficiente para realizar la operación.")
                                time.sleep(2)
                                MainMenu.exit()
                        if opcionCargo == 2:
                            print("Gracias por operar con nosotros.")
                            time.sleep(2)
                            MainMenu.exit()
                    else:
                        ErrorCodes.OptionInvalid()
                if opcion == 2:
                    print("El monto a pagar es $20.000")
                    print("¿Desea pagarlo?")
                    print()
                    print(" 1. Si")
                    print(" 2. No")
                    print()
                    opcionCargo = int(input("N: "))
                    if opcionCargo == 1 or opcionCargo == 2:
                        if opcionCargo == 1:
                            if saldoCuentaVista >= 20000:
                                print("Operación realizada.")
                                print("Gracias por operar con nosotros.")
                                time.sleep(2)
                                MainMenu.exit()
                            else:
                                print("No posee saldo suficiente para realizar la operación.")
                                time.sleep(2)
                                MainMenu.exit()
                        if opcionCargo == 2:
                            print("Gracias por operar con nosotros.")
                            time.sleep(2)
                            MainMenu.exit()
                    else:
                        ErrorCodes.OptionInvalid()
                if opcion == 3:
                    time.sleep(2)
                    from MainMenu import Menu
                    return Menu()
            else:
                ErrorCodes.OptionInvalid()
        if opcion == 5:
            print()
            print("Volviendo al menú principal...")
            time.sleep(3)
            from MainMenu import Menu
            return Menu()
    else:
        ErrorCodes.OptionInvalid()


