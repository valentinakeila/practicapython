class Precio:
    precio_hora = 100

    @staticmethod
    def calcular_importe(cant_horas: int) -> float:
        return Precio.precio_hora * cant_horas

