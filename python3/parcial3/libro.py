from datetime import *
from autor import *
from genero import *
class Libro:
    def __init__(self, nombre : str, autor: Autor = None) -> None:
        self.__nombre = nombre
        self.__fecha_publicacion = date.today()
        self.__generos_libros = []
        self.__autor = autor


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre

    @property
    def autor(self) -> Autor:
        return self.__autor

    @property
    def fecha_publicacion(self):
        return f"{self.__fecha_publicacion.day}{self.__fecha_publicacion.month}{self.__fecha_publicacion.year}"
    
    

    @property
    def generos_libros(self):
        return self.__generos_libros
    
    @generos_libros.setter
    def generos_libros(self, generosLibros):
        self.__generos_libros = generosLibros

    def add_genero(self, genero:Genero):
        self.__generos_libros.append(genero)

    def remove_genero(self, genero:Genero):
        self.__generos_libros.remove(genero)


    def __str__(self) -> str:
        return f"nombre libro:{self.__nombre} [ Autor: {self.autor.nombre if self.autor else 'unknow'} fecha publicacion: {self.__fecha_publicacion}"
