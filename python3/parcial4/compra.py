from datetime import *
from producto import *
from cliente import *
from descuento import*

class Compra:
    def __init__(self, cliente: Cliente) -> None:
        self.__cliente = cliente
        self.__fecha_hora = datetime.now()
        self.__compra_facturada = False
        self.__monto_facturado = 0
        self.__monto_total = 0
        self.__mis_productos = []


    @property
    def cliente(self):
        return self.__cliente

    
    @property
    def fecha_hora(self):
        return self.__fecha_hora
    
    @fecha_hora.setter
    def fecha_hora(self, fechaHora):
        self.__fecha_hora = fechaHora

    @property
    def compra_facturada(self):
        return self.__compra_facturada
    
    @compra_facturada.setter
    def compra_facturada(self,compraFacturada):
        self.__compra_facturada = compraFacturada


    @property
    def monto_facturado(self):
        return self.__monto_facturado
    
    @monto_facturado.setter
    def monto_facturado(self,montoFacturado):
        self.__monto_facturado = montoFacturado

    @property
    def cantidad_productos(self):
        return len(self.__mis_productos)
    
    @property
    def monto_total(self):
        return self.__monto_total

    @monto_total.setter
    def monto_total(self, monto):
        self.__monto_total = monto


    @property
    def mis_productos(self):
        return self.__mis_productos
    
    @mis_productos.setter
    def mis_productos(self, productos1):
        self.__mis_productos= productos1


    def add_producto(self, producto: Producto):
        self.__mis_productos.append(producto)

    def remove_producto(self, producto: Producto):
        self.__mis_productos.remove(producto)


    def facturar_compra(self):
        for producto in self.__mis_productos:
            self.__monto_total += producto.precio_unitario
        if self.__cliente.nro_comunidad != None:
            self.__monto_facturado = self.__monto_total
            self.__compra_facturada = True
        else:
            self.__monto_facturado = Descuento.pago_con_comunidad(self.__monto_total)
            self.__compra_facturada = True
        return self.__monto_facturado


    def __str__(self):
        return f"Cliente: {self.__cliente} Fecha de la compra: {self.__fecha_hora} Cantidad de productos: {self.__mis_productos} Monto a total pagar: {self.__monto_total} Monto con descuento aplicado: {self.facturar_compra()}"




    


    


    