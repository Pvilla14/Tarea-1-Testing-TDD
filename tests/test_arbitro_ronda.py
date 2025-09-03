import pytest
from src.Juego.arbitro_ronda import ArbitroRonda
from src.Juego.cacho import Cacho
from unittest.mock import patch, MagicMock


def test_resolver_duda_pierde_apostador():
    arbitro = ArbitroRonda()
    apuesta = (3, 4) # (cantidad, pinta)
    conteo_real = 2
    resultado = arbitro.resolver_duda(apuesta, conteo_real)
    assert resultado == 'Apostador pierde'

def test_resolver_duda_pierde_dudador():
    arbitro = ArbitroRonda()
    apuesta = (3, 4) # (cantidad, pinta)
    conteo_real = 3
    resultado = arbitro.resolver_duda(apuesta, conteo_real)
    assert resultado == 'Dudador pierde'

def test_resolver_calce_gana_apostador():
    arbitro = ArbitroRonda()
    apuesta = (2, 5)
    conteo_real = 2
    resultado = arbitro.resolver_calce(apuesta, conteo_real)
    assert resultado == 'Apostador gana'

def test_resolver_calce_pierde_apostador():
    arbitro = ArbitroRonda()
    apuesta = (2, 5)
    conteo_real = 3
    resultado = arbitro.resolver_calce(apuesta, conteo_real)
    assert resultado == 'Apostador pierde'


def test_validar_calce_mitad_de_dados():
    # Simular partida con 3 jugadores
    arbitro = ArbitroRonda()
    cacho1 = Cacho()
    cacho2 = Cacho()
    cacho3 = Cacho()

    cacho1.perder_dado()
    cacho1.perder_dado()
    cacho2.perder_dado()
    cacho3.perder_dado()
    cacho3.perder_dado()

    # Total en mesa: 3 + 4 + 3 = 10 dados
    # El jugador que quiere calzar (cacho1) tiene 3 dados
    dados_juego = cacho1.ver_cant_dados() + cacho2.ver_cant_dados() + cacho3.ver_cant_dados()
    dados_calzador = cacho1.ver_cant_dados()
    dados_totales = 15  

    # 10 dados restantes >= mitad de 15 (8)
    assert arbitro.validar_calce(dados_juego, dados_calzador, dados_totales) == True


def test_validar_calce_un_dado():
    arbitro = ArbitroRonda()
    cacho1 = Cacho()
    cacho2 = Cacho()

    # cacho1 pierde hasta quedar con 1 dado
    for i in range(4):
        cacho1.perder_dado()

    dados_juego = cacho1.ver_cant_dados() + cacho2.ver_cant_dados()
    dados_calzador = cacho1.ver_cant_dados()
    dados_totales = 10

    # Jugador con 1 dado siempre puede calzar
    assert arbitro.validar_calce(dados_juego, dados_calzador, dados_totales) == True


def test_validar_calce_no_permitido_con_cachos():
    arbitro = ArbitroRonda()
    cacho1 = Cacho()
    cacho2 = Cacho()

    for _ in range(3):  # cacho1 queda con 2 dados
        cacho1.perder_dado()
    for _ in range(3):  # cacho2 queda con 2 dados
        cacho2.perder_dado()

    dados_juego = cacho1.ver_cant_dados() + cacho2.ver_cant_dados()
    dados_calzador = cacho1.ver_cant_dados()
    dados_totales = 10

    # mitad de dados restantes y jugador no tiene 1 solo dado
    assert arbitro.validar_calce(dados_juego, dados_calzador, dados_totales) == False


def test_contar_pintas_reales_sin_comodines():
    """Test que ArbitroRonda pueda contar pintas reales usando ContadorPintas"""
    arbitro = ArbitroRonda()
    
    # Mock de cachos con dados específicos
    mock_cacho1 = MagicMock()
    mock_cacho2 = MagicMock()
    cachos = [mock_cacho1, mock_cacho2]
    
    with patch('src.Juego.arbitro_ronda.ContadorPintas') as MockContador:
        mock_contador = MockContador.return_value
        mock_contador.contar_pinta.return_value = 3
        
        resultado = arbitro.contar_pintas_reales(cachos, "trenes", False)
        
        assert resultado == 3
        MockContador.assert_called_once()
        mock_contador.contar_pinta.assert_called_once_with("trenes", cachos, False)


def test_resolver_duda_completa_con_cachos():
    """Test que resuelve duda contando automáticamente las pintas en cachos"""
    arbitro = ArbitroRonda()
    apuesta = (2, "trenes")
    
    mock_cacho1 = MagicMock()
    mock_cacho2 = MagicMock()
    cachos = [mock_cacho1, mock_cacho2]
    
    with patch.object(arbitro, 'contar_pintas_reales', return_value=1):
        resultado = arbitro.resolver_duda_completa(apuesta, cachos)
        
        assert resultado == 'Apostador pierde'  # Solo hay 1, apostó 2
        arbitro.contar_pintas_reales.assert_called_once_with(cachos, "trenes", True)


def test_resolver_calce_completo_con_cachos():
    """Test que resuelve calce contando automáticamente las pintas en cachos"""
    arbitro = ArbitroRonda()
    apuesta = (3, "cuadras")
    
    mock_cacho1 = MagicMock()
    mock_cacho2 = MagicMock()
    cachos = [mock_cacho1, mock_cacho2]
    
    with patch.object(arbitro, 'contar_pintas_reales', return_value=3):
        resultado = arbitro.resolver_calce_completo(apuesta, cachos)
        
        assert resultado == 'Apostador gana'  # Exactamente 3
        arbitro.contar_pintas_reales.assert_called_once_with(cachos, "cuadras", True)