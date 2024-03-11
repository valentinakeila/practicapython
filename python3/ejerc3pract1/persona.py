from abc import *
from datetime import *

class Persona:
    def __init__(self, nombre:str, apellido: str, edad:int, nro_documento: int, fecha_nacimiento: date):
        self._nombre = nombre
        self._apellido = apellido
        self._fecha_nacimiento = fecha_nacimiento
        self._edad = edad
        self._nro_documento = nro_documento


    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, nuevoApellido):
        self._apellido = nuevoApellido

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, nuevaFechaNacimiento):
        self._fecha_nacimiento = nuevaFechaNacimiento

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, nuevaEdad):
        self._edad = nuevaEdad

    @property
    def nro_documento(self):
        return self._nro_documento
    
    @nro_documento.setter
    def nro_documento(self, nuevoNroDocumento):
        self._nro_documento = nuevoNroDocumento


    


        