from titulo import *

class Profesional:
    def __init__(self, nombre: str, apellido:str, nro_documento: str) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nro_documento = nro_documento
        self.__titulos = []



    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombreNuevo):
        self.__nombre = nombreNuevo


    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellidoNuevo):
        self.__apellido = apellidoNuevo


    @property
    def nro_documento(self):
        return self.__nro_documento
    
    @nro_documento.setter
    def nro_documento(self, nro_documentoNuevo):
        self.__nro_documento = nro_documentoNuevo


    @property
    def titulos(self) -> list:
        return self.__titulos

    def add_titulo(self, titulo: Titulo) -> None:
        self.__titulos.append(titulo)

    def remove_titulo(self, titulo: Titulo) -> None:
        self.__titulos.remove(titulo)




    def __str__(self) -> str:
        return f"{self.__nombre}{self.__apellido}{self.__nro_documento}"
    

    