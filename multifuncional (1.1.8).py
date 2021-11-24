#                           #
#       IMPORTS & DEF       #
#                           #

import ctypes
import os
import sys
def cls():
    os.system("cls")
import time
from datetime import date
from sys import platform
import datetime
def animated_print(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
        

#                           #
#          VARIABLES        #
#                           #

version = "1.1.8" # NO MODIFICAR
MessageBox = ctypes.windll.user32.MessageBoxW
updateURL = "http://andreh001.ml/multifuncional" # NO MODIFICAR
horaActual = datetime.datetime.now() # NO MODIFICAR
fechaActual = date.today() # NO MODIFICAR
diaActual = fechaActual.day # NO MODIFICAR
mesActual = fechaActual.month # NO MODIFICAR
anoActual = fechaActual.year # NO MODIFICAR
ciudades = ["Santiago"] # MODIFICAR SOLO SI SABES LO QUE HACES
Discord = "Andreh001#5074" # NO MODIFICAR
Telegram = "@Andreh001" # NO MODIFICAR
Email = "daee@siglo.host" # NO MODIFICAR
Autor = "Diego Elos Espinoza" # NO MODIFICAR

#---------------------------#
#                           #
#           START           #
#                           #
#---------------------------#   
if platform == "win32":       
    if Discord == "Andreh001#5074" and Telegram == "@Andreh001" and Email == "daee@siglo.host" and Autor == "Diego Elos Espinoza": # NO MODIFICAR, MEREZCO CREDITOS POR EL TRABAJO, ¿NO?
        #                           #
        #           START           #
        #                           #      
        cmd = "color 0A"
        os.system(cmd)           
        try:
            import requests
        except ModuleNotFoundError:
            print("Este equipo no cuenta con una librería necesaria para el funcionamiento del programa.")
            time.sleep(2)
            print()
            print("Instalaremos automáticamente la libreria en unos segundos...")
            time.sleep(2)
            print()
            print("Recuerda que debes tener conexión a internet para que el proceso se complete correctamente.")
            print()
            time.sleep(4)
            os.system('cmd /c "py -m pip install requests"')
            time.sleep(2)
            print()
            print("¡Instalado correctamente!")
            print()
            exit(input("Presione la tecla Enter para salir, una vez cerrado, vuelva a abrir el programa.")) 

        MessageBox(None, 'Si el programa no muestra nada después de 30 segundos, ciérrelo y vuelva a abrirlo.', 'Multifuncional v' + str(version), 0)

        lastversion = requests.get("http://andreh001.ml/uploads/multifuncional-version.txt").text # NO MODIFICAR
        if version > lastversion:
         
            betatesters = requests.get("http://andreh001.ml/betatesters.txt").text # NO MODIFICAR
            print()
            print(" ████████╗███████╗███████╗████████╗███████╗██████╗ ")
            print(" ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗")
            print("    ██║   █████╗  ███████╗   ██║   █████╗  ██████╔╝")
            print("    ██║   ██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗")
            print("    ██║   ███████╗███████║   ██║   ███████╗██║  ██║")
            print("    ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝")
            print()            
            betatesterscode = int(input("Introduzca su código de Beta Tester: "))
            for betatesterscode in betatesters.split("\n"):
                print()
                print("Acceso concedido, reedirigiendo en 5 segundos...")
                time.sleep(5)
                cls()
                break
            else: 
                print()
                print("Acceso denegado.")
                print("No existe ningún Beta Tester con ese código.")
                time.sleep(3)
                exit()
        print()
        print(" ███╗   ███╗███████╗███╗   ██╗██╗   ██╗")
        print(" ████╗ ████║██╔════╝████╗  ██║██║   ██║")
        print(" ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║")
        print(" ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║")
        print(" ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝")
        print(" ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ")
        print()         
        print()
        animated_print(" ¡Bienvenido al menú multifuncional!")
        print()
        time.sleep(1.0)
        print()
        print(" Creado por " + Autor)
        print()
        time.sleep(1.0)
        print(" Discord: " + Discord)
        print(" Telegram: " + Telegram)
        print(" Email: " + Email)
        time.sleep(1.0)
        print()
        print(" Versión: " + version)
        if lastversion > version:
            print()
            print("¡Nueva versión encontrada!")
            print("  Versión nueva: " + lastversion)
            print()
            print(" Descarga la nueva versión desde:")
            print(updateURL)
            time.sleep(5.0)
        if version > lastversion:
            print(" Versión para Beta tester's")
            time.sleep(1.0)
        print()
        if horaActual.hour >= 0 and horaActual.hour <= 11:
            print(" La fecha y hora actual es " + str(fechaActual.day) + "/" + str(fechaActual.month) + "/" + str(fechaActual.year) + " - " + str(horaActual.hour)+ ":" + str(horaActual.minute) + " AM")
        if horaActual.hour >= 12:
            print(" La fecha y hora actual es " + str(fechaActual.day) + "/" + str(fechaActual.month) + "/" + str(fechaActual.year) + " - " + str(horaActual.hour)+ ":" + str(horaActual.minute) + " PM")
        time.sleep(1.0)
        print()
        print(" -=- Opciones disponibles -=-")
        print()
        print(" 1. Cálculos.")
        print(" 2. Listas.")
        print(" 3. Boolean's (True & False).")
        print(" 4. If, else y while.")
        print(" 5. Bucle For.")
        print(" 6. Actividades realizadas.")
        print(" 7. Información del programa.")
        print(" 8. Participar en programa Beta Tester.")
        print(" 9. Salir.")
        print()
        menu = int(input("Escoja una opción: "))    
        while menu >= 1 and menu <= 9:
            
            #                   #
            #       OP 1        #
            #                   #
            if menu == 1:
                cls()
                print()
                print(" ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      ██████╗ ")
                print("██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔═══██╗")
                print("██║     ███████║██║     ██║     ██║   ██║██║     ██║   ██║")
                print("██║     ██╔══██║██║     ██║     ██║   ██║██║     ██║   ██║")
                print("╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗╚██████╔╝")
                print(" ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ")
                print() 
                print(" -=- Opciones Disponibles -=-")
                print()
                print(" 1. Calcular promedio (4 notas).")
                print(" 2. Sumar.")
                print(" 3. Restar.")
                print(" 4. Multiplicar.")
                print(" 5. Dividir.")
                print(" 6. Salir.")
                calculopregunta = int(input(" Escoja una opción: "))
                print()
                while calculopregunta >= 1 and calculopregunta <= 6:
                    if calculopregunta == 1:
                        nota1 = float(input("Ingrese la primera nota: "))
                        nota2 = float(input("Ingrese la segunda nota: "))
                        nota3 = float(input("Ingrese la tercera nota: "))
                        nota4 = float(input("Ingrese la cuarta nota: "))
                        promedio = (nota1 + nota2 + nota3 + nota4) / 4
                        print()
                        while nota1 >= 1 and nota1 <= 7.0 and nota2 >=1 and nota2 <=7.0 and nota3 >=1 and nota3 <= 7.0 and nota4 >=1 and nota4 <=7.0:
                            if promedio < 4.0:
                                print("Su promedio es: " + str(promedio))
                                print("Lamentablemente reprobó el ramo.")
                                print()
                                exit(input("Presione la tecla Enter para salir."))
                            else:
                                print("Su promedio es: " + str(promedio))    
                                print("¡Aprobó el ramo!")
                                print()
                                exit(input("Presione la tecla Enter para salir."))
                        else:
                            print()
                            print("Introduce notas entre 1 a 7.")
                            print()
                            time.sleep(2.0)

                    if calculopregunta == 2:
                        suma1 = int(input("Ingrese el primer número para sumar: "))
                        suma2 = int(input("Ingrese el segundo número para sumar: "))
                        sumatotal = suma1 + suma2
                        while suma1 >= 1 and suma2 >= 1:
                            print()
                            print("La suma de los dos dígitos es: " + str(sumatotal))
                            print()
                            exit(input("Presione la tecla Enter para salir."))
                        else:
                            print()
                            print("Introduce números mayor a 1.")
                            print()
                            time.sleep(2.0)

                    if calculopregunta == 3:
                        resta1 = int(input("Ingrese el primer número para restar: "))
                        resta2 = int (input("Ingrese el segundo número para restar: "))
                        restatotal = resta1 - resta2
                        while resta1 >= 1 and resta2 >= 1:
                            print()
                            print("La resta de los dos dígitos es: " + str(restatotal))
                            print()
                            exit(input("Presione la tecla Enter para salir."))  
                        else:
                            print()
                            print("Introduce números mayor a 1.")
                            print()
                            time.sleep(2.0)

                    if calculopregunta == 4:
                        multipl1 = int(input("Ingrese el primer número para multiplicar: "))
                        multipl2 = int(input("Ingrese el segundo número para multiplicar: "))
                        multipltotal = multipl1 * multipl2
                        while multipl1 >= 1 and multipl2 >= 1:
                            print()
                            print("La multiplicación de los dos dígitos es: " + str(multipltotal))
                            print()
                            exit(input("Presione la tecla Enter para salir."))
                        else:
                            print()
                            print("Introduce números mayor a 1.")
                            print()
                            time.sleep(2.0)

                    if calculopregunta == 5:
                        dividir1 = int(input("Ingrese el primer número para dividir: "))
                        dividir2 = int(input("Ingrese el segundo número para dividir: "))    
                        dividirtotal = dividir1 / dividir2
                        while dividir1 >= 1 and dividir2 >= 1:
                            print()
                            print("La división de los dos dígitos es: " + str(dividirtotal))
                            print()
                            exit(input("Presione la tecla Enter para salir."))
                        else:
                            print()
                            print("Introduce números mayor a 1.")
                            print()
                            time.sleep(2.0)

                    if calculopregunta == 6:
                        print("Saliendo en 5 segundos...")
                        time.sleep(4.0)
                        exit()
                else:
                    print()
                    print("Introduce un número entre 1 a 6.")
                    print()
                    time.sleep(2)            
            #                   #
            #       OP 2        #
            #                   #
            if menu == 2:
                cls()
                print()
                print(" ██╗     ██╗███████╗████████╗ █████╗ ███████╗")
                print(" ██║     ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝")
                print(" ██║     ██║███████╗   ██║   ███████║███████╗")
                print(" ██║     ██║╚════██║   ██║   ██╔══██║╚════██║")
                print(" ███████╗██║███████║   ██║   ██║  ██║███████║")
                print(" ╚══════╝╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝")
                print()
                print(" -=- Opciones Disponibles -=-=")
                print()
                print(" 1. Listar Ciudades.")
                print(" 2. Agregar ciudad.")
                print(" 3. Eliminar ciudad.")
                print(" 4. Salir.")
                print()
                listaspregunta = int(input(" Escoja una opción: "))
                print()
                while listaspregunta >= 1 and listaspregunta <= 4:
                    if listaspregunta == 1:
                        print("Las ciudades almacenadas son: " + str(ciudades))
                        print()
                        exit(input("Presione la tecla Enter para salir."))

                    if listaspregunta == 2:
                        agregarciudad = str(input("Ingrese el nombre de la ciudad a agregar: "))
                        ciudades.append(agregarciudad)
                        print("¡Ciudad agregada!")
                        print()
                        print("¿Desea listar las ciudades actualizadas?")
                        print()
                        print("1. Sí.")
                        print("2. No.")
                        preguntaciudad = int(input("Escoje una opción: "))
                        while preguntaciudad == 1 or preguntaciudad == 2:
                            if preguntaciudad == 1:
                                print()
                                print("Las ciudades actualizadas son: " + str(ciudades))
                                print()
                                exit(input("Presione la tecla Enter para salir."))
                            if preguntaciudad == 2:
                                print()
                                exit(input("Presione la tecla Enter para salir."))
                        else:
                            print("Introduce un número entre 1 a 2.")

                    if listaspregunta == 3:
                        eliminarciudad = str(input("Ingrese el nombre de la ciudad a eliminar: "))
                        print()
                        ciudades.remove(eliminarciudad)
                        print("Se eliminó la ciudad " + str(eliminarciudad))
                        print()
                        print("¿Desea listar las ciudades actualizadas?")
                        print()
                        print("1. Sí.")
                        print("2. No.")
                        print()
                        preguntaciudad = int(input("Escoje una opción: "))
                        while preguntaciudad == 1 or preguntaciudad == 2:
                            if preguntaciudad == 1:
                                print()
                                print("Las ciudades actualizadas son: " + str(ciudades))
                                print()
                                exit(input("Presione la tecla Enter para salir."))
                            if preguntaciudad == 2:
                                print()
                                exit(input("Presione la tecla Enter para salir."))
                        else:
                            print("Introduce un número del 1 al 2.")  

                    if listaspregunta == 4:
                        print("Saliendo en 5 segundos...")
                        time.sleep(4.0)
                        exit()                      
                else:
                    print()
                    print("Introduce un número entre 1 a 4.")
                    print()
                    listaspregunta = int(input(" Escoja una opción: "))
            #                   #
            #       OP 3        #
            #                   #
            if menu == 3:
                cls()
                print()
                print(" ██████╗  ██████╗  ██████╗ ██╗     ███████╗ █████╗ ███╗   ██╗")
                print(" ██╔══██╗██╔═══██╗██╔═══██╗██║     ██╔════╝██╔══██╗████╗  ██║")
                print(" ██████╔╝██║   ██║██║   ██║██║     █████╗  ███████║██╔██╗ ██║")
                print(" ██╔══██╗██║   ██║██║   ██║██║     ██╔══╝  ██╔══██║██║╚██╗██║")
                print(" ██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗██║  ██║██║ ╚████║")
                print(" ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝")
                print()                                         
                print(" Para comenzar...")
                time.sleep(2.0)
                print()
                print(" ¿Sabes que es un Boolean?")
                print()
                print(" 1. Sí.")
                print(" 2. No.")        
                print()
                preguntaboolean = int(input(" Escoje una opción: "))
                while preguntaboolean == 1 or preguntaboolean == 2:
                    if preguntaboolean == 1:
                        print()
                        print()
                        print(" ¡Excelente!, continuemos...")
                        time.sleep(3.0)
                        cls()
                        print()
                        print(" ██████╗  ██████╗  ██████╗ ██╗     ███████╗ █████╗ ███╗   ██╗")
                        print(" ██╔══██╗██╔═══██╗██╔═══██╗██║     ██╔════╝██╔══██╗████╗  ██║")
                        print(" ██████╔╝██║   ██║██║   ██║██║     █████╗  ███████║██╔██╗ ██║")
                        print(" ██╔══██╗██║   ██║██║   ██║██║     ██╔══╝  ██╔══██║██║╚██╗██║")
                        print(" ██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗██║  ██║██║ ╚████║")
                        print(" ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝")
                        print()       
                        print(" -=- Opciones Disponibles -=-")   
                        print()                       
                        print(" 1. Crear variable y establecer valor.")
                        print(" 2. Salir.")
                        print()
                        opcionesboolean = int(input("Escoja una opción: "))
                        print()
                        while opcionesboolean == 1 or opcionesboolean == 2:
                            if opcionesboolean == 1:
                                cls()
                                print()
                                print(" ██████╗  ██████╗  ██████╗ ██╗     ███████╗ █████╗ ███╗   ██╗")
                                print(" ██╔══██╗██╔═══██╗██╔═══██╗██║     ██╔════╝██╔══██╗████╗  ██║")
                                print(" ██████╔╝██║   ██║██║   ██║██║     █████╗  ███████║██╔██╗ ██║")
                                print(" ██╔══██╗██║   ██║██║   ██║██║     ██╔══╝  ██╔══██║██║╚██╗██║")
                                print(" ██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗██║  ██║██║ ╚████║")
                                print(" ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝")
                                print()                               
                                print(" Nota: esta variable será TEMPORAL.")
                                print()
                                variablepregunta = str(input(" Ingrese nombre para la variable: "))
                                while variablepregunta.isalpha():
                                    print()
                                    print("¡Variable creada!")
                                    print()
                                    time.sleep(2.0)
                                    print()
                                    print("Pero espera...")
                                    time.sleep(1.0)
                                    print()
                                    print("Aquí falta algo...")
                                    time.sleep(1.5)
                                    print()
                                    print("¡Definir la variable!")
                                    time.sleep(1.0)
                                    print()
                                    definirvariable = str(input("Ingrese la variable Verdadero o Falso (True o False): "))
                                    print()
                                    while definirvariable == "True" or definirvariable == "False":
                                        if definirvariable == "True":
                                            print("Se estableció " + str(variablepregunta) + " a True.")
                                            print()
                                            variablepregunta = True
                                            exit(input("Presione la tecla Enter para salir."))                                              
                                        if definirvariable == "False":     
                                            print("Se estableció " + str(variablepregunta) + " a False.")
                                            print()
                                            variablepregunta = False
                                            exit(input("Presione la tecla Enter para salir."))                                        
                                    else:
                                        cls()
                                        print()
                                        print(" ¡Error!, debe ser: True o False (con mayúsculas)")
                                        print()
                                        exit(input("Presione la tecla Enter para salir."))
                                    
                                else:
                                    print()
                                    print(" Debe introducir un nombre de sólo letras.")
                            if opcionesboolean == 2: 
                                exit()

                        else:              
                            print()
                            print("Ingrese un número entre 1 a 2.")
                            print()
                            time.sleep(3.0)

                    if preguntaboolean == 2:
                        print()
                        print(" ¡No te preocupes!")
                        print()
                        time.sleep(1.0)
                        print(" Yo te lo explico...")
                        print()
                        time.sleep(2.0)
                        print("Boolean es para representar 2 valores.")
                        print()
                        time.sleep(2.0)
                        print(" ¿Cuáles son esos valores?")
                        print()
                        time.sleep(1.0)
                        print(" - True (Verdadero)")
                        time.sleep(1.0)
                        print(" - False (Falso)")
                        print()
                        time.sleep(2.0)
                        print(" ¿Para qué sirven estos valores?")
                        print()
                        time.sleep(2.0)
                        print("Estos valores sirven para expresiones condicionales y los bucles.")
                        print()
                        exit(input("Presione la tecla Enter para salir."))
                else:
                    print()
                    print("Ingrese un número entre 1 a 2.")
                    print()
                    time.sleep(2)

            #                   #
            #       OP 4        #
            #                   #
            if menu == 4:
                cls()
                print()
                print(" ███████╗███████╗███╗   ██╗████████╗███████╗███╗   ██╗ ██████╗██╗ █████╗ ███████╗")
                print(" ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██╔════╝████╗  ██║██╔════╝██║██╔══██╗██╔════╝")
                print(" ███████╗█████╗  ██╔██╗ ██║   ██║   █████╗  ██╔██╗ ██║██║     ██║███████║███████╗")
                print(" ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  ██║╚██╗██║██║     ██║██╔══██║╚════██║")
                print(" ███████║███████╗██║ ╚████║   ██║   ███████╗██║ ╚████║╚██████╗██║██║  ██║███████║")
                print(" ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝")
                print()
                print(" ¿Sabes qué es If, else y while?")
                print()
                print(" 1. Si lo sé.")
                print(" 2. No lo sé.")
                print()
                preguntasentencias = int(input(" Escoje una opción: "))
                print()
                while preguntasentencias == 1 or preguntasentencias == 2:
                    if preguntasentencias == 1:
                        print("¡Excelente¡, ¡el 90% de nuestro programa utiliza estas sentencias y bucles!")
                        print()
                        time.sleep(1.0)
                        print(" Puedes revisar el código y verificarlo :D")
                        print()
                        exit(input("Presione la tecla Enter para salir."))
                    if preguntasentencias == 2: 
                        print(" ¡No te preocupes!, yo te lo explico...")
                        time.sleep(2.0)
                        print()
                        print("Definiciones:")
                        time.sleep(1.0)
                        print()
                        print(" Sentencia If: Permite que un programa ejecute unas instrucciones cuando se cumplan una condición.")
                        time.sleep(5.0)
                        print()
                        print(" Sentencia Else: Permite que un programa ejecute unas instrucciones cuando la condición sea lo contrario.")
                        time.sleep(5.0)
                        print()
                        print(" Bucle While: Permite que se ejecute una sentencia repetitiva cuando se cumpla una condición.")
                        time.sleep(5.0)
                        print()
                        print()
                        print()
                        print("¡El 90% de nuestro programa utiliza estas sentencias y bucles!")
                        time.sleep(1.0)
                        print()
                        print(" Puedes revisar el código y verificarlo :D")
                        print()
                        print()
                        exit(input("Presione la tecla Enter para salir."))
                else:
                    print()
                    print("Introduce un número entre 1 a 2.")
                    print()
                    time.sleep(2)

            #                   #
            #       OP 5        #
            #                   #
            if menu == 5:
                cls()
                print()
                print(" ██████╗ ██╗   ██╗ ██████╗██╗     ███████╗    ███████╗ ██████╗ ██████╗ ")
                print(" ██╔══██╗██║   ██║██╔════╝██║     ██╔════╝    ██╔════╝██╔═══██╗██╔══██╗")
                print(" ██████╔╝██║   ██║██║     ██║     █████╗      █████╗  ██║   ██║██████╔╝")
                print(" ██╔══██╗██║   ██║██║     ██║     ██╔══╝      ██╔══╝  ██║   ██║██╔══██╗")
                print(" ██████╔╝╚██████╔╝╚██████╗███████╗███████╗    ██║     ╚██████╔╝██║  ██║")
                print(" ╚═════╝  ╚═════╝  ╚═════╝╚══════╝╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝")
                print()
                print(" ¿Sabes qué es un Bucle For?")
                print()
                print(" 1. Si lo sé.")
                print(" 2. No lo sé.")
                print()
                preguntabuclefor = int(input(" Escoje una opción: "))
                print()
                while preguntabuclefor == 1 or preguntabuclefor == 2:
                    if preguntabuclefor == 1:
                        cls()
                        print()
                        print(" ██████╗ ██╗   ██╗ ██████╗██╗     ███████╗    ███████╗ ██████╗ ██████╗ ")
                        print(" ██╔══██╗██║   ██║██╔════╝██║     ██╔════╝    ██╔════╝██╔═══██╗██╔══██╗")
                        print(" ██████╔╝██║   ██║██║     ██║     █████╗      █████╗  ██║   ██║██████╔╝")
                        print(" ██╔══██╗██║   ██║██║     ██║     ██╔══╝      ██╔══╝  ██║   ██║██╔══██╗")
                        print(" ██████╔╝╚██████╔╝╚██████╗███████╗███████╗    ██║     ╚██████╔╝██║  ██║")
                        print(" ╚═════╝  ╚═════╝  ╚═════╝╚══════╝╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝")
                        print()                        
                        animated_print("Este texto está basado en bucle for (linea 16)")
                        print()
                        print()
                        time.sleep(1)
                        exit(input("Presione la tecla Enter para salir."))
                    if preguntabuclefor == 2: 
                        cls()
                        print()
                        print(" ██████╗ ██╗   ██╗ ██████╗██╗     ███████╗    ███████╗ ██████╗ ██████╗ ")
                        print(" ██╔══██╗██║   ██║██╔════╝██║     ██╔════╝    ██╔════╝██╔═══██╗██╔══██╗")
                        print(" ██████╔╝██║   ██║██║     ██║     █████╗      █████╗  ██║   ██║██████╔╝")
                        print(" ██╔══██╗██║   ██║██║     ██║     ██╔══╝      ██╔══╝  ██║   ██║██╔══██╗")
                        print(" ██████╔╝╚██████╔╝╚██████╗███████╗███████╗    ██║     ╚██████╔╝██║  ██║")
                        print(" ╚═════╝  ╚═════╝  ╚═════╝╚══════╝╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝")
                        print()                        
                        time.sleep(1)
                        print(" El bucle for nos permitirá iterar sobre una variable compleja, del tipo lista, es decir, mostrar en líneas individuales cada resultado obtenido.")
                        print()
                        time.sleep(8.0)
                        animated_print("Este texto está basado en un bucle for (puedes verlo en la línea 16 del código)")
                        print()
                        print()
                        time.sleep(5)
                        exit(input("Presione la tecla Enter para salir."))                        
                        
                else:
                    print()
                    print("Introduce un número entre 1 a 2.")
                    print()
                    exit(input(" Presione la tecla Enter para salir."))                                                                                           

            #                   #
            #       OP 6        #
            #                   #
            if menu == 6:
                cls()
                print()
                print("  █████╗  ██████╗████████╗██╗██╗   ██╗██╗██████╗  █████╗ ██████╗ ███████╗███████╗")
                print(" ██╔══██╗██╔════╝╚══██╔══╝██║██║   ██║██║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝")
                print(" ███████║██║        ██║   ██║██║   ██║██║██║  ██║███████║██║  ██║█████╗  ███████╗")
                print(" ██╔══██║██║        ██║   ██║╚██╗ ██╔╝██║██║  ██║██╔══██║██║  ██║██╔══╝  ╚════██║")
                print(" ██║  ██║╚██████╗   ██║   ██║ ╚████╔╝ ██║██████╔╝██║  ██║██████╔╝███████╗███████║")
                print(" ╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝  ╚═══╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝")
                print()
                print(" -=- Opciones Disponibles -=-")
                print()
                print(" 1. Votacion y Signo Zodiacal.")
                print(" 2. Operaciones Matemáticas y Calculo promedio. (Ya existe en el menú principal)")
                print()
                print(" Más próximamente...")
                print()
                preguntaactividades = int(input("Escoje una opción: "))
                print()
                while preguntaactividades == 1 or preguntaactividades == 2:
                    if preguntaactividades == 1:
                        cls()
                        Nombre = input("Ingrese su primer nombre: ")
                        Apellido = input("Ingrese su primer apellido: ")

                        #-----------------------------------------------#
                        # VERIFICA QUE NOMBRE Y APELLIDOS SEAN PALABRAS #
                        #-----------------------------------------------#
                        while Nombre.isalpha() and Apellido.isalpha():
                            #-----------------------------------------------#
                            # VERIFICA QUE NOMBRE Y APELLIDOS TENGAN MINIMO #
                            # 3 LETRAS Y MAXIMO 15                          #
                            #-----------------------------------------------#    
                            while len(Nombre) >= 3 and len(Nombre) <= 15 and len(Apellido) >= 3 and len(Apellido) <= 15:
                                cls()
                                print()
                                print(" ██████╗  █████╗ ████████╗ ██████╗ ███████╗")
                                print(" ██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝")
                                print(" ██║  ██║███████║   ██║   ██║   ██║███████╗")
                                print(" ██║  ██║██╔══██║   ██║   ██║   ██║╚════██║")
                                print(" ██████╔╝██║  ██║   ██║   ╚██████╔╝███████║")
                                print(" ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝")                                        
                                print()
                                print("¡Hola, " + Nombre + " " + Apellido + "!")    
                                print()
                                print()        
                                año_nac = int(input("Ingrese su Año de nacimiento: "))
                                mes_nac = int(input("Ingrese su Mes de nacimiento: "))
                                dia_nac = int(input("Ingrese su Dia de nacimiento: "))
                                while año_nac <= anoActual and mes_nac >= 1 and mes_nac <= 12 and dia_nac >= 1 and dia_nac <= 31:
                                    cls()
                                    print()
                                    print("  ██████╗ ██████╗  ██████╗██╗ ██████╗ ███╗   ██╗███████╗███████╗")
                                    print(" ██╔═══██╗██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║██╔════╝██╔════╝")
                                    print(" ██║   ██║██████╔╝██║     ██║██║   ██║██╔██╗ ██║█████╗  ███████╗")
                                    print(" ██║   ██║██╔═══╝ ██║     ██║██║   ██║██║╚██╗██║██╔══╝  ╚════██║")
                                    print(" ╚██████╔╝██║     ╚██████╗██║╚██████╔╝██║ ╚████║███████╗███████║")
                                    print("  ╚═════╝ ╚═╝      ╚═════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝")                                                               
                                    print()
                                    animated_print("La fecha ingresada es " + str(dia_nac) + "/" + str(mes_nac) + "/" + str(año_nac))
                                    print()
                                    print()
                                    print(" -=- Opciones disponibles -=-")
                                    print()
                                    print(" 1. Verificar si puedo votar.")
                                    print(" 2. Verificar mi Signo Zodiacal.")
                                    print()
                                    pregunta = int(input("Escoja una opción: "))
                                    print()
                                    while pregunta == 1 or pregunta == 2:
                                        if pregunta == 1:
                                            calculo1 = anoActual - año_nac
                                            cls()
                                            print()
                                            print(" ██╗   ██╗ ██████╗ ████████╗ █████╗  ██████╗██╗ ██████╗ ███╗   ██╗███████╗███████╗")
                                            print(" ██║   ██║██╔═══██╗╚══██╔══╝██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║██╔════╝██╔════╝")
                                            print(" ██║   ██║██║   ██║   ██║   ███████║██║     ██║██║   ██║██╔██╗ ██║█████╗  ███████╗")
                                            print(" ╚██╗ ██╔╝██║   ██║   ██║   ██╔══██║██║     ██║██║   ██║██║╚██╗██║██╔══╝  ╚════██║")
                                            print("  ╚████╔╝ ╚██████╔╝   ██║   ██║  ██║╚██████╗██║╚██████╔╝██║ ╚████║███████╗███████║")
                                            print("   ╚═══╝   ╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝")                                                                                
                                            print()                
                                            #-------------------------------------#
                                            # VERIFICA LA VARIABLE CALCULADA PARA #
                                            # COMPROBAR SI TIENE MAS DE 18 AÑOS   #
                                            #-------------------------------------#                  
                                            if calculo1 >= 18:
                                                if (mesActual >= mes_nac) and (diaActual >= dia_nac):
                                                    print("Tiene permitido votar, ya que es mayor de edad y tiene " + repr(calculo1) + " años.")
                                                    time.sleep(4)
                                                    print()
                                                    exit(input("Presione la tecla Enter para salir."))
                                                else:
                                                    calculo1 = calculo1 - 1
                                                    print("Tiene permitido votar, ya que es mayor de edad y tiene " + repr(calculo1) + " años.")
                                                    time.sleep(4)
                                                    print()
                                                    exit(input("Presione la tecla Enter para salir."))                            
                                            else:
                                                if (mes_nac <= mesActual) and (dia_nac <= diaActual):
                                                    print("No tiene permitido votar, ya que tiene " + repr(calculo1) + " años, por lo cuál es menor de edad.")
                                                    time.sleep(4)
                                                    print()
                                                    exit(input("Presione la tecla Enter para salir."))  
                                                else:
                                                    calculo1 = calculo1 - 1
                                                    print("No tiene permitido votar, ya que tiene " + repr(calculo1) + " años, por lo cuál es menor de edad.")
                                                    time.sleep(4)
                                                    print()
                                                    exit(input("Presione la tecla Enter para salir."))                             
                                        if pregunta == 2:
                                            cls()
                                            print()
                                            print(" ███████╗██╗ ██████╗ ███╗   ██╗ ██████╗ ")
                                            print(" ██╔════╝██║██╔════╝ ████╗  ██║██╔═══██╗")
                                            print(" ███████╗██║██║  ███╗██╔██╗ ██║██║   ██║")
                                            print(" ╚════██║██║██║   ██║██║╚██╗██║██║   ██║")
                                            print(" ███████║██║╚██████╔╝██║ ╚████║╚██████╔╝")
                                            print(" ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ")
                                            print()                          
                                            #------------------------------------------#
                                            # SEGUN MES Y DIA ESTABLECE LA VARIABLE AL #
                                            # SIGNO ZODIACAL QUE CORRESPONDA           #
                                            #------------------------------------------#
                                            if (dia_nac >= 21 and mes_nac == 3) or (dia_nac <= 20 and mes_nac == 4):
                                                signo = "Aries"
                                            if (dia_nac >= 24 and mesActual == 9) or (dia_nac <= 23 and mes_nac == 10):
                                                signo = "Libra"
                                            if (dia_nac >= 21 and mes_nac == 4) or (dia_nac <= 21 and mes_nac == 5):
                                                signo = "Tauro"
                                            if (dia_nac >= 24 and mes_nac == 10) or (dia_nac <= 22 and mes_nac == 11):
                                                signo = "Escorpio"
                                            if (dia_nac >= 22 and mes_nac == 5) or (dia_nac <= 21 and mes_nac == 6):
                                                signo = "Géminis"
                                            if (dia_nac >= 23 and mes_nac == 11) or (dia_nac <= 21 and mes_nac == 12):
                                                signo = "Sagitario"
                                            if (dia_nac >= 21 and mes_nac == 6) or (dia_nac <= 23 and mes_nac == 7):
                                                signo = "Cáncer"
                                            if (dia_nac >= 22 and mes_nac == 12) or (dia_nac <= 20 and mes_nac == 1):
                                                signo = "Capricornio"
                                            if (dia_nac >= 24 and mes_nac == 7) or (dia_nac <= 23 and mes_nac == 8):
                                                signo = "Leo"
                                            if (dia_nac >= 21 and mesActual == 1) or (dia_nac <= 19 and mes_nac == 2):
                                                signo = "Acuario"
                                            if (dia_nac >= 24 and mes_nac == 8) or (dia_nac <= 23 and mes_nac == 9):
                                                signo = "Virgo"
                                            if (dia_nac >= 20 and mes_nac == 2) or (dia_nac <= 20 and mes_nac == 3):
                                                signo = "Piscis"                           
                                            print("Según los datos proporcionados, su signo zodiacal es " + str(signo) + ".")
                                            time.sleep(4)
                                            print()
                                            exit(input("Presione la tecla Enter para salir."))                
                                    else:
                                        print()
                                        print("Por favor, introduce un número entre 1 y 2.")
                                        print()
                                        time.sleep(4)

                                #--------------------------------------------#
                                # COMPRUEBA QUE NO HAYA UN PAYASO INSERTANDO #
                                # VALORES ERRONEOS A PROPOSITO               #
                                #--------------------------------------------#
                                else:
                                    if mes_nac < 0 or mes_nac > 12:
                                        print()
                                        print("Sólo debes ingresar números entre 1 a 12.")
                                        print()
                                        time.sleep(4)
                                    if dia_nac < 0 or dia_nac > 31:
                                        print()
                                        print("Sólo debes ingresar números entre 1 a 31.")
                                        print()
                                        time.sleep(4)
                                    if año_nac > anoActual:
                                        print()
                                        print("Me parece bien que te guste el futuro, pero acá necesitamos seriedad.")
                                        print("Introduce un año igual o menor a " + str(anoActual) + " por favor.")
                                        print()
                                        time.sleep(4)
                                    if año_nac < 0:
                                        print()
                                        print("¿Qué intentas hacer?")
                                        print("Introduce un año válido.")
                                        print()
                                        time.sleep(4)
                            else:
                                if (len(Nombre) < 3 or len(Nombre) > 15) or (len(Apellido) < 3 or len(Apellido) > 15):
                                    print()
                                    print("El nombre o apellido no puede tener menos de 3 letras ni más de 15.")
                                    print()
                                    time.sleep(4)
                                    exit(input("Presione la tecla Enter para salir."))
                        else:
                            print()
                            print("Nombre o apellido inválido, sólo debe ingresar letras.")
                            time.sleep(4)
                    if preguntaactividades == 2:
                        print("¡Ya existe esto en el menú principal!")
                        time.sleep(4) 
                        print()  
                        exit(input("Presione la tecla Enter para salir."))
                else:
                    print()
                    print("Por favor, introduce un número entre 1 y 2.")
                    print()
                    time.sleep(4)

            #                   #
            #       OP 7        #
            #                   #
            if menu == 7:
                cls()
                print()
                print(" ██╗███╗   ██╗███████╗ ██████╗ ")
                print(" ██║████╗  ██║██╔════╝██╔═══██╗")
                print(" ██║██╔██╗ ██║█████╗  ██║   ██║")
                print(" ██║██║╚██╗██║██╔══╝  ██║   ██║")
                print(" ██║██║ ╚████║██║     ╚██████╔╝")
                print(" ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ ")
                print()
                print()
                print("     ¡Hola amig@ curios@!")
                print()
                time.sleep(2.0)
                print(" ¡Me alegra que quieras saber más sobre mi programa! :D")
                time.sleep(2.0)
                print()
                print(" Las cosas que puedes hacer con éste programa son:")
                time.sleep(1.0)
                print()
                print("   - Hacer cálculos matemáticos, tales como; Sumar, restar, multiplicar, dividir y calcular promedios.")
                time.sleep(1.0)
                print("   - Funciones de lista, tales como; Ver lista, agregar cosas a lista, eliminar cosas de lista.")
                time.sleep(1.0)
                print("   - Funciones de Boolean.")
                time.sleep(1.0)
                print("   - Sentencias If y Else.")
                time.sleep(1.0)
                print("   - Bucles While y For.")
                time.sleep(2.0)
                print()
                print(" De momento son pocas funciones que ofrece este programa, a medida que vaya aprendiendo, se agregarán más :)")
                print()
                time.sleep(4.0)
                print(" Ante cualquier duda, o problemática que tenga, no dude en contactarme")
                print()
                time.sleep(1.0)
                print(" Discord: " + Discord)
                time.sleep(1.0)
                print(" Telegram: " + Telegram)
                time.sleep(1.0)
                print(" Email: " + Email)
                time.sleep(3.0)
                print()
                exit(input("¡Para salir presione la tecla Enter!"))                  

            #                   #
            #       OP 8        #
            #                   #
            if menu == 8:
                cls()
                print()
                print(" ████████╗███████╗███████╗████████╗███████╗██████╗ ")
                print(" ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗")
                print("    ██║   █████╗  ███████╗   ██║   █████╗  ██████╔╝")
                print("    ██║   ██╔══╝  ╚════██║   ██║   ██╔══╝  ██╔══██╗")
                print("    ██║   ███████╗███████║   ██║   ███████╗██║  ██║")
                print("    ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝")
                print()
                time.sleep(5.0)
                print(" ¡Hola!")
                print()
                time.sleep(1.0)
                print(" ¡Agradezco querer colaborar en este programa!")
                print()
                time.sleep(3.0)
                print(" Para formar parte del programa de Beta Tester, envíame")
                print(" un mensaje por WhatsApp al +56 9 8206 6886 para inscribirte!")
                print()
                time.sleep(2.0)
                print(" ¡Muchas gracias por tu colaboración y uso del programa! :D")
                time.sleep(5.0)
                print()
                exit(input("Presione la tecla Enter para salir."))

            #                   #
            #       OP 9        #
            #                   #
            if menu == 9:
                exit()
        else:
            print()
            print("Escoja un número entre 1 y 9.")
            print()
            menu = int(input("Escoja una opción: "))
        #                       #
        #           END         #
        #                       #          
    else:
        print()
        print(" ███████╗██████╗ ██████╗  ██████╗ ██████╗ ")
        print(" ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗")
        print(" █████╗  ██████╔╝██████╔╝██║   ██║██████╔╝")
        print(" ██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗")
        print(" ███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║")
        print(" ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝")
        print()
        print("¡No modifiques mis créditos ni redes sociales!")
        time.sleep(5.0)
        exit()
else:
    print("Este programa sólo puede ser ejecutado en un equipo Windows.")

#                           #
#       FIN CHECK SO        #
#                           #    

#-----------------------#
#                       #
#           END         #
#                       #
#-----------------------#   