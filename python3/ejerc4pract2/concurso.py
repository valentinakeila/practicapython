from datetime import *
from inscripcion import *



class Concurso:
    def __init__(self, nombre : str):
        self.__nombre = nombre
        self.__fecha_inscripcion_desde = date.today()
        self.__fecha_inscripcion_hasta = None
        self.__inscripciones = []


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombreNuevo):
        self.__nombre = nombreNuevo


    @property
    def fecha_inscripcion_desde(self):
        return self.__fecha_inscripcion_desde
    
    @fecha_inscripcion_desde.setter
    def fecha_inscripcion_desde(self, fechaInscripcionDesde):
        self.__fecha_inscripcion_desde = fechaInscripcionDesde


    @property
    def fecha_inscripcion_hasta(self):
        return self.__fecha_inscripcion_hasta
    
    @fecha_inscripcion_hasta.setter
    def fecha_inscripcion_hasta(self, fechaInscripcionHasta):
        self.__fecha_inscripcion_hasta = fechaInscripcionHasta

    @property
    def inscripciones(self):
        return self.__inscripciones
    
    @inscripciones.setter
    def inscripciones(self, inscripcionesNuevo):
        self.__inscripciones= inscripcionesNuevo


    def add_inscripcion(self, inscripcion: Inscripcion):
        self.__inscripciones.append(inscripcion)


    def remove_inscripcion(self, inscripcion: Inscripcion):
        self.__inscripciones.remove(inscripcion)


    def get_inscripciones_activas(self):
        for inscripcion in self.__inscripciones:
            if inscripcion.inscripcion_activa:
             print(inscripcion)


    def __str__(self) -> str:
        return f"{self.__nombre}{self.__fecha_inscripcion_desde}"
            
               


    

        