class ContadorPintas:
    """
    Cuenta apariciones de pintas en múltiples cachos.
    """

    def __init__(self):
        """Inicializa con las pintas válidas del juego."""
        self.pintas_validas = ["as", "tontos", "trenes", "cuadras", "quinas", "sextos"]

    def contar_pinta(self, pinta, cachos, usar_comodines=True):
        """
        Cuenta cuántas veces aparece una pinta específica en todos los cachos.

        Args:
            pinta (str): Pinta a contar
            cachos (list): Lista de objetos Cacho
            usar_comodines (bool): Si los ases cuentan como comodines

        Returns:
            int: Número total de dados con esa pinta

        Raises:
            ValueError: Si la pinta no es válida
        """

        if pinta not in self.pintas_validas:
            raise ValueError("Pinta inválida")

        contador = 0

        for cacho in cachos:
            for dado in cacho.dados:
                valor_dado = dado.obtener_valor()

                if valor_dado == pinta:
                    contador += 1

                if usar_comodines and valor_dado == "as" and pinta != "as":
                    contador += 1

        return contador