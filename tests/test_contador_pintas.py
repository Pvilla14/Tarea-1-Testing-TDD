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

    @patch("src.Juego.cacho.Dado")
    def test_contar_pinta_con_comodines(self, MockDado):
        # Cacho 1: [trenes, as, trenes, quinas, sextos]
        dados_cacho1 = []
        for valor in ["trenes", "as", "trenes", "quinas", "sextos"]:
            mock_dado = MagicMock()
            mock_dado.obtener_valor.return_value = valor
            dados_cacho1.append(mock_dado)

        # Cacho 2: [cuadras, as, tontos, trenes, as]
        dados_cacho2 = []
        for valor in ["cuadras", "as", "tontos", "trenes", "as"]:
            mock_dado = MagicMock()
            mock_dado.obtener_valor.return_value = valor
            dados_cacho2.append(mock_dado)

        MockDado.side_effect = dados_cacho1 + dados_cacho2

        cacho1 = Cacho()
        cacho2 = Cacho()
        cachos = [cacho1, cacho2]

        contador = ContadorPintas()

        resultado = contador.contar_pinta("trenes", cachos)

        # Debe contar 6 "trenes" total:
        # - 2 "trenes" del cacho1 + 1 "as" comodín = 3
        # - 1 "trenes" del cacho2 + 2 "as" comodines = 3
        # Total = 6
        self.assertEqual(resultado, 6)

    def test_validar_pinta_existente_valida(self):
        contador = ContadorPintas()
        cachos = []

        try:
            for pinta_valida in ["as", "tontos", "trenes", "cuadras", "quinas", "sextos"]:
                contador.contar_pinta(pinta_valida, cachos)
        except ValueError:
            self.fail("No debería dar error con pintas válidas")

    def test_validar_pinta_existente_invalida(self):
        contador = ContadorPintas()
        cachos = []

        # Pintas inválidas deberían lanzar ValueError
        with self.assertRaises(ValueError) as context:
            contador.contar_pinta("pinta_inexistente", cachos)

        self.assertIn("Pinta inválida", str(context.exception))

        with self.assertRaises(ValueError) as context:
            contador.contar_pinta("", cachos)

        self.assertIn("Pinta inválida", str(context.exception))