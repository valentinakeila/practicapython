from usuario import *
from libro import *
from datetime import date

libros = [Libro("El Principito","Antoine de Saint-Exupéry",date(1943,4,6)), Libro("Juan Salvador Gaviota","Richard Bach",date(1970,1,1))]

administrador = Usuario('admin','admin',23, 100000, date(2023,6,20), 'admin',"admi@gmail.com", 'admin')
usuario1 = Usuario("Nicolas", "cataldi",21 , 140000, date(2002,3,20), "nico", "nico@gmail.com","ninini" )
usuario2 = Usuario("Valentina", "Garrido",  12,  789012, date(2009, 1, 1), "valen", "valen@gmail.com","valenlamejor")

usuarios = [usuario1, usuario2, administrador]
usuario2.mis_libros = [libros[0]]


def menu_principal():
    print("1 - Ingresar como usuario")
    print("2 - Ingresar como administrador")
    print("3 - Ver libros del usuario...")
    print("4 - Ver usuario del libro...")
    print("5 - Salir")
def menu_administrador():
    print("1 - Nuevo usuario")
    print("2 - Nuevo libro")
    print("3 - Cerrar sesión")


def menu_usuario():
    print("1 - Agregar libro a mi coleccion")
    print("2 - Quitar libro de mi coleccion")
    print("3 - Cerrar sesión")


def ingresoUsuario():
    user = input("Ingrese usuario\n")
    contraseña = input("Ingrese contraseña\n")

    for usuario in usuarios:
        credenciales_correctas, mensaje = usuario.validar_credenciales(user, contraseña)
        if credenciales_correctas:
            print(mensaje)
            menu_usuario()
            while True:             
                opt = input("Ingrese una opción")
                if opt == "1":

                    isbn = input("Ingrese el ISBN del libro que desea agregar: ")
                    libro_encontrado = None
                    for libro in libros:
                        if libro.isbn == isbn:
                            libro_encontrado = libro
                            break
                        
                    if libro_encontrado:
                        usuario.agregar_libro(libro_encontrado)
                        print("Libro agregado a tu colección.")
                    else:
                        print("El libro no existe.")
                    break
                if opt == "2":
                        isbn = input("Ingrese el ISBN del libro que desea quitar: ")
                        libro_encontrado = None
                        for libro in usuario.mis_libros:
                            if libro.isbn == isbn:
                                libro_encontrado = libro
                                break
                        if libro_encontrado:
                            usuario.quitar_libro(libro_encontrado)
                            print("Libro quitado de tu colección.")
                        else:
                            print("El libro no está en tu colección.")
                     
                        break
                if opt == "3":
                    print("Saludos!.")
                    break

            return
    print("Credenciales incorrectas. Por favor, inténtelo de nuevo.")


def ingresoAdmistrador():
    user = input("Ingrese usuario\n")
    contraseña = input("Ingrese contraseña\n")

    for administrador in usuarios:
        credenciales_correctas, mensaje =administrador.validar_credenciales(user, contraseña)
        if credenciales_correctas:
            print(mensaje)
            menu_administrador()
            
            while True:             
                opt = input("Ingrese una opción")
                if opt == "1":

                    nuevo_usuario()                
                    break
                if opt == "2":
                        nuevo_libro()
                     
                        break
                if opt == "3":
                    print("Saludos!.")
                    break

            return
    print("Credenciales incorrectas. Por favor, inténtelo de nuevo.")



def nuevo_usuario():
    while True:
        user_name = input("Ingrese el nombre de usuario: ")
        # Verificar si el nombre de usuario ya existe
        if any(usuario.user_name == user_name for usuario in usuarios):
            print("El nombre de usuario ya existe. Por favor, ingrese otro.")
        else:
            break


    email = input("Ingrese el email: ")

    while True:
        administrador = input("¿Es administrador? (True/False): ").lower()
        if administrador == "true":
            es_administrador = True
            break
        elif administrador == "false":
            es_administrador = False
            break
        else:
            print("Opción no válida. Por favor, ingrese True o False.")

    contraseña1 = input("Ingrese la contraseña: ")
    contraseña2 = input("Confirme la contraseña: ")

    while contraseña1 != contraseña2 or len(contraseña1) < 8 or len(contraseña1) > 10 or not any(char.isdigit() for char in contraseña1):
        print("Las contraseñas no coinciden o no cumplen con los requisitos.")
        contraseña1 = input("Ingrese la contraseña: ")
        contraseña2 = input("Confirme la contraseña: ")

    # Aquí se solicitan los demás datos del usuario
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = int(input("Ingrese la edad: "))
    nro_documento = int(input("Ingrese el número de documento: "))
    fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()

    nuevo_usuario = Usuario(nombre, apellido, edad, nro_documento, fecha_nacimiento, user_name, email, contraseña1)
    nuevo_usuario.administrador = es_administrador
    usuarios.append(nuevo_usuario)


def nuevo_libro():
    nombre = input("Ingrese el título del libro: ")
    autor = input("Ingrese el nombre del autor: ")
    fecha_lanzamiento = input("Ingrese la fecha de publicación (YYYY-MM-DD): ")
    try:
        fecha_lanzamiento = datetime.strptime(fecha_lanzamiento, "%Y-%m-%d").date()
    except ValueError:
        print("Formato de fecha incorrecto. Utilice el formato YYYY-MM-DD.")
        return


    nuevo_libro = Libro(nombre, autor, fecha_lanzamiento)
    libros.append(nuevo_libro)
    print("Libro creado exitosamente.")

def ver_libros_usuario():
        user_name = input("Ingrese el nombre de usuario: ")
        usuario_encontrado = None
        for usuario in usuarios:
            if usuario.user_name == user_name:
                usuario_encontrado = usuario
                break
        if usuario_encontrado:
            print(f"Libros del usuario {user_name}:")
            for libro in usuario_encontrado.mis_libros:
                print("Título:", libro.nombre)
                print("Autor:", libro.autor)
                print("Fecha de publicación:", libro.fecha_lanzamiento)
            else:
                print("No se encontró el usuario.")
        else:
            print("No se encontró el usuario.")

def ver_usuario_libro():
    isbn = input("Ingrese el ISBN del libro: ")
    libro_encontrado = None
    for libro in libros:
        if libro.isbn == isbn:
            libro_encontrado = libro
            break
    if libro_encontrado:
        print(f"Usuarios que leyeron el libro con ISBN {isbn}:")
        for usuario in usuarios:
            if libro_encontrado in usuario.mis_libros:
                print(usuario.user_name)
    else:
        print("No se encontró el libro.")


while True:

    menu_principal()
    opt = input("Ingrese una opción")
    if opt == "1":

        ingresoUsuario()
        
        continue
    if opt == "2":

        ingresoAdmistrador()
        
        continue
    if opt == "3":
        ver_libros_usuario()
        continue
    if opt == "4":
        ver_usuario_libro()
        continue
    if opt == "5":
        print("Saludos!.")
    break


"""
     La tupla no es explícitamente retornada por el método validar_credenciales(). La tupla se crea implícitamente cuando se usan dos variables separadas para asignar los resultados del método. Permíteme explicarlo con más detalle.

En Python, cuando un método retorna múltiples valores separados por comas, estos valores se empaquetan en una tupla automáticamente. Esto significa que, aunque el método validar_credenciales() parece solo retornar un valor (True o False), en realidad, está retornando una tupla con dos elementos: el primer elemento es el valor booleano que indica si las credenciales son correctas o no, y el segundo elemento es el mensaje relacionado con el resultado de la validación.
    """ 