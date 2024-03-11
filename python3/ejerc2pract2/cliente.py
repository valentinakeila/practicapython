from datetime import *
class Cliente:
    prox_nro_cliente = 0

    def __init__(self, nombre_apellido: str, direccion: str):
        self.__nombre_apellido = nombre_apellido
        self.__nro_cliente = Cliente.get_nro_cliente()
        self.__direccion = direccion
        self.__fecha_alta = date.today()
        self.__fecha_baja = None
        




    @property
    def nombre_apellido(self):
        return self.__nombre_apellido
    
    @nombre_apellido.setter
    def nombre_apellido(self, nombreApellido):
        self.__nombre_apellido = nombreApellido

    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self, direccionNueva):
        self.__direccion = direccionNueva


    @property
    def fecha_alta(self):
        return self.__fecha_alta
    
    @property
    def fecha_baja(self):
        return self.__fecha_baja
    
    @fecha_baja.setter
    def fecha_baja(self, fechaBaja):
        self.__fecha_baja = fechaBaja


    @classmethod
    def get_nro_cliente(cls):
        cls.prox_nro_cliente += 1
        return cls.prox_nro_cliente
    

    def eliminar_cliente(self):
        self.__fecha_baja= date.today()


    def reactivar_cliente(self):
        self.__fecha_baja= date.today()


    def __str__(self) -> str:
        return f"{self.__nombre_apellido}{self.__nro_cliente}{self.__direccion }{self.__fecha_alta } {self.__}"
    



