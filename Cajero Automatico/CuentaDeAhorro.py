import time
import os
from sys import platform
import MainMenu
import ErrorCodes
def cls():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")

def MainMenu():
    saldo = 1350000
    cls()
    print()
    print("  █████╗ ██╗  ██╗ ██████╗ ██████╗ ██████╗  ██████╗")
    print(" ██╔══██╗██║  ██║██╔═══██╗██╔══██╗██╔══██╗██╔═══██╗")
    print(" ███████║███████║██║   ██║██████╔╝██████╔╝██║   ██║")
    print(" ██╔══██║██╔══██║██║   ██║██╔══██╗██╔══██╗██║   ██║")
    print(" ██║  ██║██║  ██║╚██████╔╝██║  ██║██║  ██║╚██████╔╝")
    print(" ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝")
    print()
    print("       Cuenta de Ahorro")
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
            cls()
            print()
            print(" ██████╗ ███████╗████████╗██╗██████╗  ██████╗ ")
            print(" ██╔══██╗██╔════╝╚══██╔══╝██║██╔══██╗██╔═══██╗")
            print(" ██████╔╝█████╗     ██║   ██║██████╔╝██║   ██║")
            print(" ██╔══██╗██╔══╝     ██║   ██║██╔══██╗██║   ██║")
            print(" ██║  ██║███████╗   ██║   ██║██║  ██║╚██████╔╝")
            print(" ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═╝ ╚═════╝ ")
            print()
            menuGiro = [
                " 1. $10.000",
                " 2. $20.000",
                " 3. $30.000",
                " 4. $40.000",
                " 5. $100.000",
                " 6. $150.000",
                " 7. $200.000",
                " 8. Otro monto"
            ]
            for Montos in menuGiro:
                print(Montos)
            print()
            opcionGiro = int(input("N: "))
            if opcionGiro >= 1 and opcionGiro <= len(menuGiro):
                if opcionGiro == 1:
                    if saldo >= 10000:
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
                            if confirmacion1 == 2:
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
                        print("No cuenta con saldo suficiente para realizar la operación.")                                                               
                if opcionGiro == 2:
                    if saldo >= 20000:
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
                            if confirmacion1 == 2:
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
                        print("No cuenta con saldo suficiente para realizar la operación.")                    
                if opcionGiro == 3:
                    if saldo >= 30000:
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
                            if confirmacion1 == 2:
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
                        print("No cuenta con saldo suficiente para realizar la operación.")                                        
                if opcionGiro == 4:
                    if saldo >= 40000:
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
                            if confirmacion1 == 2:
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
                        print("No cuenta con saldo suficiente para realizar la operación.")                                        
                if opcionGiro == 5:
                    if saldo >= 100000:
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
                            if confirmacion1 == 2:
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
                        print("No cuenta con saldo suficiente para realizar la operación.")                                        
                if opcionGiro == 6:
                    if saldo >= 150000:
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
                            if confirmacion1 == 2:
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
                        print("No cuenta con saldo suficiente para realizar la operación.")                                        
                if opcionGiro == 7:
                    if saldo >= 200000:
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
                            if confirmacion1 == 2:
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
                        print("No cuenta con saldo suficiente para realizar la operación.")                                        
                if opcionGiro == 8:
                    montoRetiro = int(input("Ingrese la cantidad de dinero a retirar: "))
                    print()
                    if saldo >= montoRetiro:
                        print(" ¿Está seguro de querer retirar $", str(montoRetiro), "?")
                        print()
                        print(" 1. Si")
                        print(" 2. No")
                        print()
                        confirmacion6 = int(input("N: "))
                        if confirmacion6 == 1 or confirmacion6 == 2:
                            if confirmacion6 == 1:
                                saldo -= montoRetiro
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
                    else:
                        print("Lamentablemente no cuenta con el saldo solicitado.")                    
            else:
                ErrorCodes.OptionInvalid()
        
        if opcion == 2:
            print("Su saldo disponible es $" + str(saldo))
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
                    print(" Gracias por operar con nosotros.")
                    time.sleep(2)
                    print("Volviendo al menú principal...")
                    time.sleep(2)
                    MainMenu.Menu()
                if BackMenu == 2:
                    print(" Gracias por operar con nosotros.")
                    time.sleep(4)
                    MainMenu.exit()
        if opcion == 3:
            from MainMenu import Menu
            return Menu()
    else:
        ErrorCodes.OptionInvalid()