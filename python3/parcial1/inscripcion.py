from aspirante import *
from carrera import *
from datetime import *

class Inscripcion:

    prox_nro = int(0)
    def __init__(self, carrera: Carrera, aspirante: Aspirante) -> None:
        self.__aspirante = aspirante
        self.__carrera = carrera
        self.__nro = Inscripcion.get_prox_nro()
        self.__fecha_inscripcion = date.today()
        self.__inscripcion_activa = True


    @property
    def aspirante(self) -> object:
        return self.__aspirante
    
    @property
    def carrera(self) -> object:
        return self.__carrera

    @property
    def fecha_inscripcion(self):
        return self.__fecha_inscripcion
    
    @fecha_inscripcion.setter
    def fecha_inscripcion(self,fechaInscripcion):
        self.__fecha_inscripcion = fechaInscripcion


    @property
    def inscripcion_activa(self):
        return self.__inscripcion_activa
    
    @inscripcion_activa.setter
    def inscripcion_activa(self,inscripcionActiva):
        self.__inscripcion_activa= inscripcionActiva



    @property
    def nro(self) -> int:
        return self.__nro


    @classmethod
    def get_prox_nro(cls):
        cls.prox_nro += 1
        return cls.prox_nro
    

    def __str__(self) -> str:
        
        return f"{self.__nro}{self.__aspirante}{self.__carrera}{self.__fecha_inscripcion}{self.__inscripcion_activa}"