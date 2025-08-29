import unittest
from unittest.mock import patch, MagicMock
from src.Juego.contador_pintas import ContadorPintas
from src.Juego.cacho import Cacho


class TestContadorPintas(unittest.TestCase):

    @patch("src.Juego.cacho.Dado")
    def test_contar_pinta_sin_comodines(self, MockDado):
        # Cacho 1: [trenes, cuadras, trenes, quinas, sextos]
        dados_cacho1 = []
        for valor in ["trenes", "cuadras", "trenes", "quinas", "sextos"]:
            mock_dado = MagicMock()
            mock_dado.obtener_valor.return_value = valor
            dados_cacho1.append(mock_dado)

        # Cacho 2: [trenes, as, tontos, trenes, cuadras]
        dados_cacho2 = []
        for valor in ["trenes", "as", "tontos", "trenes", "cuadras"]:
            mock_dado = MagicMock()
            mock_dado.obtener_valor.return_value = valor
            dados_cacho2.append(mock_dado)

        MockDado.side_effect = dados_cacho1 + dados_cacho2

        cacho1 = Cacho()
        cacho2 = Cacho()
        cachos = [cacho1, cacho2]

        contador = ContadorPintas()

        resultado = contador.contar_pinta("trenes", cachos, usar_comodines=False)

        # Debe contar 4 "trenes" (2 del cacho1 + 2 del cacho2)
        self.assertEqual(resultado, 4)