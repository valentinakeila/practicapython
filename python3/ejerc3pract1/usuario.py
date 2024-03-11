from datetime import date
from persona import *
from libro import *

class Usuario(Persona):
    def __init__(self, nombre: str, apellido: str, edad: int, nro_documento: int, fecha_nacimiento: date, user_name: str, email:str, contraseña: str):
        super().__init__(nombre, apellido, edad, nro_documento, fecha_nacimiento)

        self.__user_name = user_name
        self.__estado = True
        self.__administrador = False
        self.__email = email
        self.__contraseña = contraseña
        self.__fecha_alta = date.today()
        self.__fecha_baja = None
        self.__mis_libros = []


    @property
    def user_name(self):
        return self.__user_name
    
    @property
    def administrador(self):
         return self._administrador
    
    @administrador.setter
    def administrador(self, nuevoAdministrador):
        self.__administrador = nuevoAdministrador

    @property
    def contraseña(self):
        return self.__contraseña

    @contraseña.setter
    def contraseña(self, valorContraseña):
        self.__contraseña = valorContraseña


    @property
    def fecha_alta(self):
        return self.__fecha_alta

    @property
    def fecha_baja(self):
        return self.__fecha_baja

    @fecha_baja.setter
    def fecha_baja(self, nuevaFechaBaja):
        self.__fecha_baja = nuevaFechaBaja




    def validar_credenciales(self, user_name_ingresado: str, contraseña_ingresada: str) -> bool:
        if self.__user_name == user_name_ingresado and self.__contraseña == contraseña_ingresada:
            return True, "Credenciales correctas"
        return False, "Credenciales incorrectas"
    
    def baja_usuario(self):
        self.__estado = False
        self.__fecha_baja = date.today()




    @property
    def mis_libros(self):
        return self.__mis_libros

    @mis_libros.setter
    def mis_libros(self, valor):
        self.__mis_libros = valor


    def leyo_libro(self, nombre):
        for i in range(0, len(self.__mis_libros)):
            if nombre == self.__mis_libros[i].nombre:
                return True



    def agregar_libro(self, libro: Libro):
        self.__mis_libros.append(libro)


    def quitar_libro(self, libro:Libro):
        self.__mis_libros.remove(libro)
        

    


    


    


    


    


    



    





