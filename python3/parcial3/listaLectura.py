
from libro import *
class ListaLectura:
    __codigos = set()
    def __init__(self, nombre: str, codigo: int):
        self.__codigo = self.__validar_codigo()
        self.__nombre = nombre
        self.__libros = []


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre


    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def cantidad_libros(self):
        return len(self.__libros)
    

    @property
    def libros(self):
        return self.__libros
    
    @libros.setter
    def libros(self, nuevoLibros):
        self.__libros= nuevoLibros
    
    def add_libro(self, libro: Libro):
        self.__libros.append(libro)

    def remove_libro(self, libro:Libro):
        self.__libros.remove(libro)


    @classmethod
    def __validar_codigo(cls, codigo):
        if codigo in cls.__codigos:
            raise Exception("El codigo está repetido")
        cls.__codigos.add(codigo)
        return codigo


"""if self._email == email and self._contrasenia == contrasenia:
            return True, "Credenciales correctas"
        return False, "Credenciales incorrectas"""
    



    