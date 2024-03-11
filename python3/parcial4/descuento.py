class Descuento:
    descuento_comunidad = 0.30


    @staticmethod
    def pago_con_comunidad(monto: float):
        return monto -(monto * Descuento.descuento_comunidad)

