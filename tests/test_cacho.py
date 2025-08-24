import pytest
from src.Juego.cacho import Cacho

class TestCacho:

    def test_crear(self):
        cacho = Cacho()
        assert cacho is not None
        assert cacho.cant_dados() == 5

    def test_ver_dados_null(self):
        cacho = Cacho()
        assert cacho.ver_dados() == None

    def test_agitar(self):
        cacho = Cacho()
        cacho.agitar()
