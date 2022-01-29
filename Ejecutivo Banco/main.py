from datetime import datetime
import time

from Clases.Movimiento import Movimiento
from Clases.Cliente import Cliente
from Clases.Cuenta import Cuenta
from Clases.Titles import AddClient
from Clases.Titles import AddAccount
from Clases.Titles import Saldo
from Clases.Titles import Deposito
from Clases.Titles import Girar
from Clases.Titles import Transferencia
import os
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
def clear():
    os.system("cls")

cuenta_1 = Cuenta('20876732', 'Cuenta Corriente', 15000)
cuenta_2 = Cuenta('20246772', 'Cuenta Vista', 1000)

listaClientes = []
listaCuentas = []
def Menu():
    clear()
    global cuentaactual, cuentaDestino, cuentaOrigen, movimiento
    cuentaactual = None
    print('''
    
    ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
    ████╗ ████║██╔════╝████╗  ██║██║   ██║
    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                                          
            ¡Bienvenido/a, ejecutivo!
     Por favor, seleccione una opción
    
     1. Agregar Cliente.
     2. Crear cuenta.
     3. Depositar.
     4. Girar.
     5. Transferir.
     6. Consultar saldo.
     7. Ver movimientos.
     8. Salir.
    
    ''')
    option = int(input("N: "))
    while option < 1 or option > 8:
        print("Error: Su opción es inválida.")
        option = int(input("Ingrese opción nuevamente: "))
    else:
        # ----------------#
        # AGREGAR CLIENTE #
        # ----------------#
        if option == 1:
            clear()
            AddClient()
            name = input("Ingrese el nombre del cliente: ")
            rut = input("Ingrese el RUT del cliente: ")
            edad = int(input("Ingrese la edad del cliente: "))
            print('''

             ¿Estás seguro que los datos son correctos?

            ''')
            addclient_confirmation = input("Ingrese S para confirmar o N para cancelar: ")
            if addclient_confirmation == 'S' or addclient_confirmation == 's':
                try:
                    cliente = Cliente({rut},{name},{edad})
                    listaClientes.append(cliente)
                    print("Se ha agregado el cliente.")
                    input("Presione Enter para volver al menú principal.")
                    return Menu()
                except:
                    print("Ha ocurrido un error.")
            elif addclient_confirmation == 'N' or addclient_confirmation == 'n':
                print("Operación cancelada.")
                time.sleep(2)
                print("Volviendo al menú principal...")
                time.sleep(1)
                return Menu()


        # ----------------#
        #  CREAR CUENTA   #
        # ----------------#
        elif option == 2:
            clear()
            AddAccount()
            account_number = int(input("Ingrese un número para la cuenta: "))
            account_type = input("Ingrese el tipo de cuenta: ")
            account_available = int(input("Ingrese el saldo a asignar en la cuenta: "))
            print('''

             ¿Estás seguro que los datos son correctos?

            ''')
            addaccount_confirmation = input("Ingrese S para confirmar y N para cancelar: ")
            if addaccount_confirmation == 'S' or addaccount_confirmation == 's':
                cuenta = Cuenta(account_number,account_type,account_available)
                listaCuentas.append(cuenta)
                print("Se ha agregado una nueva cuenta.")
                input("Presione Enter para volver al menú principal.")
                return Menu()
            elif addaccount_confirmation == 'N' or addaccount_confirmation == 'n':
                print("Operación cancelada.")
                time.sleep(2)
                print("Volviendo al menú principal...")
                time.sleep(1)
                return Menu()

        # ---------------#
        #   DEPOSITAR    #
        # ---------------#
        elif option == 3:
            clear()
            Deposito()
            if listaCuentas == []:
                print("No hay ninguna cuenta en nuestro sistema.")
                time.sleep(2)
                print("Volviendo al menú principal...")
                time.sleep(2)
                return Menu()
            else:
                account_number = int(input("Ingrese el número de cuenta: "))
                for cuenta in listaCuentas:
                    if cuenta.numero_cuenta == account_number:
                        amount = int(input("Por favor, ingrese la cantidad a depositar: "))
                        while amount < 500:
                            print("No puede depositar menos de $500 pesos")
                            amount = int(input("Por favor, ingrese la cantidad a depositar: "))
                        else:
                            cuenta.depositar(amount)
                            movimiento = Movimiento(account_number,dt_string,amount,"Depósito")
                            time.sleep(2)
                            print("Volviendo al menú principal...")
                            time.sleep(2)
                            return Menu()
                    else:
                        print("No se ha encontrado ninguna cuenta con ese número.\nVolviendo al menú principal...")
                        time.sleep(2)
                        return Menu()


        # ---------------#
        #     GIRAR      #
        # ---------------#
        elif option == 4:
            clear()
            Girar()
            if listaCuentas == []:
                print("No hay ninguna cuenta en nuestro sistema.")
                time.sleep(2)
                print("Volviendo al menú principal...")
                time.sleep(2)
                return Menu()
            else:
                account_number = int(input("Ingrese el número de cuenta: "))
                for cuenta in listaCuentas:
                    if cuenta.numero_cuenta == account_number:
                        amount = int(input("Por favor, ingrese la cantidad a girar: "))
                        while amount < 1000:
                            print("No puede girar menos de $1.000 pesos")
                            amount = int(input("Por favor, ingrese la cantidad a girar: "))
                        else:
                            cuenta.girar(amount)
                            time.sleep(2)
                            print("Volviendo al menú principal...")
                            time.sleep(2)
                            return Menu()
                    else:
                        print("No se ha encontrado ninguna cuenta con ese número.\nVolviendo al menú principal...")
                        time.sleep(2)
                        return Menu()

        #---------------#
        # TRANSFERENCIA #
        #---------------#
        elif option == 5:
            clear()
            Transferencia()
            print(f'''
            1. Cuenta Nro 20876732
            2. Cuenta Nro 20246772  
''')
            origen = int(input("Seleccione una cuenta de origen: "))
            destino = int(input("Seleccione la cuenta de destino: "))
            while (origen < 1 or origen > 2) or (destino < 1 or destino > 2):
                print("Error: Opción inválida.")
                origen = int(input("Seleccione una cuenta de origen: "))
                destino = int(input("Seleccione la cuenta de destino: "))
            else:
                while origen == destino or destino == origen:
                    print("¡No puedes transferir a la misma cuenta!")
                    origen = int(input("Seleccione una cuenta de origen: "))
                    destino = int(input("Seleccione la cuenta de destino: "))
                else:
                    montoTransferencia = int(input("Ingrese la cantidad a transferir: "))
                    while montoTransferencia < 1000:
                        print("No puedes transferir menos de $1.000 pesos.")
                        montoTransferencia = int(input("Ingrese la cantidad a transferir: "))
                    else:
                        if origen == 1:
                            cuentaOrigen = cuenta_1
                        elif origen == 2:
                            cuentaOrigen = cuenta_2
                        if destino == 1:
                            cuentaDestino = cuenta_1
                        elif destino == 2:
                            cuentaDestino = cuenta_2

                        if cuentaOrigen.saldo >= montoTransferencia:
                            cuentaOrigen.saldo -= montoTransferencia
                            cuentaDestino.saldo += montoTransferencia
                            print(f"Has transferido ${montoTransferencia} a la cuenta Nro {cuentaDestino.numero_cuenta}")
                        else:
                            print("No cuentas con saldo suficiente para realizar la transferencia.")
                            time.sleep(2)
                            print("Volviendo al menú principal...")
                            time.sleep(2)
                            return Menu()


        #---------------#
        # CONSULT SALDO #
        #---------------#
        elif option == 6:
            clear()
            Saldo()
            if listaCuentas == []:
                print("No hay ninguna cuenta en nuestro sistema.")
                time.sleep(2)
                print("Volviendo al menú principal...")
                time.sleep(2)
                return Menu()
            else:
                account_number = int(input("Ingrese el número de cuenta: "))
                for cuenta in listaCuentas:
                    if cuenta.numero_cuenta == account_number:
                        cuenta.ConsultarSaldo()
                        time.sleep(2)
                        print("Volviendo al menú principal...")
                        time.sleep(2)
                        return Menu()
                    else:
                        print("No se ha encontrado ninguna cuenta con ese número.\nVolviendo al menú principal...")
                        time.sleep(2)
                        return Menu()

        #---------------#
        # VER MOVIMIENT #
        #---------------#
        elif option == 7:
            clear()
            Saldo()
            if listaCuentas == []:
                print("No hay ninguna cuenta en nuestro sistema.")
                time.sleep(2)
                print("Volviendo al menú principal...")
                time.sleep(2)
                return Menu()
            else:
                account_number = int(input("Ingrese el número de cuenta: "))
                for cuenta in listaCuentas:
                    if cuenta.numero_cuenta == account_number:
                        movimiento.VerMovimiento()
                        print("Volviendo al menú principal...")
                        time.sleep(2)
                        return Menu()
                    else:
                        print("No se ha encontrado ninguna cuenta con ese número.\nVolviendo al menú principal...")
                        time.sleep(2)
                        return Menu()

        #---------------#
        #     SALIR     #
        #---------------#
        elif option == 8:
            print("Saliendo...")
            time.sleep(2)
            exit()
Menu()