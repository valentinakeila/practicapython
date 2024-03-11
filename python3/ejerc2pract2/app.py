from datos import *
from cliente import *




clientes = []

def registrarCliente():
    nombre = input("Ingrese nombre y apellido")
    

    print("Países disponibles:")
    for i, pais in enumerate(paises):
        print(f"{i + 1}. {pais.nombre}")

    while True:
        paisSeleccionado = int(input("Seleccione pais"))
        if paisSeleccionado < 1 or paisSeleccionado > 2:
            print("no valido")
        
        else: 
            eleccionPais = paises[paisSeleccionado -1]
            break

    print("Provincias disponibles:")

    for i, provincia in enumerate(eleccionPais.mis_provincias, 1):
        print (f"{i} {provincia.nombre}")


    while True:
        provinciaSeleccionado = int(input("Seleccione pronvincia"))
        if provinciaSeleccionado < 1 or provinciaSeleccionado > 3:
            print("no valido")
        
        else: 
            eleccionProvincia = provincias[provinciaSeleccionado -1]
            break


    print("Provincias disponibles:")

    for i, localidad in enumerate(eleccionProvincia.mis_localidades, 1):
        print (f"{i} {localidad.nombre}")


    while True:
        localidadSeleccionado = int(input("Seleccione localidad"))
        if localidadSeleccionado < 1 or localidadSeleccionado > 3:
            print("no valido")
        
        else: 
            eleccionLocalidad = localidades[localidadSeleccionado -1]
            break


    direccion = input("Ingrese direccion")

    datosCliente = (f"{eleccionPais.nombre} {eleccionProvincia.nombre}{ eleccionLocalidad.nombre}{direccion}")

    cliente = Cliente(nombre, datosCliente)
    clientes.append(cliente)
    
    
    print(cliente.get_nro_cliente())
            

    
def buscarCliente():
    numero = int(input("Ingrese número de cliente: "))
    encontrado = False
    for cliente in clientes:
        if numero == cliente.get_nro_cliente():
            print("Cliente encontrado")
            encontrado = True
            break
    
    if not encontrado:
        print("Cliente no encontrado")
    


    

    


  


    




opcion = 0
while opcion != 3:
    print("1-Registrar")
    print("2- Buscar")
    opcion = input("Ingrese opcion")
    if opcion == "1":
        registrarCliente()
        
    
    elif opcion == "2":

        buscarCliente()
    elif opcion == "3":
        print("saludos")
        break

    else:
        print("no valido")

