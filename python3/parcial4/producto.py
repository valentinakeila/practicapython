from random import *
class Producto:
    def __init__(self, nombre: str, precio_unitario: float) -> None:
         self.__nombre = nombre
         self.__codigo = randint(10000, 30000)
         self.__precio_unitario = precio_unitario


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre1):
        self.__nombre =  nombre1


    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo1):
        self.__codigo =  codigo1


    @property
    def precio_unitario(self):
        return self.__precio_unitario
    
    @precio_unitario.setter
    def precio_unitario(self, precioUnitario):
        self.__precio_unitario =  precioUnitario


    def __str__(self) -> str:
        return f"{self.__nombre}{self.__codigo}{self.__precio_unitario}"
    
    @staticmethod
    def validar_codigo(self, codigo: str):
        if codigo == self.__codigo:
            return True, "codigo correcto"
        return False, "codigo no valido"



    















