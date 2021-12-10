#             #
#   IMPORTS   #
#             #
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