from datetime import *


class Localidad:
    def __init__(self, nombre: str , codigo: int, cod_postal: int):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__cod_postal = cod_postal
        self.__fecha_alta = date.today()
        
        

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
    def cod_postal(self):
        return self.__cod_postal
    
    @cod_postal.setter
    def cod_postal(self, cod_postal):
        self.__cod_postal = cod_postal

    @property
    def fecha_alta(self):
        return self.__fecha_alta

    

    def __str__(self) -> str:

        return f"nombre: {self.__nombre} codigo: {self.__codigo} codigo postal: {self.__cod_postal} fecha: {self.__fecha_alta} "
        