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

def MainMenu():
    saldo = 553000
    cls()
    print()
    print("  ██████╗████████╗ █████╗      ██████╗ ██████╗ ██████╗ ██████╗ ██╗███████╗███╗   ██╗████████╗███████╗")
    print(" ██╔════╝╚══██╔══╝██╔══██╗    ██╔════╝██╔═══██╗██╔══██╗██╔══██╗██║██╔════╝████╗  ██║╚══██╔══╝██╔════╝")
    print(" ██║        ██║   ███████║    ██║     ██║   ██║██████╔╝██████╔╝██║█████╗  ██╔██╗ ██║   ██║   █████╗")
    print(" ██║        ██║   ██╔══██║    ██║     ██║   ██║██╔══██╗██╔══██╗██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝")
    print(" ╚██████╗   ██║   ██║  ██║    ╚██████╗╚██████╔╝██║  ██║██║  ██║██║███████╗██║ ╚████║   ██║   ███████╗")
    print("  ╚═════╝   ╚═╝   ╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝")
    print()
    print(" Por favor, seleccione la operación que desea realizar")
    print()
    menuOpciones = [
        " 1. Giro rápido por $5.000",
        " 2. Giro rápido por $15.000",
        " 3. Giro rápido por $50.000",
        " 4. Giro por otro monto",
        " 5. Consulta de saldo",
        " 6. Volver al menú principal"
    ]
    for menu in menuOpciones:
        print(menu)
    print()
    opcion = int(input("N: "))
    if opcion >= 1 and opcion <= len(menuOpciones):
        if opcion == 1:
            print(" ¿Desea impresión de comprobante?")
            print()
            print(" 1. Si")
            print(" 2. No")
            print()
            confirmacion1 = int(input("N: "))
            if confirmacion1 == 1 or confirmacion1 == 2:
                if confirmacion1 == 1:
                    print(" Imprimiendo comprobante...")
                    time.sleep(3)
                    input(" Por favor, retire su dinero.")
                    time.sleep(2)
                    print(" Gracias por operar con nosotros.")
                    time.sleep(4)
                    MainMenu.exit()
                if confirmacion1 == 2:
                    time.sleep(3)
                    print(" Por favor, retire su dinero.")
                    time.sleep(2)
                    print(" Gracias por operar con nosotros.")
                    time.sleep(4)
                    MainMenu.exit()
            else:
                ErrorCodes.OptionInvalid()
        if opcion == 2:
            print(" ¿Desea impresión de comprobante?")
            print()
            print(" 1. Si")
            print(" 2. No")
            print()
            confirmacion2 = int(input("N: "))
            if confirmacion2 == 1 or confirmacion2 == 2:
                if confirmacion2 == 1:
                    print(" Imprimiendo comprobante...")
                    time.sleep(3)
                    input(" Por favor, retire su dinero.")
                    time.sleep(2)
                    print(" Gracias por operar con nosotros.")
                    time.sleep(4)
                    MainMenu.exit()
                if confirmacion2 == 2:
                    time.sleep(3)
                    print(" Por favor, retire su dinero.")
                    time.sleep(2)
                    print(" Gracias por operar con nosotros.")
                    time.sleep(4)
                    MainMenu.exit()
            else:
                ErrorCodes.OptionInvalid()
        if opcion == 3:
            print(" ¿Desea impresión de comprobante?")
            print()
            print(" 1. Si")
            print(" 2. No")
            print()
            confirmacion3 = int(input("N: "))
            if confirmacion3 == 1 or confirmacion3 == 2:
                if confirmacion3 == 1:
                    print(" Imprimiendo comprobante...")
                    time.sleep(3)
                    input(" Por favor, retire su dinero.")
                    time.sleep(2)
                    print(" Gracias por operar con nosotros.")
                    time.sleep(4)
                    MainMenu.exit()
                if confirmacion3 == 2:
                    time.sleep(3)
                    print(" Por favor, retire su dinero.")
                    time.sleep(2)
                    print(" Gracias por operar con nosotros.")
                    time.sleep(4)
                    MainMenu.exit()
            else:
                ErrorCodes.OptionInvalid()
        if opcion == 4:
            monto = int(input(" Ingrese la cantidad de dinero a retirar: "))
            print()
            if monto < saldo:
              print("Lamentablemente no cuenta con el saldo solicitado.")
              time.sleep(3)
              MainMenu.exit()
            elif monto >= saldo:
                print(" ¿Está seguro de querer retirar $", str(monto), "?")
                print()
                print(" 1. Si")
                print(" 2. No")
                print()
                confirmacion6 = int(input("N: "))
                if confirmacion6 == 1 or confirmacion6 == 2:
                    if confirmacion6 == 1:
                        saldo -= monto
                        print()
                        print(" ¿Desea impresión de comprobante?")
                        print()
                        print(" 1. Si")
                        print(" 2. No")
                        print()
                        confirmacion5 = int(input("N: "))
                        if confirmacion5 == 1 or confirmacion5 == 2:
                            if confirmacion5 == 1:
                                print(" Imprimiendo comprobante...")
                                time.sleep(3)
                                input(" Por favor, retire su dinero.")
                                time.sleep(2)
                                print()
                                print(" Gracias por operar con nosotros.")
                                time.sleep(4)
                                print()
                                print(" ¿Desea volver al menú principal?")
                                print()
                                print(" 1. Si")
                                print(" 2. No")
                                print()
                                BackMenu = int(input("N: "))
                                if BackMenu == 1 or BackMenu == 2:
                                    if BackMenu == 1:
                                        print("Volviendo al menú principal...")
                                        time.sleep(2)
                                        MainMenu.Menu()
                                    if BackMenu == 2:
                                        print(" Gracias por operar con nosotros.")
                                        time.sleep(4)
                                        MainMenu.exit()
                                else:
                                    ErrorCodes.OptionInvalid()
                            if confirmacion5 == 2:
                                time.sleep(3)
                                print(" Por favor, retire su dinero.")
                                time.sleep(2)
                                print(" Gracias por operar con nosotros.")
                                time.sleep(4)
                                print()
                                print(" ¿Desea volver al menú principal?")
                                print()
                                print(" 1. Si")
                                print(" 2. No")
                                print()
                                BackMenu = int(input("N: "))
                                if BackMenu == 1 or BackMenu == 2:
                                    if BackMenu == 1:
                                        print("Volviendo al menú principal...")
                                        time.sleep(2)
                                        MainMenu.Menu()
                                    if BackMenu == 2:
                                        print(" Gracias por operar con nosotros.")
                                        time.sleep(4)
                                        MainMenu.exit()
                                else:
                                    ErrorCodes.OptionInvalid()
                        else:
                            ErrorCodes.OptionInvalid()
                if confirmacion6 == 2:
                    print("Volviendo al menú principal...")
                    time.sleep(2)
                    MainMenu.Menu()
            else:
                ErrorCodes.OptionInvalid()
        if opcion == 5:
            print("Su saldo disponible es $" + str(saldo))
            time.sleep(4)
            MainMenu.exit()
        if opcion == 6:
            from MainMenu import Menu
            return Menu()
    else:
        ErrorCodes.OptionInvalid()