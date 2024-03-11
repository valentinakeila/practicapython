class Tag:
    def __init__(self, nombre : str) -> None:
        self.__nombre = nombre


    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombreValor):
        self.__nombre = nombreValor


    def __str__(self) -> str:
        return f"Nombre: {self.__nombre}"