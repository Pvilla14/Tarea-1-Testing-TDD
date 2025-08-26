import pytest
from src.servicios.generador_aleatorio import GeneradorAleatorio

def test_generar_devuelve_numero_en_rango():
    # Arrange
    generador = GeneradorAleatorio()
    min_val = 1
    max_val = 6
    
    # Act
    resultado = generador.generar(min_val, max_val)
    
    # Assert
    assert min_val <= resultado <= max_val

def test_generar_con_min_mayor_que_max_lanza_error():
    # Arrange
    generador = GeneradorAleatorio()
    
    # Act & Assert
    with pytest.raises(ValueError):
        generador.generar(6, 1)