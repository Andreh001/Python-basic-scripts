class Bibliotecario:
    def __init__(self,  rut, nombre, contrasena):
        self.rut = rut
        self.nombre = nombre
        self.contrasena = contrasena

    #-------------------#
    #   VALIDAR USER    #
    #-------------------#
    def validarUsuario(self, contrasena):
        if self.contrasena == contrasena:
            return True