#             #
#   IMPORTS   #
#             #
import time

import MainMenu
import ErrorCodes
from sys import platform
import os

#             #
#  VARIABLES  #
#             #
validPassword = "1935"
#                #
#  DEF & OTROS   #
#                #
def cls():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")

#                   #
#   INICIO CÓDIGO   #
#                   #

# PIN CORRECTO: 1935 #

def LoginSystem():
    cls()
    print()
    print(" ██╗      ██████╗  ██████╗ ██╗███╗   ██╗")
    print(" ██║     ██╔═══██╗██╔════╝ ██║████╗  ██║")
    print(" ██║     ██║   ██║██║  ███╗██║██╔██╗ ██║")
    print(" ██║     ██║   ██║██║   ██║██║██║╚██╗██║")
    print(" ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║")
    print(" ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝")
    print()
    password = input("Ingrese su PIN: ")
    if password.isnumeric():
        if len(password) == 4:
            if password == validPassword:
                MainMenu.Menu()
            else:
                for intentospass in range(2):
                    password = input("Ingrese su PIN nuevamente: ")
                    if password == validPassword:
                        MainMenu.Menu()
                    else:
                        intentospass += 1
                        print("Contraseña incorrecta.")
                if intentospass == 2:
                    ErrorCodes.TriesLimit()
        else:
            print("Su PIN debe tener 4 números.")
            for intentos in range(2):
                password = input("Ingrese su PIN: ")
                if password.isnumeric() and len(password) == 4:
                    if password == validPassword:
                        MainMenu.Menu()
                    else:
                        print("Contraseña incorrecta.")
                        for intentospass in range(2):
                            password = input("Ingrese su PIN nuevamente: ")
                            if password == validPassword:
                                MainMenu.Menu()
                            else:
                                intentospass += 1
                                print("Contraseña incorrecta.")
                        if intentospass == 2:
                            ErrorCodes.TriesLimit()
                else:
                    intentos += 1
                    print("Su PIN debe tener 4 números.")
            if intentos == 2:
                ErrorCodes.TriesLimit()
    else:
        print("Su PIN sólo puede contener números.")
        for intentos in range(2):
            password = input("Ingrese su PIN: ")
            if password.isnumeric():
                if len(password) == 4:
                    if password == validPassword:
                        MainMenu.Menu()
                    else:
                        print("Contraseña incorrecta.")
                        for intentospass in range(2):
                            password = input("Ingrese su PIN nuevamente: ")
                            if password == validPassword:
                                MainMenu.Menu()
                            else:
                                intentospass += 1
                                print("Contraseña incorrecta.")
                        if intentospass == 2:
                            ErrorCodes.TriesLimit()
                else:
                    print("Su PIN debe tener 4 números.")
            else:
                intentos += 1
                print("Su PIN sólo puede contener números.")
        if intentos == 2:
            ErrorCodes.TriesLimit()

def ResetPassword():
    cls()
    print()
    print("  ██████╗██╗      █████╗ ██╗   ██╗███████╗")
    print(" ██╔════╝██║     ██╔══██╗██║   ██║██╔════╝")
    print(" ██║     ██║     ███████║██║   ██║█████╗")
    print(" ██║     ██║     ██╔══██║╚██╗ ██╔╝██╔══╝")
    print(" ╚██████╗███████╗██║  ██║ ╚████╔╝ ███████╗")
    print("  ╚═════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝")
    print()
    print("    ¿Está seguro de cambiar su clave?")
    print()
    print(" 1. Si")
    print(" 2. No")
    opcion = int(input("N: "))
    if opcion == 1 or opcion == 2:
        if opcion == 1:
            print()
            newpassword = input("Introduzca su nueva clave numérica de 4 dígitos: ")
            if newpassword.isnumeric():
                if len(newpassword) == 4:
                    validPassword = str(newpassword)
                    print()
                    print("¡Clave cambiada con éxito!")
                    time.sleep(3)
                    exit()
                else:
                    print("Su nueva clave debe tener 4 dígitos.")
                    for intentos in range(2):
                        newpassword = input("Introduzca su nueva clave numérica de 4 dígitos: ")
                        if len(newpassword) == 4:
                            validPassword = str(newpassword)
                            print()
                            print("¡Clave cambiada con éxito!")
                            time.sleep(3)
                            exit()
                        else:
                            intentos += 1
                            print("Su nueva clave debe tener 4 dígitos.")
                    if intentos == 2:
                        ErrorCodes.TriesLimit()
            else:
                print("Su nueva clave debe ser de 4 dígitos.")
                for intentos in range(2):
                    newpassword = input("Introduzca su nueva clave numérica de 4 dígitos: ")
                    if len(newpassword) == 4 and newpassword.isnumeric():
                        validPassword = str(newpassword)
                        print()
                        print("¡Clave cambiada con éxito!")
                        time.sleep(3)
                        exit()
                    else:
                        intentos += 1
                        print("Su nueva clave debe tener 4 dígitos.")
                if intentos == 2:
                    ErrorCodes.TriesLimit()
        if opcion == 2:
            print("Cancelando operación...")
            time.sleep(3)
            exit()
    else:
        ErrorCodes.OptionInvalid()