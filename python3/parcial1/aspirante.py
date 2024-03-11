
from titulo import *

class Aspirante:
    def __init__(self, nombre: str, apellido:str, email:str, num_telefono: str) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__num_telefono = num_telefono
        self.__titulos = []


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombreValor):
        self.__nombre = nombreValor

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellidoValor):
        self.__apellido = apellidoValor


    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, emailValor):
        self.__email = emailValor


    @property
    def num_telefono(self):
        return self.__num_telefono
    
    @num_telefono.setter
    def num_telefono(self, numTelefonoValor):
        self.__num_telefono = numTelefonoValor


    @property
    def titulos(self):
        return self.__titulos
    
    @titulos.setter
    def titulos(self, titulosValor):
        self.__titulos = titulosValor


    def add_titulo(self, titulo : Titulo):
        self.__titulos.append(titulo)


    def remove_titulo(self, titulo : Titulo):
        self.__titulos.remove(titulo)



    def __str__(self) -> str:
        return f"{self.__nombre}{self.__apellido}{self.__email}{self.__num_telefono}"