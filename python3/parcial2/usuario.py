class Usuario:
    def __init__(self, nombre: str, apellido:str, email:str, password:str) -> None:
         self.__nombre = nombre
         self.__apellido = apellido
         self.__email= email
         self.__password = password



    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nombreValor):
        self.__nombre = nombreValor


    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self,apellidoValor):
        self.__apellido = apellidoValor


    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,emailValor):
        self.__email = emailValor


    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,passwordValor):
        self.__password = passwordValor



    def __str__(self) -> str:
        
        return f"{self.__nombre} {self.__apellido} {self.__email} {self.__password}"
    

    def validar_credenciales(self, email_ingresado, password_ingreado):
        if self.__email == email_ingresado and self.__password == password_ingreado:
            return True, "Datos correctos"
        return False, "Datos incorrectos"


    

    