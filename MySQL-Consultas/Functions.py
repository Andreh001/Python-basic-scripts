import time
from subprocess import check_call
def clipboard(txt):
    cmd = 'echo '+txt.strip()+'|clip'
    return check_call(cmd, shell=True)
import Menu

def CreateDB():
    print()
    dbname = input("Introduzca un nombre para su base de datos: ")
    print()
    clipboard("CREATE DATABASE " + str(dbname) + ";")
    print("Consulta copiada al portapapeles, pégalo utilizando CTRL + V")
    time.sleep(3)
    print("Volviendo al menú principal...")
    return Menu.MainMenu()

def Select():
    Menu.cls()
    print()
    print(" ███████╗███████╗██╗     ███████╗ ██████╗████████╗")
    print(" ██╔════╝██╔════╝██║     ██╔════╝██╔════╝╚══██╔══╝")
    print(" ███████╗█████╗  ██║     █████╗  ██║        ██║")
    print(" ╚════██║██╔══╝  ██║     ██╔══╝  ██║        ██║")
    print(" ███████║███████╗███████╗███████╗╚██████╗   ██║")
    print(" ╚══════╝╚══════╝╚══════╝╚══════╝ ╚═════╝   ╚═╝")
    print()
    cantlist = int(input("Ingrese la cantidad de listas a usar: "))
    while cantlist < 1:
        print("No puedes ingresar números negativos.")
        cantlist = int(input("Ingrese la cantidad de listas a usar: "))
    else:
        listtotal = []
        for List in range(cantlist):
            list = input("Ingrese el nombre de la lista N" + str(List + 1) + ": ")
            listtotal.append(str(list))
        print("Guardado, continuando al siguiente paso...")
        time.sleep(1)


def Roles():
    Menu.cls()
    print()
    print(" ██████╗  ██████╗ ██╗     ███████╗███████╗")
    print(" ██╔══██╗██╔═══██╗██║     ██╔════╝██╔════╝")
    print(" ██████╔╝██║   ██║██║     █████╗  ███████╗")
    print(" ██╔══██╗██║   ██║██║     ██╔══╝  ╚════██║")
    print(" ██║  ██║╚██████╔╝███████╗███████╗███████║")
    print(" ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝")
    print()
    print("        Seleccione una opción")
    print()
    rolesMenu = [
        "1. Crear Rol",
        "2. Otorgar privilegios a Rol",
        "3. Asignar rol a usuario",
        "4. Establecer rol predeterminado",
        "5. Revocar permisos a rol",
        "6. Restaurar permisos a un rol",
        "7. Eliminar rol",
        "8. Volver al menú"
    ]
    for MenuRoles in rolesMenu:
        print(MenuRoles)
    print()
    option = int(input("N: "))
    while option < 1 or option > len(rolesMenu):
        print("Opción errónea.")
        option = int(input("N: "))
    else:
        if option == 1:
            cantroles = int(input("¿Cuántos roles quiere crear?: "))
            while cantroles < 1:
                print("No puedes ingresar números negativos.")
                cantroles = int(input("¿Cuántos roles quiere crear?: "))
            else:
                rolename = []
                for roles in range(cantroles):
                    role = input("Nombre de rol N" + str(roles + 1) + ": ")
                    rolename.append(str(role))
                clipboard("CREATE ROLE " + str(rolename) + ";")
                print("Consulta copiada al portapapeles, pégalo utilizando CTRL + V y recuerda borrar los [ ] y las comillas, no borres las comas.")
                time.sleep(10)
                print("Volviendo al menú principal...")
                return Roles()
        if option == 2:
            print()
            dbname = input("Ingrese el nombre de la base de datos: ")
            rolename = input("Ingrese el nombre del rol: ")
            print()
            print(" Privilegios: ALL, SELECT, INSERT, UPDATE O DELETE")
            permissions = input("Ingrese los privilegios a otorgar, separados y con comas: ")
            clipboard("GRANT " + str(permissions) + " ON " + str(dbname) + ".*" + " TO " + str(rolename) + ";")
            print("Consulta copiada al portapapeles, pégalo utilizando CTRL + V")
            time.sleep(3)
            print("Volviendo al menú...")
            return Roles()
        if option == 3:
            print()
            namerole = input("Ingrese el nombre del rol a asignar: ")
            username = input("Ingrese el nombre de usuario: ")
            clipboard("GRANT " + str(namerole) + " TO " + str(username) + "@localhost;")
            print("Consulta copiada al portapapeles, pégalo utilizando CTRL + V")
            print("Si deseas agregar más de 1 rol o mas de 1 cuenta de usuario, ejemplo: GRANT rol1, rol2 to user1@localhost, user2@localhost;")
            time.sleep(10)
            print("Volviendo al menú...")
            return Roles()
        if option == 4:
            defaultrole = input("Ingrese el nombre del rol a predeterminar: ")
            print()
            clipboard("SET DEFAULT ROLE ALL TO " + str(defaultrole) + "@localhost;")
            print("Consulta copiada al portapapeles, pégalo utilizando CTRL + V")
            time.sleep(3)
            print("Volviendo al menú...")
            return Roles()
        if option == 5:
            print()
            dbname = input("Ingrese el nombre de la base de datos: ")
            rolename = input("Ingrese el nombre del rol: ")
            print()
            print(" Privilegios: ALL, SELECT, INSERT, UPDATE O DELETE")
            permissions = input("Ingrese los privilegios a revocar, separados y con comas: ")
            clipboard("REVOKE " + str(permissions) + " ON " + str(dbname) + ".*" + " FROM " + str(rolename) + ";")
            print("Consulta copiada al portapapeles, pégalo utilizando CTRL + V")
            time.sleep(3)
            print("Volviendo al menú...")
            return Roles()
        if option == 6:
            print()
            dbname = input("Ingrese el nombre de la base de datos: ")
            rolename = input("Ingrese el nombre del rol: ")
            print()
            print(" Privilegios: ALL, SELECT, INSERT, UPDATE O DELETE")
            permissions = input("Ingrese los privilegios a otorgar, separados y con comas: ")
            clipboard("GRANT " + str(permissions) + " ON " + str(dbname) + ".*" + " FROM " + str(rolename) + ";")
            print("Consulta copiada al portapapeles, pégalo utilizando CTRL + V")
            time.sleep(3)
            print("Volviendo al menú...")
            return Roles()
        if option == 7:
            delrole = input("Ingrese el nombre del rol a eliminar: ")
            clipboard("DROP ROLE " + str(delrole) + ";")
            print()
            print("Consulta copiada al portapapeles, pégalo utilizando CTRL + V")
            print("Si deseas eliminar más de 1 rol, ejemplo: DROP ROLE rol1, rol2, rol3;")
            time.sleep(5)
            print("Volviendo al menú...")
            return Roles()
        if option == 8:
            print("Volviendo al menú principal...")
            time.sleep(3)
            return Menu.MainMenu()

def DropDatabase():
    print()
    dropdb = input("Introduzca el nombre de la base de datos a borrar: ")
    print()
    clipboard("DROP DATABASE " + str(dropdb) + ";")
    print("Consulta copiada al portapapeles, pégalo utilizando CTRL + V")
    time.sleep(3)
    print("Volviendo al menú...")
    return Menu.MainMenu()