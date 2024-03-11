class Titulo:
    def __init__(self, nombre: str , codigo:int):
        self.__nombre = nombre
        self.__codigo = codigo

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombreNuevo):
        self.__nombre = nombreNuevo

    @property
    def codigo(self):
        return self.__codigo
    
    @nombre.setter
    def codigo(self, codigoNuevo):
        self.__codigo = codigoNuevo



    def __str__(self) -> str:
        return f"{self.__nombre}{self.__codigo}"
    

    