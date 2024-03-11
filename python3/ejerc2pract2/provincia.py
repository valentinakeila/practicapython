from datetime import *
from localidad import *


class Provincia:
    def __init__(self, nombre: str , codigo: int):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__fecha_alta = date.today()
        self.__mis_localidades = []
        

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombreNuevo):
        self.__nombre = nombreNuevo


    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigoNuevo):
        self.__codigo = codigoNuevo

    @property
    def fecha_alta(self):
        return self.__fecha_alta

    @property
    def mis_localidades(self):
        return self.__mis_localidades
    
    @mis_localidades.setter
    def mis_localidades(self, misLocalidades):
        self.__mis_localidades = misLocalidades


    def add_localidad(self, localidad : Localidad):
        self.__mis_localidades.append(localidad)

    def remove_localidad(self, localidad : Localidad):
        self.__mis_localidades.remove(localidad)


    

    def __str__(self) -> str:

        return f"nombre: {self.__nombre} codigo: {self.__codigo} fecha: {self.__fecha_alta} lista{self.__mis_localidades}"
        
        