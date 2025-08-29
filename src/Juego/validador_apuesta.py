class ValidadorApuesta:
    def validar_apuesta_inicial(self, apuesta, cantidad_dados):
        if apuesta[1] == 1 and cantidad_dados > 1:
            raise ValueError("No se puede apostar por ases con más de un dado")
    
    def validar_apuesta_subsiguiente(self, apuesta_actual, nueva_apuesta):
        # Implementación mínima - solo verifica que la nueva apuesta sea mayor en cantidad
        if nueva_apuesta[0] <= apuesta_actual[0]:
            raise ValueError("La nueva apuesta debe ser mayor en cantidad o pinta")