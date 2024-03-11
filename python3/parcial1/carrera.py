from titulo import *
from datetime import *
class Carrera:
    def __init__(self, nombre:str, comienzo: date) -> None:
        self.__nombre = nombre
        self.__comienzo = comienzo
        self.__titulos_grado_requeridos = []


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombreValor):
        self.__nombre = nombreValor


    @property
    def comienzo(self):
        return f"{self.__comienzo.year}{self.__comienzo.month}"
    
    @comienzo.setter
    def comienzo(self, comienzoValor):
        self.__comienzo = comienzoValor


    

    @property
    def titulos_grado_requeridos(self):
        return self.__titulos_grado_requeridos
    
    @titulos_grado_requeridos.setter
    def titulos_grado_requeridos(self, titulos_grado):
        self.__titulos_grado_requeridos = titulos_grado


    def add_titulo_requerido(self, titulo:Titulo):
        self.__titulos_grado_requeridos.append(titulo)

    def remove_titulo_(self, titulo:Titulo):
        self.__titulos_grado_requeridos.remove(titulo)



    def __str__(self) -> str:
        return f"{self.__nombre}{self.__comienzo}"


