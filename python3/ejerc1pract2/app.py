from estadia import *
from precio import *


estadias = [Estadia("0000")]



def ingreso():
    while True:

        auto = input("Ingrese patente")
        if any(estadia.nro_patente == auto for estadia in estadias):
            print("no valido")
        
        else: 
            estadia = Estadia(auto)
            estadias.append(estadia)
            print("Registrado")
    
            break


def egreso():
    patente = input("Ingrese el número de patente: ")
    bandera_patente_encontrada = False
    for estadia in estadias:
        if patente == estadia.nro_patente:
            bandera_patente_encontrada = True
            if estadia.estado == "ACTIVO" and estadia.pagado == False:
                estadia.registrar_salida()
                importe = Precio.calcular_importe(estadia.cantHoras)
                """
                Aquí, estadia.registrar_salida() llama al método registrar_salida() del objeto estadia. Este método calcula la cantidad de horas que ha estado estacionado el vehículo y establece la hora de salida en el objeto estadia.
                Una vez que la salida se ha registrado, estadia.cantHoras contiene la cantidad de horas que el vehículo estuvo estacionado. Luego, Precio.calcular_importe(estadia.cantHoras) calcula el importe a pagar por la estadía utilizando el método estático calcular_importe() de la clase Precio, pasando la cantidad de horas como argumento.
                """
                print(f"El precio a pagar es ${importe}")
                confirmacion = input("¿Desea confirmar el pago? (s/n): ")
                if confirmacion.lower() == "s":
                    estadia.pagado = True
                    estadia.estado = "PAGADO"
                    estadia.hora_salida = datetime.now().hour
                    print("El pago ha sido confirmado.")
                    print(estadia)
            else:
                print("La estadía ya ha sido finalizada o pagada.")
            break

        

     
    








opcion = 0
while opcion != 3:
    print("Menú:")
    print("1. Ingresar Estadia")
    print("2. Finalizar Estadia")
    print("3. Salir")
    opcion = input("ingrese opcion")

    if opcion == "1":
        ingreso()

    elif opcion == "2":

        egreso()

    elif opcion == "3":

        print("saludos!")

        break

    else: 
        print("opcion no valida")

    

"""
En el contexto del código, la palabra "estadia" se refiere a un objeto de la clase Estadia. Es la variable que utilizamos para iterar sobre la lista de estadías en el bucle for.

En el bucle for, cada iteración asigna un objeto de la clase Estadia a la variable estadia. Entonces, cada vez que veas estadia dentro del bucle for, se está refiriendo a un objeto específico de la clase Estadia dentro de la lista estadias.

Por ejemplo, en la línea for estadia in estadias:, estadia se refiere a un objeto de la clase Estadia en la lista estadias. Y cuando escribimos estadia.nro_patente, estamos accediendo al atributo nro_patente de ese objeto específico. Lo mismo ocurre con otras propiedades y métodos, como estadia.registrar_salida() o estadia.pagado.
"""
