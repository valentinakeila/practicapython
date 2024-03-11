class Titulo:
    def __init__(self, nombre : str, universidad: str):
        self.__nombre = nombre
        self.__universidad = universidad


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombreValor):
        self.__nombre = nombreValor

    @property
    def universidad(self):
        return self.__universidad
    
    @universidad.setter
    def universidad(self, universidadValor):
        self.__universidad = universidadValor

    def __str__(self) -> str:
        return f"{self.__nombre} {self.__universidad}"