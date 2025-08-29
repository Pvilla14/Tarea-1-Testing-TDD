import pytest
from src.Juego.validador_apuesta import ValidadorApuesta

def test_validar_apuesta_inicial_rechaza_ases_con_mas_de_un_dado():
    validador = ValidadorApuesta()
    with pytest.raises(ValueError):
        validador.validar_apuesta_inicial((2, 1), 2)

def test_validar_apuesta_inicial_permite_ases_con_un_dado():
    validador = ValidadorApuesta()
    validador.validar_apuesta_inicial((1, 1), 1)

def test_validar_apuesta_subsiguiente_mayor_cantidad():
    validador = ValidadorApuesta()
    validador.validar_apuesta_subsiguiente((2, 3), (3, 3))

def test_validar_apuesta_subsiguiente_mayor_pinta():
    validador = ValidadorApuesta()
    validador.validar_apuesta_subsiguiente((2, 3), (2, 4))

def test_validar_apuesta_subsiguiente_menor_cantidad_lanza_error():
    validador = ValidadorApuesta()
    with pytest.raises(ValueError):
        validador.validar_apuesta_subsiguiente((2, 3), (1, 3))

def test_validar_apuesta_subsiguiente_menor_pinta_lanza_error():
    validador = ValidadorApuesta()
    with pytest.raises(ValueError):
        validador.validar_apuesta_subsiguiente((2, 4), (2, 3))

def test_cambiar_a_ases_par():
    validador = ValidadorApuesta()
    assert validador.calcular_nueva_cantidad_ases(8) == 5

def test_cambiar_a_ases_impar():
    validador = ValidadorApuesta()
    assert validador.calcular_nueva_cantidad_ases(7) == 4

def test_cambiar_de_ases():
    validador = ValidadorApuesta()
    assert validador.calcular_minimo_cambio_ases(2) == 5

def test_validar_formato_apuesta_correcto():
    validador = ValidadorApuesta()
    validador._validar_formato_apuesta((2, 3))

def test_validar_formato_apuesta_incorrecto():
    validador = ValidadorApuesta()
    with pytest.raises(ValueError):
        validador._validar_formato_apuesta((2, 7))

def test_validar_apuesta_subsiguiente_cambiar_a_ases():
    validador = ValidadorApuesta()
    validador.validar_apuesta_subsiguiente((8, 3), (5, 1)) 

def test_validar_apuesta_subsiguiente_cambiar_de_ases():
    validador = ValidadorApuesta()
    validador.validar_apuesta_subsiguiente((2, 1), (5, 3))  

def test_validar_apuesta_subsiguiente_cambiar_a_ases_invalido():
    validador = ValidadorApuesta()
    with pytest.raises(ValueError):
        validador.validar_apuesta_subsiguiente((2, 3), (1, 1))

def test_validar_apuesta_subsiguiente_cambiar_de_ases_invalido():
    validador = ValidadorApuesta()
    with pytest.raises(ValueError):
        validador.validar_apuesta_subsiguiente((2, 1), (1, 3))

def test_validar_apuesta_subsiguiente_igual_cantidad_igual_pinta_lanza_error():
    validador = ValidadorApuesta()
    with pytest.raises(ValueError):
        validador.validar_apuesta_subsiguiente((2, 3), (2, 3))

def test_es_pinta_mayor_false():
    validador = ValidadorApuesta()
    assert not validador._es_pinta_mayor(3, 4)