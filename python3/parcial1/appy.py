from aspirante import Aspirante
from carrera import Carrera
from titulo import Titulo
from inscripcion import Inscripcion
from datetime import date
from datos import *

def menu(): 
    return "\n1 - Nueva Inscripción\n2 - Ver carreras\n3 - Ver inscripciones\n4 - Salir\n"

def nueva_inscripcion():
    for i, carrera in enumerate(carreras, 1):
        print(f"{i}{carrera.nombre}")

    carreraElegida = int(input("elija carrera"))
    carreraSelecciona = carreras[carreraElegida - 1]

    nombre = input("ingrese nombre ")
    apellido = input("ingrese apellido")
    email = input("ingrese email")
    telefono = input("ingresa telefono")

    aspirante = Aspirante(nombre, apellido, email, telefono)


    for i, titulo in enumerate(titulos, 1):
        print(f"{i}{titulo.nombre}")

    tituloElegida = int(input("elija titulo"))
    tituloSelecciona = titulos[tituloElegida - 1]

    aspirante.add_titulo(tituloSelecciona)
    inscripciones.append(Inscripcion(carreraSelecciona, aspirante))
    print("EXITO")


while True:
    print(menu())
    opt = input("Ingrese la opción seleccionada: ")
    if opt == "1":
        nueva_inscripcion()
        continue
    if opt == "2":
        carreraOrdenada = sorted(carreras, key= lambda x:x.comienzo)
        for carrera in carreraOrdenada:
            print(carrera)

        
        continue
    if opt == "3":

        for inscripcion in inscripciones:
            if inscripcion.inscripcion_activa:
                print(inscripcion)
               



       
       
        continue
    if opt == "4":
        print("Saludos.")
        break
    else:
        print("Ingrese una opcion valida.")