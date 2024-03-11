from profesional import *
from datetime import *

class Inscripcion:

    prox_nro = int(0)

    def __init__(self):
        self.__nro = Inscripcion.get_nro()
        self.__fecha_hora_inscripcion = date.today().hour
        self.__inscripcion_activa = False

    

    @property
    def fecha_hora_inscripcion(self):
        return self.__fecha_hora_inscripcion
    
    @fecha_hora_inscripcion.setter
    def fecha_hora_inscripcion(self, fechaHoraInscripcion):
        self.__fecha_hora_inscripcion = fechaHoraInscripcion


    @property
    def inscripcion_activa(self):
        return self.__inscripcion_activa
    
    @inscripcion_activa.setter
    def inscripcion_activa(self, inscripcionActiva):
        self.__inscripcion_activa= inscripcionActiva


    
    @property
    def nro(self) -> int:
        return self.__nro
    
    
    @classmethod
    def get_nro(cls):
        cls.prox_nro += 1
        return cls.prox_nro
        

    def __str__(self) -> str:
        return f"{self.__nro}{self.__fecha_hora_inscripcion}{self.__inscripcion_activa}"