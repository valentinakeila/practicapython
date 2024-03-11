from datetime import *
class Autor:
    def __init__(self, nombre: str, apellido:str, fecha_nacimiento: date) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre


    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, nuevoApellido):
        self.__apellido = nuevoApellido


    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fechaNacimiento):
        self.__fecha_nacimiento = fechaNacimiento

   
    @property
    def nombre_completo(self) -> str:
        return f"{self.__apellido}, {self.__nombre}"


    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"

    