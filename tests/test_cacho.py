import unittest
from src.Juego.cacho import Cacho

class TestCacho(unittest.TestCase):

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
        self.assertTrue(cacho is not None)
        self.assertIsNone(cacho.ver_dados())

    def test_ver_dados_not_null(self):
        cacho = Cacho()
        cacho.cambiar_visibles()
        self.assertTrue(cacho.ver_dados() is not None)

    def test_agitar(self):
        cacho = Cacho()
        cacho.cambiar_visibles()
        dados = cacho.ver_dados()
        cacho.agitar()
        self.assertNotEqual(dados,cacho.ver_dados())

    def test_perder_dado(self):
        cacho = Cacho()
        cacho.perder_dado()
        self.assertEqual(cacho.ver_cant_dados(), 4)

    def test_recuperar_dado(self):
        cacho = Cacho()
        cacho.perder_dado()
        self.assertEqual(cacho.ver_cant_dados(), 4)

        cacho.recuperar_dado()
        self.assertEqual(cacho.ver_cant_dados(), 5)

    def test_dado_extra(self):
        cacho = Cacho()
        self.assertEqual(cacho.ver_dados_extra(), 0)
        cacho.recuperar_dado()
        self.assertEqual(cacho.ver_cant_dados(), 5)
        self.assertEqual(cacho.ver_dados_extra(), 1)

    def test_perder_dado_con_dado_extra(self):
        cacho = Cacho()
        cacho.recuperar_dado()
        self.assertEqual(cacho.ver_dados_extra(), 1)
        cacho.perder_dado()
        self.assertEqual(cacho.ver_cant_dados(), 5)
        self.assertEqual(cacho.ver_dados_extra(), 0)