import unittest
from unittest.mock import patch
from src.Juego.dado import Dado

class TestDado(unittest.TestCase):

    def test_crear(self):
        dado = Dado()
        assert dado is not None

    @patch("src.Juego.dado.GeneradorAleatorio")
    def test_ver_valor(self, GeneradorMock):
        mock = GeneradorMock.return_value
        mock.generar.return_value = 4

        dado = Dado()

        assert dado.obtener_valor() == "cuadras"

        mock.generar.assert_called_once_with(1,6)

    @patch("src.Juego.dado.GeneradorAleatorio")
    def test_cambiar_valor(self, GeneradorMock):
        dado = Dado()

        mock = GeneradorMock.return_value
        mock.generar.return_value = 5

        dado.cambiar_valor()

        assert dado.obtener_valor() == "quinas"

