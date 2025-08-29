class ValidadorApuesta:
    """
    Valida las reglas para las apuestas en el juego de cacho.
    """

    def __init__(self):
        """
        Inicializa el validador con el orden de pintas y las pintas válidas.
        """
        # Orden de pintas: 2, 3, 4, 5, 6, 1 (ases)
        self.orden_pintas = [2, 3, 4, 5, 6, 1]
        self.pintas_validas = [1, 2, 3, 4, 5, 6]
    
    def validar_apuesta_inicial(self, apuesta, cantidad_dados):
        """
        Valida la apuesta inicial según las reglas del juego.

        Args:
            apuesta (tuple): Tupla (cantidad, pinta).
            cantidad_dados (int): Número de dados del jugador.

        Raises:
            ValueError: Si la apuesta no es válida.
        """
        self._validar_formato_apuesta(apuesta)
        
        cantidad, pinta = apuesta
        
        if pinta == 1 and cantidad_dados > 1:
            raise ValueError("No se puede apostar por ases con más de un dado")
    
    def validar_apuesta_subsiguiente(self, apuesta_actual, nueva_apuesta):
        """
        Valida que la nueva apuesta sea válida respecto a la apuesta actual.

        Args:
            apuesta_actual (tuple): Apuesta anterior (cantidad, pinta).
            nueva_apuesta (tuple): Nueva apuesta (cantidad, pinta).

        Raises:
            ValueError: Si la nueva apuesta no es válida.
        """
        self._validar_formato_apuesta(apuesta_actual)
        self._validar_formato_apuesta(nueva_apuesta)
        
        cantidad_actual, pinta_actual = apuesta_actual
        cantidad_nueva, pinta_nueva = nueva_apuesta
        
        # Reglas especiales para cambios de ases
        if pinta_actual != 1 and pinta_nueva == 1:
            # Cambiar a ases
            cantidad_esperada = self.calcular_nueva_cantidad_ases(cantidad_actual)
            if cantidad_nueva != cantidad_esperada:
                raise ValueError(f"Al cambiar a ases, la cantidad debe ser {cantidad_esperada}")
            return
        
        if pinta_actual == 1 and pinta_nueva != 1:
            # Cambiar de ases
            cantidad_minima = self.calcular_minimo_cambio_ases(cantidad_actual)
            if cantidad_nueva < cantidad_minima:
                raise ValueError(f"Al cambiar de ases, la cantidad debe ser al menos {cantidad_minima}")
            return
        
        # Validación normal
        if pinta_nueva == pinta_actual and cantidad_nueva > cantidad_actual:
            return
        
        if cantidad_nueva == cantidad_actual and self._es_pinta_mayor(pinta_nueva, pinta_actual):
            return
        
        if cantidad_nueva > cantidad_actual and self._es_pinta_mayor(pinta_nueva, pinta_actual):
            return
        
        raise ValueError("La nueva apuesta debe ser mayor en cantidad o pinta")
    
    def _es_pinta_mayor(self, pinta1, pinta2):
        """
        Determina si pinta1 es mayor que pinta2 según el orden de pintas.

        Args:
            pinta1 (int): Pinta a comparar.
            pinta2 (int): Pinta base.

        Returns:
            bool: True si pinta1 es mayor que pinta2, False en caso contrario.
        """
        return self.orden_pintas.index(pinta1) > self.orden_pintas.index(pinta2)
    
    def calcular_nueva_cantidad_ases(self, cantidad_actual):
        """
        Calcula la cantidad de ases necesaria al cambiar de otra pinta a ases.

        Args:
            cantidad_actual (int): Cantidad de la apuesta anterior.

        Returns:
            int: Nueva cantidad de ases requerida.
        """
        if cantidad_actual % 2 == 0:
            return cantidad_actual // 2 + 1
        else:
            return (cantidad_actual + 1) // 2
    
    def calcular_minimo_cambio_ases(self, cantidad_ases):
        """
        Calcula la cantidad mínima al cambiar de ases a otra pinta.

        Args:
            cantidad_ases (int): Cantidad de ases apostados.

        Returns:
            int: Cantidad mínima requerida para la nueva apuesta.
        """
        return cantidad_ases * 2 + 1
    
    def _validar_formato_apuesta(self, apuesta):
        """
        Valida que la apuesta tenga el formato correcto.

        Args:
            apuesta (tuple): Apuesta a validar.

        Raises:
            ValueError: Si la apuesta no tiene el formato correcto.
        """
        if not isinstance(apuesta, tuple) or len(apuesta) != 2:
            raise ValueError("La apuesta debe ser una tupla (cantidad, pinta)")
        
        cantidad, pinta = apuesta
        
        if not isinstance(cantidad, int) or cantidad < 1:
            raise ValueError("La cantidad debe ser un entero positivo")
        
        if pinta not in self.pintas_validas:
            raise ValueError("La pinta debe ser un valor entre 1 y 6")