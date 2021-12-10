import time
import os
import MainMenu
from sys import platform
def cls():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")

def TriesLimit():
    cls()
    print()
    print("  ███████╗██████╗ ██████╗  ██████╗ ██████╗")
    print("  ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗")
    print("  █████╗  ██████╔╝██████╔╝██║   ██║██████╔╝")
    print("  ██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗")
    print("  ███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║")
    print("  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝")
    print()
    print(" Has superado el límite de intentos.")
    time.sleep(3)
    MainMenu.exit()

def OptionInvalid():
    cls()
    print()
    print("  ███████╗██████╗ ██████╗  ██████╗ ██████╗")
    print("  ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗")
    print("  █████╗  ██████╔╝██████╔╝██║   ██║██████╔╝")
    print("  ██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗")
    print("  ███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║")
    print("  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝")
    print()
    print(" La opción introducida es inválida.")
    time.sleep(3)
    MainMenu.exit()