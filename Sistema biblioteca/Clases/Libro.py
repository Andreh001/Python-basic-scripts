class Libro:

    def __init__(self, isbn, nombre, autor, estado):
        self.isbn = isbn
        self.nombre = nombre
        self.autor = autor
        self.estado = estado


    #--------------------#
    #   LISTAR LIBROS    #
    #--------------------#
    def verLibro(self):
        if self.estado == 1:
            estado_libro = "Disponible"
        elif self.estado == 0:
            estado_libro = "Prestado"
        print(f'''

    ISBN: {self.isbn}
    Nombre libro: {self.nombre}
    Autor: {self.autor}
    Estado: {estado_libro}
        
''')


    #----------------------#
    #  LIBROS DISPONIBLES  #
    #----------------------#
    def verLibrosDisponibles(self):
        if self.estado == 1:
            print(f'''
    ISBN: {self.isbn}
    Nombre libro: {self.nombre}
    Autor: {self.autor}
    
''')


    #--------------------#
    #  LIBROS PRESTADOS  #
    #--------------------#
    def verLibrosPrestados(self):
        if self.estado == 0:
            print(f'''
    ISBN: {self.isbn}
    Nombre libro: {self.nombre}
    Autor: {self.autor}

''')


    #---------------------#
    #    PRESTAR LIBRO    #
    #---------------------#
    def realizarPrestamo(self, isbn):
        if self.estado == 1:
            self.estado = 0
            print(f"Se ha realizado el prestamo del libro '{self.nombre}' de '{self.autor}'")
        else:
            print("El libro solicitado ya se encuentra prestado.")

    # ----------------------#
    #  REALIZAR DEVOLUCION  #
    #-----------------------#
    def realizarDevolucion(self, isbn):
        if self.estado == 0:
            self.estado = 1
            print(f"¡El libro '{self.nombre}' de '{self.autor}' ha sido devuelto!\nAhora se encuentra disponible.")
        else:
            print("El libro solicitado no se encuentra prestado.")