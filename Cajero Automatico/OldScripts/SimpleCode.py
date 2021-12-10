#-----------------#
#   SIMPLE CODE   #
#-----------------#
def main():
    usuario = input("Ingrese Nombre de Usuario: ")
    if len(usuario) >= 3: # LEN = Largo
        password = input("Ingrese su contraseña: ")
        if len(password) >= 3:
            print()
            print(" Bienvenido, ", str(usuario))
            print()
            print("Escoje una opción: ")
            print()
            print("")
            # Aca crean los print de opciones
            opcion = int(input("Ingrese una opción: "))
            if opcion >= 1 and opcion <= 3: # Reemplaza el 3 por la cantidad de opciones que tenga tu menú
                if opcion == 1:
                    print("Codigo que desees")
                if opcion == 2:
                    print("Codigo que desees")
                # Y asi con el resto
            else:
                print("Introduce un número entre 1 a 3.")
                opcion = int(input("Ingrese una opción: "))
        else:
            print("La contraseña debe tener 3 o más carácteres.")
            password = input("Ingrese su contraseña nuevamente: ")
    else:
        print("El nombre de usuario debe contener 3 o más carácteres")
        usuario = input("Ingrese Nombre de Usuario nuevamente: ")

