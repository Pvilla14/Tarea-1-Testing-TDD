import unittest
from unittest.mock import patch, MagicMock
import io

import src.Juego.cacho
from src.Juego.gestor_partida import GestorPartida
from src.Juego.cacho import Cacho

class TestGestorPartida(unittest.TestCase):

    @patch("builtins.input", side_effect=["5"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_crear(self, mock_stdout, mock_input):
        gestor = GestorPartida()

        self.assertIsInstance(gestor, GestorPartida)

        salida = mock_stdout.getvalue().strip()
        self.assertEqual(salida, "Bienvenido a una nueva partida de cachos. Indique la cantidad de jugadores:")

    @patch("builtins.input", side_effect= "5")
    def test_cant_jugadores(self, mock_input):

        gestor = GestorPartida()
        self.assertEqual(gestor.jugadores_restantes(), 5)
        self.assertEqual(mock_input.call_count, 1)
        self.assertEqual(gestor.dados_iniciales, 25)

    @patch("builtins.input", side_effect=["2", "1", "2", "Tontos"])
    def test_apuesta_inicial(self, mock_input):
        gestor = GestorPartida()

        gestor.rondas_siguientes = MagicMock()
        gestor.ronda_inicial()

        self.assertEqual(gestor.direccion, "Derecha")
        self.assertEqual(gestor.apuesta_actual, (2,2) )
        self.assertEqual(gestor.apuesta_anterior, gestor.apuesta_actual)
        gestor.rondas_siguientes.assert_called_once_with(0)
        self.assertEqual(mock_input.call_count, 4)

    @patch("src.Juego.dado.GeneradorAleatorio.generar", side_effect=[1, 2, 3, 4, 5] * 2)
    @patch("src.Juego.cacho.Cacho.agitar", side_effect=[1, 2]*10)
    @patch("builtins.input", side_effect=["2","1","2","Tontos","2","1","3","3","Tontos","1","1","5","Tontos","2"])#cant_j,dir,apuesta,dudar(falla),dir,apuesta,apuesta,duda(acierta),gana
    def test_gestor_juego(self, mock_input, mock_generar, mock_agitar):
        gestor = GestorPartida()
        for jugador in gestor.jugadores:
            valores = [dado.valor for dado in jugador.dados]
            self.assertEqual(valores, [1,2,3,4,5])

        #para metodos de practicidad limitaremos los dados a 2 por jugador por el test
        gestor.limitar_dados(2)
        for jugador in gestor.jugadores:
            valores = [dado.valor for dado in jugador.dados]
            self.assertEqual(valores, [1,2])
        #ambos jugadores tienen los valores [1,2] en sus dados

        with self.assertRaises(SystemExit):
            gestor.ronda_inicial()
            '''al iniciar el test se van introduciendo valores gracias a 
            mock_input, los cuales naturalmente se introducirian por terminal,
            con esto, la partida se desarrolla sola, y cuando uno de los jugadores
            pierde se termina de manera automatica.
            Las entradas de mock_input las verificamos para que pudieran generar un 
            flujo sencillo y directo a la victoria, y acortamos la cantidad de dados para
            no extender tanto el test
            '''








