from datos import *



def menu(): 
    return "\n1 - Nueva Compra\n2 - Resumen Compras\n3 - Salir\n"

def menu_compra():
    return "\n1 - Agregar Producto\n2 - Finalizar Compra\n"



while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    opt2 = 0
    if opt == "1":
            nombreCliente = input("Ingrese su nombre")
            apellidoCliente = input("Ingrese su apellido")
            dniCliente = input("Ingrese su dni")
            cliente3 = (Cliente(nombreCliente,apellidoCliente,dniCliente))
            while opt != 3: 
   
                print(menu_compra())   
                opt2 = input("Ingrese una opcion: ")
                if opt2 == "1":
                   
                    for i, producto in enumerate(productos):
                        print(f"{i+1}. {producto}")

                    productoElegido = int(input("elija producto"))
                    productoSeleccionado = productos[productoElegido- 1]

                    compra1 = Compra(cliente3)

                    compra1.add_producto(productoSeleccionado)

                    

                
                    
                  
                elif opt2 == "2" :

                    compras.append(compra1)

                    print(compra1)

                elif opt2 == "3":
                    print("chau")
                    break


                    
                else:
                    print("Error, Ingrese una opcion valida...")



                      
            
    elif opt == "2":

        for i in range(len(compras)):
            print(compras[i])


        pass
    elif opt == "3":
        print("Gracias por utilizar nuestro sistema.")
        break
    else:
        print("Error, Ingrese una opcion valida...")

