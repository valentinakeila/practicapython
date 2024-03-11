from datos import *

def menu(): 
    return "\n1 - Home\n2 - Nueva Lista\n3 - Ver listas\n4 - Salir\n"

def nuevalista():
    lista = input(" ingrese nombre nueva lista ")
    listaCreada = ListaReproduccion(lista)
    
    for i, video in enumerate(videos, 1):
        print(f"{i}{video.nombre}")

    videoElegido = int(input("elija video"))
    videoSeleccionado = videos[videoElegido- 1]

    listaCreada.add_video(videoSeleccionado)
    listas.append(listaCreada)


    

while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    if opt == "1":

        for video in sorted(videos, key=lambda x: x.nombre):
            print(video)

     
        continue
    if opt == "2":

        nuevalista()
  
        continue
    if opt == "3":
        for lista in listas:
            print(lista.nombre)
        
        continue
    if opt == "4":
        print("Gracias por utilizar nuestro sistema.")
        break
    else:
        print("Error, Ingrese una opcion valida...")