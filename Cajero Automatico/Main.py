import Login
import time
import os
version = "1.0.3"
print("Verificando actualizaciones...")
try:
    import requests
    try:
        lastversion = requests.get("http://andreh001.ml/uploads/version-cajero.txt").text
        if lastversion == version:
            print("Estás usando la versión más reciente.")
            time.sleep(2)
            Login.LoginSystem()
        elif lastversion < version:
            print("Se ha encontrado una actualización de Sistema, descarguela desde http://andreh001.ml/?p=uploads&dl=CajeroAutomatico.zip")
    except:
        exit()
except ModuleNotFoundError:
    print("Este equipo no cuenta con una librería necesaria para el funcionamiento del programa.")
    time.sleep(2)
    print()
    print("Instalaremos automáticamente la librería en unos segundos...")
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