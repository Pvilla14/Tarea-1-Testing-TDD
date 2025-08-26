class GeneradorAleatorio:
    def generar(self, min, max):
        if min > max:
            raise ValueError("min no puede ser mayor que max")
        return 3  # Sigue devolviendo 3 por ahora