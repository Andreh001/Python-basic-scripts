#                           #
#       IMPORTS & DEF       #
#                           #
import os
def cls():
    os.system("cls")
cmd = "color 0A"
os.system(cmd)
import time
import sys
def animated_print(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.002)
from datetime import date
dateSystem = date.today()
dia = dateSystem.day
mes = dateSystem.month
año = dateSystem.year

#                   #
#       START       #
#                   #
print()
animated_print(" ███╗   ███╗███████╗███╗   ██╗██╗   ██╗")
print()
animated_print(" ████╗ ████║██╔════╝████╗  ██║██║   ██║")
print()
animated_print(" ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║")
print()
animated_print(" ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║")
print()
animated_print(" ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝")
print()
animated_print(" ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ")
print() 
print()                                                      
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
        animated_print(" ██████╗  █████╗ ████████╗ ██████╗ ███████╗")
        print()
        animated_print(" ██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝")
        print()
        animated_print(" ██║  ██║███████║   ██║   ██║   ██║███████╗")
        print()
        animated_print(" ██║  ██║██╔══██║   ██║   ██║   ██║╚════██║")
        print()
        animated_print(" ██████╔╝██║  ██║   ██║   ╚██████╔╝███████║")
        print()
        animated_print(" ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝")
        print()                                          
        print()
        print("¡Hola, " + Nombre + " " + Apellido + "!")    
        print()
        print()        
        año_nac = int(input("Ingrese su Año de nacimiento: "))
        mes_nac = int(input("Ingrese su Mes de nacimiento: "))
        dia_nac = int(input("Ingrese su Dia de nacimiento: "))
        while año_nac <= año and mes_nac >= 1 and mes_nac <= 12 and dia_nac >= 1 and dia_nac <= 31:
            cls()
            print()
            animated_print("  ██████╗ ██████╗  ██████╗██╗ ██████╗ ███╗   ██╗███████╗███████╗")
            print()
            animated_print(" ██╔═══██╗██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║██╔════╝██╔════╝")
            print()
            animated_print(" ██║   ██║██████╔╝██║     ██║██║   ██║██╔██╗ ██║█████╗  ███████╗")
            print()
            animated_print(" ██║   ██║██╔═══╝ ██║     ██║██║   ██║██║╚██╗██║██╔══╝  ╚════██║")
            print()
            animated_print(" ╚██████╔╝██║     ╚██████╗██║╚██████╔╝██║ ╚████║███████╗███████║")
            print()
            animated_print(" ╚═════╝ ╚═╝      ╚═════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝")                                                               
            print()
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
                    calculo1 = año - año_nac
                    cls()
                    print()
                    animated_print(" ██╗   ██╗ ██████╗ ████████╗ █████╗  ██████╗██╗ ██████╗ ███╗   ██╗███████╗███████╗")
                    print()
                    animated_print(" ██║   ██║██╔═══██╗╚══██╔══╝██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║██╔════╝██╔════╝")
                    print()
                    animated_print(" ██║   ██║██║   ██║   ██║   ███████║██║     ██║██║   ██║██╔██╗ ██║█████╗  ███████╗")
                    print()
                    animated_print(" ╚██╗ ██╔╝██║   ██║   ██║   ██╔══██║██║     ██║██║   ██║██║╚██╗██║██╔══╝  ╚════██║")
                    print()
                    animated_print("  ╚████╔╝ ╚██████╔╝   ██║   ██║  ██║╚██████╗██║╚██████╔╝██║ ╚████║███████╗███████║")
                    print()
                    print("   ╚═══╝   ╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝")                                                                                
                    print()                
                    #-------------------------------------#
                    # VERIFICA LA VARIABLE CALCULADA PARA #
                    # COMPROBAR SI TIENE MAS DE 18 AÑOS   #
                    #-------------------------------------#                  
                    if calculo1 >= 18:
                        if (mes >= mes_nac) and (dia >= dia_nac):
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
                        if (mes_nac <= mes) and (dia_nac <= dia):
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
                    animated_print(" ███████╗██╗ ██████╗ ███╗   ██╗ ██████╗ ")
                    print()
                    animated_print(" ██╔════╝██║██╔════╝ ████╗  ██║██╔═══██╗")
                    print()
                    animated_print(" ███████╗██║██║  ███╗██╔██╗ ██║██║   ██║")
                    print()
                    animated_print(" ╚════██║██║██║   ██║██║╚██╗██║██║   ██║")
                    print()
                    animated_print(" ███████║██║╚██████╔╝██║ ╚████║╚██████╔╝")
                    print()
                    animated_print(" ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ")
                    print()  
                    print()                          
                    #------------------------------------------#
                    # SEGUN MES Y DIA ESTABLECE LA VARIABLE AL #
                    # SIGNO ZODIACAL QUE CORRESPONDA           #
                    #------------------------------------------#
                    if (dia_nac >= 21 and mes_nac == 3) or (dia_nac <= 20 and mes_nac == 4):
                        signo = "Aries"
                    if (dia_nac >= 24 and mes == 9) or (dia_nac <= 23 and mes_nac == 10):
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
                    if (dia_nac >= 21 and mes == 1) or (dia_nac <= 19 and mes_nac == 2):
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
            if año_nac > año:
                print()
                print("Me parece bien que te guste el futuro, pero acá necesitamos seriedad.")
                print("Introduce un año igual o menor a " + str(año) + " por favor.")
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
#               #
#       END     #
#               #