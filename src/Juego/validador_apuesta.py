class ValidadorApuesta:
    def validar_apuesta_inicial(self, apuesta, cantidad_dados):
        if apuesta[1] == 1 and cantidad_dados > 1:
            raise ValueError("No se puede apostar por ases con más de un dado")
    
    def validar_apuesta_subsiguiente(self, apuesta_actual, nueva_apuesta):
        cantidad_actual, pinta_actual = apuesta_actual
        cantidad_nueva, pinta_nueva = nueva_apuesta
        if cantidad_nueva < cantidad_actual or (cantidad_nueva == cantidad_actual and pinta_nueva <= pinta_actual):
            raise ValueError("La nueva apuesta debe ser mayor en cantidad o pinta")