import pytest
from src.Juego.validador_apuesta import ValidadorApuesta

def test_validar_apuesta_inicial_rechaza_ases_con_mas_de_un_dado():
    # Arrange
    validador = ValidadorApuesta()
    
    # Act & Assert
    with pytest.raises(ValueError):
        validador.validar_apuesta_inicial((2, 1), 2)  # 2 ases con 2 dados

def test_validar_apuesta_inicial_permite_ases_con_un_dado():
    # Arrange
    validador = ValidadorApuesta()
    
    # Act & Assert
    # No debe lanzar excepción
    validador.validar_apuesta_inicial((1, 1), 1)  # 1 as con 1 dado

def test_validar_apuesta_subsiguiente_mayor_cantidad():
    # Arrange
    validador = ValidadorApuesta()
    
    # Act & Assert
    # No debe lanzar excepción
    validador.validar_apuesta_subsiguiente((2, 3), (3, 3))  # 3 trenes vs 2 trenes

def test_validar_apuesta_subsiguiente_mayor_pinta():
    # Arrange
    validador = ValidadorApuesta()
    
    # Act & Assert
    # No debe lanzar excepción
    validador.validar_apuesta_subsiguiente((2, 3), (2, 4))  # 2 cuadras vs 2 trenes

def test_validar_apuesta_subsiguiente_menor_cantidad_lanza_error():
    # Arrange
    validador = ValidadorApuesta()
    
    # Act & Assert
    with pytest.raises(ValueError):
        validador.validar_apuesta_subsiguiente((2, 3), (1, 3))  # 1 tren vs 2 trenes

def test_validar_apuesta_subsiguiente_menor_pinta_lanza_error():
    # Arrange
    validador = ValidadorApuesta()
    
    # Act & Assert
    with pytest.raises(ValueError):
        validador.validar_apuesta_subsiguiente((2, 4), (2, 3))  # 2 trenes vs 2 cuadras