from datos import *
def menu(): 
    return "\n1 - Pagina principal\n2 - Nueva Lista de lectura\n3 - Ver listas de lectura\n4 - Salir\n"





while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    if opt == "1":

        for libro in sorted(libros, key=lambda x: x.nombre ):
            print(libro)
       
        continue
    if opt == "2":
        nueva_lista()
        continue
    if opt == "3":
        
        continue
    if opt == "4":
        print("Gracias por utilizar nuestro sistema.")
        break
    else:
        print("Error, Ingrese una opcion valida...")