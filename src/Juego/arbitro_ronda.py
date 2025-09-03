from src.Juego.contador_pintas import ContadorPintas
from src.Juego.validador_apuesta import ValidadorApuesta

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

    def contar_pintas_reales(self, cachos, pinta, usar_comodines=True):
        """
        Cuenta las pintas reales en los cachos para resolver dudas/calces.
        """
        contador = ContadorPintas()
        return contador.contar_pinta(pinta, cachos, usar_comodines)

    def resolver_duda_completa(self, apuesta, cachos, usar_comodines=True):
        """
        Resuelve una duda contando automáticamente las pintas en los cachos.
        
        Args:
            apuesta (tuple): Tupla (cantidad, pinta) apostada.
            cachos (list): Lista de objetos Cacho para contar.
            usar_comodines (bool): Si los ases cuentan como comodines.
            
        Returns:
            str: 'Apostador pierde' o 'Dudador pierde'
        """
        cantidad, pinta = apuesta
        conteo_real = self.contar_pintas_reales(cachos, pinta, usar_comodines)
        return self.resolver_duda(apuesta, conteo_real)

    def resolver_calce_completo(self, apuesta, cachos, usar_comodines=True):
        """
        Resuelve un calce contando automáticamente las pintas en los cachos.
        
        Args:
            apuesta (tuple): Tupla (cantidad, pinta) apostada.
            cachos (list): Lista de objetos Cacho para contar.
            usar_comodines (bool): Si los ases cuentan como comodines.
            
        Returns:
            str: 'Apostador gana' o 'Apostador pierde'
        """
        cantidad, pinta = apuesta
        conteo_real = self.contar_pintas_reales(cachos, pinta, usar_comodines)
        return self.resolver_calce(apuesta, conteo_real)

    def validar_apuesta_inicial(self, apuesta, dados_jugador):
        """
        Valida una apuesta inicial usando ValidadorApuesta.
        
        Args:
            apuesta (tuple): Tupla (cantidad, pinta).
            dados_jugador (int): Cantidad de dados del jugador.
        """
        validador = ValidadorApuesta()
        validador.validar_apuesta_inicial(apuesta, dados_jugador)
