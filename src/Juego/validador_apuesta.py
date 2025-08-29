class ValidadorApuesta:
    def __init__(self):
        # Orden de pintas: 2, 3, 4, 5, 6, 1 (ases)
        self.orden_pintas = [2, 3, 4, 5, 6, 1]
    
    def validar_apuesta_inicial(self, apuesta, cantidad_dados):
        if apuesta[1] == 1 and cantidad_dados > 1:
            raise ValueError("No se puede apostar por ases con más de un dado")
    
    def validar_apuesta_subsiguiente(self, apuesta_actual, nueva_apuesta):
        cantidad_actual, pinta_actual = apuesta_actual
        cantidad_nueva, pinta_nueva = nueva_apuesta
        
        # Mayor cantidad, misma pinta
        if pinta_nueva == pinta_actual and cantidad_nueva > cantidad_actual:
            return
        
        # Misma cantidad, mayor pinta
        if cantidad_nueva == cantidad_actual and self._es_pinta_mayor(pinta_nueva, pinta_actual):
            return
        
        # Mayor cantidad y mayor pinta
        if cantidad_nueva > cantidad_actual and self._es_pinta_mayor(pinta_nueva, pinta_actual):
            return
        
        raise ValueError("La nueva apuesta debe ser mayor en cantidad o pinta")
    
    def _es_pinta_mayor(self, pinta1, pinta2):
        return self.orden_pintas.index(pinta1) > self.orden_pintas.index(pinta2)
    
    def calcular_nueva_cantidad_ases(self, cantidad_actual):
        if cantidad_actual % 2 == 0:
            return cantidad_actual // 2 + 1
        else:
            return (cantidad_actual + 1) // 2
    
    def calcular_minimo_cambio_ases(self, cantidad_ases):
        return cantidad_ases * 2 + 1