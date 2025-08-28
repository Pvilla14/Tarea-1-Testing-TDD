class ValidadorApuesta:
    def validar_apuesta_inicial(self, apuesta, cantidad_dados):
        if apuesta[1] == 1 and cantidad_dados > 1:
            raise ValueError("No se puede apostar por ases con más de un dado")