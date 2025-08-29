import pytest
from src.Juego.arbitro_ronda import ArbitroRonda

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