class ContadorPintas:
    """
    Cuenta apariciones de pintas en múltiples cachos.
    """

    def contar_pinta(self, pinta, cachos, usar_comodines=True):
        """
        Cuenta cuántas veces aparece una pinta específica en todos los cachos.

        Args:
            pinta (str): Pinta a contar
            cachos (list): Lista de objetos Cacho
            usar_comodines (bool): Si los ases cuentan como comodines

        Returns:
            int: Número total de dados con esa pinta
        """
        contador = 0

        for cacho in cachos:
            for dado in cacho.dados:
                valor_dado = dado.obtener_valor()

                if valor_dado == pinta:
                    contador += 1

                if usar_comodines and valor_dado == "as" and pinta != "as":
                    contador += 1

        return contador