from tag import *
from datetime import *
from usuario import *


class Video:
    def __init__(self, nombre : str, fecha_publicacion: date) -> None:
           self.__nombre = nombre
           self.__fecha_publicacion = fecha_publicacion
           self.__palabras_claves =[]



    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombreValor):
        self.__nombre = nombreValor

    @property
    def fecha_publicacion(self):
        return f"{self.__fecha_publicacion.day}{self.__fecha_publicacion.month} {self.__fecha_publicacion.year}"

    @fecha_publicacion.setter
    def fecha_publicacion(self,fechaPublicacion):
        self.__fecha_publicacion = fechaPublicacion

    @property
    def palabras_claves(self):
        return self.__palabras_claves
    @palabras_claves.setter
    def palabras_claves(self,palabrasClaves):
        self.__palabras_claves = palabrasClaves

    def add_tag(self, tag: Tag):
        self.__palabras_claves.append(tag)


    def remove_tag(self, tag: Tag):
        self.__palabras_claves.remove(tag)


    def __str__(self) -> str:
        return f"{self.__nombre}{self.__fecha_publicacion}"


    











