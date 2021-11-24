#                   #
#       IMPORTS     #
#                   #
import time
import os
import sys
def cls():
    os.system("cls")
def animated_print(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.09)

#                   #
#       START       #
#                   #
print()
print("  ██████╗ ██╗   ██╗██╗ █████╗      ██╗")
print(" ██╔════╝ ██║   ██║██║██╔══██╗    ███║")
print(" ██║  ███╗██║   ██║██║███████║    ╚██║")
print(" ██║   ██║██║   ██║██║██╔══██║     ██║")
print(" ╚██████╔╝╚██████╔╝██║██║  ██║     ██║")
print("  ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═╝     ╚═╝")
print()       
print()                              
animated_print("     -=- Opciones Disponibles -=-")
print()
print()
time.sleep(0.3)
print(" 1. Ejercicio N1 (Número positivo, negativo y neutro).")
time.sleep(0.3)
print(" 2. Ejercicio N2 (Suma, resta, producto y división).")
time.sleep(0.3)
print(" 3. Ejercicio N3 (Raíz cuadrada).")
time.sleep(0.3)
print(" 4. Ejercicio N4 (Promedio 3 notas).")
time.sleep(0.3)
print(" 5. Ejercicio N5 (Promedio notas a elección).")
time.sleep(0.3)
print(" 6. Ejercicio N6 (Seg a cant min, hora, min y seg).")
time.sleep(0.3)
print(" 7. Ejercicio N7 (Calcular sueldo según horas).")
time.sleep(0.3)
print(" 8. Ejercicio N8 (Calcular sueldo con incremento).")
time.sleep(0.3)
print(" 9. Ejercicio N9 (No supe hacerlo).")
time.sleep(0.3)
print(" 10. Ejercicio N10 (Convertir entre °C y °F).")
time.sleep(0.3)
print()
pregunta1 = int(input("Escoja una opción: "))
print()
time.sleep(0.3)
while pregunta1 >= 1 and pregunta1 <= 10:
    #                 #
    #   EJERCICIO 1   #
    #                 #    
    if pregunta1 == 1:
        cls()
        print()
        print(" ███████╗     ██╗     ██╗")
        print(" ██╔════╝     ██║    ███║")
        print(" █████╗       ██║    ╚██║")
        print(" ██╔══╝  ██   ██║     ██║")
        print(" ███████╗╚█████╔╝     ██║")
        print(" ╚══════╝ ╚════╝      ╚═╝")
        print()
        print("  Número positivo, negativo y neutro.")
        print()
        ej1n1 = int(input(" Ingrese un número: "))
        print()
        if ej1n1 < 0:
            print("El número ingresado fue " + str(ej1n1) + " y es un número negativo.")
            time.sleep(2)
            print()
            exit(input("Presione la tecla Enter para salir."))
        else:
            if ej1n1 == 0:
                print("El número ingresado fue " + str(ej1n1) + " y es un número neutro.")
                time.sleep(2)
                print()
                exit(input("Presione la tecla Enter para salir."))                

            if ej1n1 > 0:
                print("El número ingresado fue " + str(ej1n1) + " y es un número positivo.")
                time.sleep(2)
                print()
                exit(input("Presione la tecla Enter para salir."))

    #                 #
    #   EJERCICIO 2   #
    #                 #
    if pregunta1 == 2:
        cls()
        print()
        print(" ███████╗     ██╗    ██████╗ ")
        print(" ██╔════╝     ██║    ╚════██╗")
        print(" █████╗       ██║     █████╔╝")
        print(" ██╔══╝  ██   ██║    ██╔═══╝ ")
        print(" ███████╗╚█████╔╝    ███████╗")
        print(" ╚══════╝ ╚════╝     ╚══════╝")
        print()
        print("  Suma, resta, producto y división")
        print()
        ej2n1 = int(input("Introduzca el priner núnero: "))
        ej2n2 = int(input("Introdzuca el segundo número: "))
        print()
        ej2calc1 = ej2n1 + ej2n2
        print("La suma de ambos números es " + str(ej2calc1))
        print()
        ej2calc2 = ej2n1 - ej2n2
        print("La resta de ambos números es " + str(ej2calc2))
        print()
        ej2calc3 = ej2n1 * ej2n2
        print("El producto de ambos números es " + str(ej2calc3))
        print()
        ej2calc4 = ej2n1 / ej2n2
        print("La división de ambos números es " + str(ej2calc4))
        print()
        exit(input("Presione la tecla Enter para salir."))
    
    #                 #
    #   EJERCICIO 3   #
    #                 #
    if pregunta1 == 3:
        cls()
        print()
        print(" ███████╗     ██╗    ██████╗ ")
        print(" ██╔════╝     ██║    ╚════██╗")
        print(" █████╗       ██║     █████╔╝")
        print(" ██╔══╝  ██   ██║     ╚═══██╗")
        print(" ███████╗╚█████╔╝    ██████╔╝")
        print(" ╚══════╝ ╚════╝     ╚═════╝ ")
        print()
        print("     Raíz cuadrada")
        print()
        ej3n1 = int(input("Introduzca un número: "))
        while ej1n1 >= 1:
            print()
            print("La raíz cuadrada de " + str(ej3n1) + " es " + str(pow(ej3n1,0.3)))
            print()
            exit(input("Presione la tecla Enter para salir."))
        else:
            print()
            print("Intrduce un número positivo.")
            print()
            time.sleep(2)
            ej3n1 = int(input("Introduzca un número: "))

    #                 #
    #   EJERCICIO 4   #
    #                 #
    if pregunta1 == 4:
        listnotas = []
        sumanotas = 0
        cls()
        print()
        print(" ███████╗     ██╗    ██╗  ██╗")
        print(" ██╔════╝     ██║    ██║  ██║")
        print(" █████╗       ██║    ███████║")
        print(" ██╔══╝  ██   ██║    ╚════██║")
        print(" ███████╗╚█████╔╝         ██║")
        print(" ╚══════╝ ╚════╝          ╚═╝")
        print()                            
        print("       Promedio 3 notas en")
        print(" Introducción a la programación")
        print()
        for tresnotas in range(3):
            if tresnotas == 0:
                nota = float(input("Ingrese la primera nota: "))
                while nota >=1.0 and nota <= 7.0:
                    listnotas.append(nota)
                    tresnotas + 1
                    break
                else:
                    if tresnotas < 1:
                        print()
                        print("No puede haber ningúna nota negativa.")
                        time.sleep(2)
                        print()
                        exit(input("Presione la tecla Enter para salir."))
                    if tresnotas > 7:
                        print()
                        print("No puede ingresar una nota mayor a 7.")    
                        time.sleep(2) 
                        print()
                        exit(input("Presione la tecla Enter para salir."))                
            if tresnotas == 1:
                print()
                nota = float(input("Ingrese la segunda nota: "))
                while nota >=1.0 and nota <= 7.0:
                    listnotas.append(nota)
                    tresnotas + 1
                    break
                else:
                    if tresnotas < 1:
                        print()
                        print("No puede haber ningúna nota negativa.")
                        time.sleep(2)
                        print()
                        exit(input("Presione la tecla Enter para salir."))
                    if tresnotas > 7:
                        print()
                        print("No puede ingresar una nota mayor a 7.") 
                        time.sleep(2)     
                        print()
                        exit(input("Presione la tecla Enter para salir."))       
            if tresnotas == 2:
                print()
                nota = float(input("Ingrese la tercera nota: "))
                while nota >=1.0 and nota <= 7.0:
                    listnotas.append(nota)
                    break
                else:
                    if tresnotas < 1:
                        print()
                        print("No puede haber ningúna nota negativa.")
                        time.sleep(2)
                        print()
                        exit(input("Presione la tecla Enter para salir."))
                    if tresnotas > 7:
                        print()
                        print("No puede ingresar una nota mayor a 7.")
                        time.sleep(2)
                        print()
                        exit(input("Presione la tecla Enter para salir."))
            sumanotas += listnotas[tresnotas]
        if len(listnotas) == 3:
            print()
            print("El promedio final es: " + str(sumanotas / 3))
            time.sleep(2)
            print()
            exit(input("Presione la tecla enter para salir."))                                      
        else:
            print()
            print("Error: No se han encontrado 3 notas.")

    #                 #
    #   EJERCICIO 5   #
    #                 #
    if pregunta1 == 5:
        listnotas2 = []
        sumanotas2 = 0
        cls()
        print()
        print(" ███████╗     ██╗    ███████╗")
        print(" ██╔════╝     ██║    ██╔════╝")
        print(" █████╗       ██║    ███████╗")
        print(" ██╔══╝  ██   ██║    ╚════██║")
        print(" ███████╗╚█████╔╝    ███████║")
        print(" ╚══════╝ ╚════╝     ╚══════╝")
        print()                    
        print("       Promedio de Notas")
        print()
        c1p5 = int(input("Introduzca la cantidad de notas que desea calcular: "))
        print()
        while c1p5 >=2:
            for pnotas in range(c1p5):
                notaej5 = float(input("Ingrese la nota número " + str(pnotas + 1) + ": "))
                while notaej5 >= 1.0 and notaej5 <= 7.0:
                    listnotas2.append(notaej5)
                    break
                else:
                    if pnotas < 1:
                        print()
                        print("No puede haber ningúna nota negativa.")
                        time.sleep(2)
                        print()
                        exit(input("Presione la tecla Enter para salir."))
                    if pnotas > 7:
                        print()
                        print("No puede ingresar una nota mayor a 7.")
                        time.sleep(2)
                        print()
                        exit(input("Presione la tecla Enter para salir.")) 
                sumanotas2 += listnotas2[pnotas] 
            if len(listnotas2) == c1p5:
                print()
                print("El promedio final es: " + str(sumanotas2 / c1p5))
                time.sleep(2)
                print()
                exit(input("Presione la tecla enter para salir."))                  
            else:
                print()
                print("Error: No se han encontrado " + str(c1p5) + " notas.")                   
        else:
            if c1p5 == 1:
                print()
                print("No podré calcular el promedio si sólo ingresas una nota.")
                time.sleep(2)
            if c1p5 == 0:
                print()
                print("Error: El número ingresado es neutro, por favor, ingrese un número positivo.")
                time.sleep(2)            
            if c1p5 < 1:
                print()
                print("Error: El número ingresado es negativo, por favor, ingrese un número positivo.")
                time.sleep(2)

    #                 #
    #   EJERCICIO 6   #
    #                 #    
    if pregunta1 == 6:
        cls()
        print()
        print(" ███████╗     ██╗     ██████╗ ")
        print(" ██╔════╝     ██║    ██╔════╝ ")
        print(" █████╗       ██║    ███████╗ ")
        print(" ██╔══╝  ██   ██║    ██╔═══██╗")
        print(" ███████╗╚█████╔╝    ╚██████╔╝")
        print(" ╚══════╝ ╚════╝      ╚═════╝ ")
        print()                             
        print("  Segundos a cantidad de minutos,")
        print("   horas y segundos")
        print()
        segundos= int(input("Escriba la cantidad de segundos: "))
        while segundos >= 1:
            print()
            if segundos <= 59:
                print("La cantidad de segundos ingresados se define en, 0 dias, 0 horas, 0 minutos y " + str(segundos) + " segundos")
                time.sleep(2)
                print()
                exit(input("Presione la tecla Enter para salir."))
            else:
                if segundos == 60:
                    print("La cantidad de segundos ingresados se define en, 0 dias, 0 horas, 1 minuto y 0 segundos")
                    time.sleep(2) 
                    print()
                    exit(input("Presione la tecla Enter para salir."))
                if segundos > 60:
                    Dias = segundos // (24 * 60 * 60)
                    segundos = segundos % (24 * 60 *60)
                    Horas = segundos // (60 * 60)
                    segundos = segundos % (60 * 60)
                    minutos = segundos // 60
                    segundos = segundos // 60                    
                    print("La cantidad de segundos ingresados se define en, {} dias, {} horas, {} minutos y {} segundos".format(Dias, Horas, minutos, segundos)) 
                    time.sleep(2) 
                    print()
                    exit(input("Presione la tecla Enter para salir."))                    
        else:
            time.sleep(2)
            print()                  
            print(" Debe introducir un número mayor a 1.")
            print()
            segundos= int(input("Escriba la cantidad de segundos: "))
    
    #                 #
    #   EJERCICIO 7   #
    #                 #  
    if pregunta1 == 7:
        cls()
        print()
        print(" ███████╗     ██╗    ███████╗")
        print(" ██╔════╝     ██║    ╚════██║")
        print(" █████╗       ██║        ██╔╝")
        print(" ██╔══╝  ██   ██║       ██╔╝ ")
        print(" ███████╗╚█████╔╝       ██║  ")
        print(" ╚══════╝ ╚════╝        ╚═╝  ")
        print()                            
        sueldo = float(input("Ingrese el sueldo por hora que se le asigno: "))
        horas = int(input("Ingrese la cantidad de horas que trabaja: "))
        sueldototal = horas * sueldo
        while sueldo >= 1 and horas >= 1:
            print()
            print("Se le debe pagar ", sueldototal, " por la cantidad de horas trabajadas." )
            time.sleep(2)
            print()
            exit(input("Presione la tecla Enter para salir."))
        else:
            if sueldo < 1:
                time.sleep(2)
                print()                  
                print(" Debe introducir un sueldo mayor a $1.")
                print()           
                sueldo = float(input("Ingrese el sueldo por hora que se le asigno: "))
            if horas < 1:
                print()                  
                print(" Debe introducir una cantidad de horas mayor a 1.")
                print()   
                horas = int(input("Ingrese la cantidad de horas que trabaja: "))                

    #                 #
    #   EJERCICIO 8   #
    #                 # 
    if pregunta1 == 8:
        tarifa = 1500
        cls()
        print()
        print(" ███████╗     ██╗     █████╗ ")
        print(" ██╔════╝     ██║    ██╔══██╗")
        print(" █████╗       ██║    ╚█████╔╝")
        print(" ██╔══╝  ██   ██║    ██╔══██╗")
        print(" ███████╗╚█████╔╝    ╚█████╔╝")
        print(" ╚══════╝ ╚════╝      ╚════╝")                            
        print()
        p8n1 = int(input("Ingrese la cantidad de horas trabajadas: "))
        print()
        while p8n1 >=1:
            if p8n1 > 45:
                pago = p8n1 * tarifa
                incremento = (50 / 100) * pago
                pago += incremento
                print("Según las horas trabajadas y la tarifa, su sueldo es " + str(pago))
                time.sleep(2)
                print()
                exit(input("Presione la tecla Enter para salir."))                
            else:
                pagototal = p8n1 * tarifa
                print("Según las horas trabajadas y la tarifa, su sueldo es " + str(pagototal))
                time.sleep(2)
                print()
                exit(input("Presione la tecla Enter para salir."))
        else:
            time.sleep(2)
            print()
            print(" Debe introducir un número mayor a 1.")
            print()   
            p8n1 = int(input("Ingrese la cantidad de horas trabajadas: ")) 
    
    #                 #
    #   EJERCICIO 9   #
    #                 #     
    if pregunta1 == 9:
        cls()
        print()
        print(" ███████╗██████╗ ██████╗  ██████╗ ██████╗ ")
        print(" ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗")
        print(" █████╗  ██████╔╝██████╔╝██║   ██║██████╔╝")
        print(" ██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗")
        print(" ███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║")
        print(" ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝")
        print()
        animated_print("Como le dije...") 
        print()
        print()
        animated_print("No supe hacerlo :(")
        time.sleep(2)
        print()
        print()
        exit(input("Presione la tecla Enter para salir."))

    #                  #
    #   EJERCICIO 10   #
    #                  # 
    if pregunta1 == 10:
        cls()
        print()
        print("  ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ███████╗ ██████╗ ██████╗ ")
        print(" ██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗██╔════╝██╔═══██╗██╔══██╗")
        print(" ██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝███████╗██║   ██║██████╔╝")
        print(" ██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██║   ██║██╔══██╗")
        print(" ╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║███████║╚██████╔╝██║  ██║")
        print("  ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝")
        print()                                                                             
        animated_print("     -=- Opciones Disponibles -=-")
        print()
        print()
        time.sleep(0.3)
        print(" 1. Convertir °C a °F.")
        time.sleep(0.3)
        print(" 2. Convertir °F a °C.")
        print()
        p10n1 = int(input("Escoja una opción: "))
        print()
        while p10n1 == 1 or p10n1 == 2:
            if p10n1 == 1:
                p10v1 = int(input("Ingrese la cantidad de grados Celcius para convertir: "))
                ctof = (p10v1 * 9/5) + 32
                print()
                print(str(p10v1) + " grados Celcios es igual a " + str(ctof) + " grados Fahrenheit.")
                time.sleep(2)
                print()
                exit(input("Presione la tecla Enter para salir."))
            if p10n1 == 2:
                p10v1 = int(input("Ingrese la cantidad de grados Fahrenheit para convertir: "))
                ftoc = (p10v1 - 32) * 5/9
                print()
                print(str(p10v1) + " grados Fahrenheit es igual a " + str(ftoc) + " grados Celcius.")
                time.sleep(2)
                print()
                exit(input("Presione la tecla Enter para salir."))
        else:
            time.sleep(2)
            print()
            print(" Debe introducir un número entre 1 a 11.")
            print()  
            p10n1 = int(input("Escoja una opción: "))          
else:
    time.sleep(2)
    print()
    print(" Debe introducir un número entre 1 a 10.")
    print()
    pregunta1 = int(input(" Escoja una opción: "))
