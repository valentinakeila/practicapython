class Genero:
    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre

    def __str__(self) -> str:
        return f"Nombre:{self.__nombre} "