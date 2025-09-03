import unittest
from unittest.mock import patch, MagicMock
import io

import src.Juego.cacho
from src.Juego.gestor_partida import GestorPartida
from src.Juego.cacho import Cacho

class TestGestorPartida(unittest.TestCase):

    @patch("builtins.input", side_effect=["2"])
    def test_jugador_anterior_derecha(self, mock_input):
        gestor = GestorPartida()
        gestor.direccion = 'Derecha'
        self.assertEqual(gestor.jugador_anterior(0), 1)
        self.assertEqual(gestor.jugador_anterior(1), 0)

    @patch("builtins.input", side_effect=["3"])
    def test_jugador_siguiente_derecha(self, mock_input):
        gestor = GestorPartida()
        gestor.direccion = 'Derecha'
        self.assertEqual(gestor.jugador_siguiente(0), 1)
        self.assertEqual(gestor.jugador_siguiente(1), 2)

    @patch("builtins.input", side_effect=["2"])
    def test_jugador_anterior_izquierda(self, mock_input):
        gestor = GestorPartida()
        gestor.direccion = 'Izquierda'
        self.assertEqual(gestor.jugador_anterior(0), 1)
        self.assertEqual(gestor.jugador_anterior(1), 0)

    @patch("builtins.input", side_effect=["3"])
    def test_jugador_siguiente_izquierda(self, mock_input):
        gestor = GestorPartida()
        gestor.direccion = 'Izquierda'
        self.assertEqual(gestor.jugador_siguiente(0), 2)
        self.assertEqual(gestor.jugador_siguiente(1), 0)

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


    @patch("builtins.input", side_effect=["2"])
    def test_persona_calza_acertada(self, mock_input):
        """Test para cuando una persona pierde un dado y luego calza, y recupera un dado"""
        gestor = GestorPartida()

        # Mock de dependencias
        gestor.cambiar_estado_dados_otros_jugadores = MagicMock()
        gestor.contar_pintas.contar_pinta = MagicMock(return_value=3)
        gestor.arbitro.resolver_calce = MagicMock(return_value='Apostador gana')
        gestor.ronda_inicial = MagicMock()

        # Setup
        gestor.apuesta_anterior = (3, 4)
        gestor.obligo = False
        gestor.jugadores[0].perder_dado()
        dados_antes = gestor.jugadores[0].ver_cant_dados()

        # Act
        gestor.persona_calza(0)

        # Assert
        dados_despues = gestor.jugadores[0].ver_cant_dados()
        assert dados_despues == dados_antes + 1  # Recuperó un dado
        gestor.ronda_inicial.assert_called_once_with(0)


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

    @patch("builtins.input", side_effect=["2"])
    def test_jugador_anterior(self, mock_input):
        gestor = GestorPartida()
        gestor.direccion = 'Derecha'
        self.assertEqual(gestor.jugador_anterior(0), 1)
        self.assertEqual(gestor.jugador_anterior(1), 0)

    @patch("builtins.input", side_effect=["3"])
    def test_jugador_siguiente(self, mock_input):
        gestor = GestorPartida()
        gestor.direccion = 'Derecha'
        self.assertEqual(gestor.jugador_siguiente(0), 1)
        self.assertEqual(gestor.jugador_siguiente(1), 2)

    @patch('builtins.input', side_effect=['2'])
    def test_jugadores_restantes(self, mock_input):
        gestor = GestorPartida()
        self.assertEqual(gestor.jugadores_restantes(), 2)
        gestor.jugadores.pop()
        self.assertEqual(gestor.jugadores_restantes(), 1)

    @patch('builtins.input', side_effect=['2'])
    def test_cambiar_estado_dados_otros_jugadores(self, mock_input):
        gestor = GestorPartida()
        jugador1 = MagicMock(spec=Cacho)
        jugador2 = MagicMock(spec=Cacho)
        gestor.jugadores = [jugador1, jugador2]
        gestor.cambiar_estado_dados_otros_jugadores(jugador1)
        jugador2.cambiar_visibles.assert_called_once()
        jugador1.cambiar_visibles.assert_not_called()

    @patch('builtins.input', side_effect=['2'])
    def test_quitar_dado_jugador(self, mock_input):
        gestor = GestorPartida()
        jugador = MagicMock(spec=Cacho)
        gestor.jugadores = [jugador]
        gestor.quitar_dado_jugador(0)
        jugador.perder_dado.assert_called_once()

    @patch('builtins.input', side_effect=['2'])
    def test_cant_dados_en_juego(self, mock_input):
        gestor = GestorPartida()
        jugador1 = MagicMock(spec=Cacho)
        jugador1.ver_cant_dados.return_value = 3
        jugador2 = MagicMock(spec=Cacho)
        jugador2.ver_cant_dados.return_value = 2
        gestor.jugadores = [jugador1, jugador2]
        self.assertEqual(gestor.cant_dados_en_juego(), 5)

    @patch('builtins.input', side_effect=['2'])
    def test_verificar_obliga(self, mock_input):
        gestor = GestorPartida()
        jugador1 = MagicMock(spec=Cacho)
        jugador1.ver_cant_dados.return_value = 1
        jugador2 = MagicMock(spec=Cacho)
        jugador2.ver_cant_dados.return_value = 2
        gestor.jugadores = [jugador1, jugador2]
        gestor.jugadores_obliga = [False, False]
        self.assertTrue(gestor.verificar_obliga(0))
        self.assertFalse(gestor.verificar_obliga(0))  # segunda vez no obliga
        self.assertFalse(gestor.verificar_obliga(1))

    @patch('builtins.input', side_effect=['2'])
    def test_ver_dados_contrincantes(self, mock_input):
        gestor = GestorPartida()
        jugador1 = MagicMock(spec=Cacho)
        jugador2 = MagicMock(spec=Cacho)
        jugador1.ver_dados.return_value = [1, 2, 3]
        jugador2.ver_dados.return_value = [4, 5]
        gestor.jugadores = [jugador1, jugador2]
        gestor.ver_dados_contrincantes(jugador1)
        jugador2.cambiar_visibles.assert_any_call()
        jugador2.ver_dados.assert_called_once()
        jugador1.ver_dados.assert_not_called()

    @patch('builtins.input', side_effect=['2'])
    def test_limitar_dados(self, mock_input):
        gestor = GestorPartida()
        jugador1 = MagicMock(spec=Cacho)
        jugador2 = MagicMock(spec=Cacho)
        gestor.jugadores = [jugador1, jugador2]
        gestor.limitar_dados(1)
        self.assertEqual(jugador1.perder_dado.call_count, 4)
        self.assertEqual(jugador2.perder_dado.call_count, 4)

