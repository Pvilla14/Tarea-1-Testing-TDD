import pytest
from src.Juego.cacho import Cacho

class TestCacho:

    def test_crear(self):
        cacho = Cacho()
        assert cacho is not None
        assert cacho.ver_cant_dados() == 5

    def test_visibles_cambio(self):
        cacho = Cacho()
        estado_previo = cacho.visibles
        cacho.cambiar_visibles()
        assert cacho.visibles != estado_previo

    def test_ver_dados_null(self):
        cacho = Cacho()
        assert cacho.ver_dados() == None

    def test_ver_dados_not_null(self):
        cacho = Cacho()
        cacho.cambiar_visibles()
        assert cacho.ver_dados() is not None

    def test_agitar(self):
        cacho = Cacho()
        cacho.cambiar_visibles()
        dados = cacho.ver_dados()
        cacho.agitar()
        assert dados != cacho.ver_dados()

    def test_perder_dado(self):
        cacho = Cacho()
        cacho.perder_dado()
        assert cacho.ver_dados() == 4
