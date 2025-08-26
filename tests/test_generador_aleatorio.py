import pytest
from src.servicios.generador_aleatorio import GeneradorAleatorio, GeneradorAleatorioBase

class TestGeneradorAleatorio:
    def test_generar_devuelve_numero_en_rango(self):
        # Arrange
        generador = GeneradorAleatorio()
        min_val = 1
        max_val = 6
        
        # Act
        resultado = generador.generar(min_val, max_val)
        
        # Assert
        assert min_val <= resultado <= max_val
    
    def test_generar_con_min_mayor_que_max_lanza_error(self):
        # Arrange
        generador = GeneradorAleatorio()
        
        # Act & Assert
        with pytest.raises(ValueError):
            generador.generar(6, 1)
    
    def test_generar_es_interface_abstracta(self):
        # Arrange
        class GeneradorMock(GeneradorAleatorioBase):
            def generar(self, min, max):
                return 5  # Valor fijo para testing
        
        # Act
        generador = GeneradorMock()
        resultado = generador.generar(1, 6)
        
        # Assert
        assert resultado == 5