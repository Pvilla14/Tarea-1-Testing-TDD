class ArbitroRonda:
    """
    Arbitra la resolución de dudas y calces en una ronda de Dudo.
    Decide quién pierde o gana un dado según las reglas del juego.
    """

    def resolver_duda(self, apuesta, conteo_real):
        """
        Resuelve la acción de 'duda' comparando la apuesta con el conteo real.

        Args:
            apuesta (tuple): Tupla (cantidad, pinta) apostada.
            conteo_real (int): Cantidad real de la pinta en juego.

        Returns:
            str: 'Apostador pierde' si la apuesta fue incorrecta,
                 'Dudador pierde' si la apuesta fue correcta.
        """
        cantidad, pinta = apuesta
        if conteo_real < cantidad:
            return 'Apostador pierde'
        else:
            return 'Dudador pierde'

    def resolver_calce(self, apuesta, conteo_real):
        """
        Resuelve la acción de 'calce' verificando si el conteo es exacto.

        Args:
            apuesta (tuple): Tupla (cantidad, pinta) apostada.
            conteo_real (int): Cantidad real de la pinta en juego.

        Returns:
            str: 'Apostador gana' si el conteo es exacto,
                 'Apostador pierde' si no lo es.
        """
        cantidad, pinta = apuesta
        if conteo_real == cantidad:
            return 'Apostador gana'
        else:
            return 'Apostador pierde'

    def validar_calce(self, dados_restantes, dados_jugador, dados_iniciales):
        """
        Valida si está permitido calzar según las reglas del juego.

        Args:
            dados_restantes (int): Total de dados en juego.
            dados_jugador (int): Dados que tiene el jugador que desea calzar.
            dados_iniciales (int): Dados iniciales en la ronda.

        Returns:
            bool: True si se puede calzar, False en caso contrario.
        """
        return dados_jugador == 1 or dados_restantes >= self.mitad(dados_iniciales)

    def mitad(self, total):
        return (total + 1) // 2