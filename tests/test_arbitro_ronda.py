import pytest
from src.Juego.arbitro_ronda import ArbitroRonda
from src.Juego.cacho import Cacho


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