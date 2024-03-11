from datos import *




def nuevaInscripcion():
    for indice, concurso in enumerate(concursos, start=1):
        print(f"{indice} {concurso}")
        
        





def cancelarInscripcion():
    print()
def registrarProfesional():
    print()




while True:


    print("1-Nueva Inscripción")
    print("2-Cancelar inscripción")
    print("3-Registrar profesional")
    opcion = input("Ingrese una opcion")


    if opcion == "1":

        nuevaInscripcion()

        

    elif opcion == "2":

        cancelarInscripcion()
    

    elif opcion == "3":
        registrarProfesional()



    
    elif opcion == "4":
        print("Saludos")
        break
    
    else: 
        print("no valido") 

