#----------------IMPORTS------------------#
from Clases.Bibliotecario import Bibliotecario
from Clases.Libro import Libro
import time
import os
from sys import platform
import getpass
#------------------FIN--------------------#


#----------------VARIABLES------------------#
libro1 = Libro(16, "A fuego lento", "Paula Hawkins", 1)
libro2 = Libro(8, "Verdades enterradas", "Hjorth & Roenfeldt", 0)
libro3 = Libro(10, "La Bestia", "Carmen Mola", 1)
libro4 = Libro(19, "Últimos dias en Berlín", "Paloma Sánchez-Garnica", 0)
libro5 = Libro(5, "La cuenta atrás para el verano", "La Vecina Rubia", 1)
libro6 = Libro(7, "Los vencejos", "Fernando Aramburu", 0)
libro7 = Libro(3, "¿Un último vaile, milady?", "Megan Maxwell", 1)
libro8 = Libro(4, "Sira", "María Dueñas", 0)
libro9 = Libro(14, "Las tres hermanas", "Heather Morris", 1)
libro10 = Libro(17, "Primera persona del singular", "Haruki Murakami", 0)
bibliotecario = Bibliotecario(210647682, "Andy Luchin Piton", "Test%123")
listaLibros = [libro1, libro2, libro3, libro4, libro5, libro6, libro7, libro8, libro9, libro10]
libroexistente = None
nodisponible = None
#-------------------FIN----------------------#


#-----------------CODE--------------------#
def clear():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system("clear")
    elif platform == "win32":
        os.system("cls")

rut = int(input("Ingrese su RUT: "))
password = getpass.getpass("Ingrese su contraseña: ")
if bibliotecario.rut == rut:
    validacion = bibliotecario.validarUsuario(password)
    if validacion:
        print("\n¡Ingreso existoso!\n\nReedirigiendo...")
        time.sleep(2)
        while True:
            clear()
            print(f'''
    ██████╗ ██╗██████╗ ██╗     ██╗ ██████╗ ████████╗███████╗ ██████╗ █████╗ 
    ██╔══██╗██║██╔══██╗██║     ██║██╔═══██╗╚══██╔══╝██╔════╝██╔════╝██╔══██╗
    ██████╔╝██║██████╔╝██║     ██║██║   ██║   ██║   █████╗  ██║     ███████║
    ██╔══██╗██║██╔══██╗██║     ██║██║   ██║   ██║   ██╔══╝  ██║     ██╔══██║
    ██████╔╝██║██████╔╝███████╗██║╚██████╔╝   ██║   ███████╗╚██████╗██║  ██║
    ╚═════╝ ╚═╝╚═════╝ ╚══════╝╚═╝ ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝                                                                   
            
                        ¡Bienvenido {bibliotecario.nombre}!

   ____             _                             _ _                       _ _     _           
  / __ \           (_)                           | (_)                     (_) |   | |          
 | |  | |_ __   ___ _  ___  _ __   ___  ___    __| |_ ___ _ __   ___  _ __  _| |__ | | ___  ___ 
 | |  | | '_ \ / __| |/ _ \| '_ \ / _ \/ __|  / _` | / __| '_ \ / _ \| '_ \| | '_ \| |/ _ \/ __|
 | |__| | |_) | (__| | (_) | | | |  __/\__ \ | (_| | \__ \ |_) | (_) | | | | | |_) | |  __/\__ \ 
  \____/| .__/ \___|_|\___/|_| |_|\___||___/  \__,_|_|___/ .__/ \___/|_| |_|_|_.__/|_|\___||___/
        | |                                              | |                                    
        |_|                                              |_|                                    


    1. Listar todos los libros.
    2. Listar libros disponibles.
    3. Listar libros prestados.
    4. Realizar préstamo.
    5. Realizar devolución.
    6. Salir.

''')
            option = int(input("Ingrese una opción: "))
            while option < 1 or option > 6:
                print("Opción inválida, ingrese un número entre 1 y 6.")
                option = int(input("Ingrese una opción: "))
            else:
                if option == 1:
                    clear()
                    for libros in listaLibros:
                        libros.verLibro()
                    time.sleep(10)
                    print("\nVolviendo al menú...")
                    time.sleep(2)

                if option == 2:
                    for libros in listaLibros:
                        libros.verLibrosDisponibles()
                    print("Volviendo al menú...")
                    time.sleep(5)

                if option == 3:
                    for libros in listaLibros:
                        libros.verLibrosPrestados()
                    print("Volviendo al menú...")
                    time.sleep(5)

                if option == 4:
                    num_libro = int(input("Ingrese el ISBN del libro: "))
                    for libro in listaLibros:
                        if libro.isbn == num_libro:
                            libro.realizarPrestamo(num_libro)
                            print("Volviendo al menú...")
                            time.sleep(5)

                if option == 5:
                    num_libro = int(input("Ingrese el ISBN del libro: "))
                    for libro in listaLibros:
                        if libro.isbn == num_libro:
                            libro.realizarDevolucion(num_libro)
                            print("Volviendo al menú..")
                            time.sleep(5)

                if option == 6:
                    clear()
                    print("Saliendo...")
                    time.sleep(2)
                    exit()
    else:
        print("\nLa contraseña ingresada es incorrecta.")
        time.sleep(3)
        exit()
else:
    print("\nNo existe ningún bibliotecario en nuestros sistemas con el RUT ingresado.")
    time.sleep(3)
    exit()
#------------------FIN--------------------#