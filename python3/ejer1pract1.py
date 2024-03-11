from datetime import *

"""
Codificar todos los atributos privados con @property.
Para crear (instanciar) un usuario:
Se ingresa el user_name y email. Se asigna en fecha_alta la fecha del día y estado True.
Luego se le solicita al usuario que ingrese su contraseña.
Una vez creado el usuario al mismo no se le puede cambiar el user_name(sólo lectura).
Luego de creado el usuario, se pueden ingresar los demás datos del usuario.
Al dar de baja el usuario, el mismo no se elimina, si no que su estado cambia a False y se le
asigna en fecha_baja la fecha del día.
Al validar las credenciales, se retorna verdadero si el usuario y pass ingresado coincide con el
user_name y password el usuario; en caso contrario se retorna False.
Tecnicatura Universitaria en Programación - Programación II
Utilizar lossiguientesimports y funciones/métodos.
from datetime import date
x = date.today()

"""

class Usuario:
    def __init__(self,user_name: str, email: str, password:str ):
        self.__user_name = user_name
        self.__estado = True
        self.__email = email
        self.__password = password
        self.__nombre  = ""
        self.__apellido = ""
        self.__fecha_alta = date.today()
        self.__fecha_baja = None


    




    @property
    def user_name(self):
        return self.__user_name
    
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, nuevoEstado: bool):
        self.__estado = nuevoEstado


    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, nuevoEmail: str):
        self.__email = nuevoEmail

    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, nuevaPassword: str):
        self.__password = nuevaPassword

    @property
    def nombre(self):
        return self.__nombre 
    
    @nombre.setter
    def nombre(self, nuevoNombre :str):
        self.__nombre = nuevoNombre

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, nuevoApellido: str):   
        self.__apellido = nuevoApellido


    @property
    def fecha_baja(self):
        return self.__fecha_baja
    
    @fecha_baja.setter
    def fecha_alta(self, fechaBaja : bool):
        self.__fecha_baja = fechaBaja


    def validar_credenciales(self, email_ingresado: str, password_ingresada: str) -> bool:
        return email_ingresado == self.__email and password_ingresada == self.__password
    

    def darBaja(self):
        self.__estado = False
        self.__fecha_baja = date.today()




usuarios =[]
user = input("Ingrese su user")
email = input("Ingrese mail")
password = input("ingrese contrasenia")
usuario = Usuario(user, email, password)


nombre = input("\nIngrese su nombre: ")
apellido = input("\nIngrese su apellido: ")

usuario.nombre = nombre #aca esta usando el setter de nombre porque pide que ingreses datos despues de creado el objeto
usuario.apellido = apellido

respuesta = input("Queres dar de baja la cuenta?\n1 - Sipi\n2 - Jamasss")
if respuesta == "1": #SI PONES UN
    usuario.estado = False
    usuario.fecha_baja = date.today()

usuarios.append(usuario)




    


    


        
