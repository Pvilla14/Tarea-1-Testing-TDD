import random
from abc import ABC, abstractmethod

class GeneradorAleatorioBase(ABC):
    """Interfaz base para generadores aleatorios"""
    
    @abstractmethod
    def generar(self, min: int, max: int) -> int:
        """Genera un número aleatorio entre min y max (inclusive)"""
        pass

class GeneradorAleatorio(GeneradorAleatorioBase):
    """Implementación concreta de generador aleatorio usando random"""
    
    def generar(self, min: int, max: int) -> int:
        """
        Genera un número entero aleatorio entre min y max (inclusive)
        
        Args:
            min: Valor mínimo (inclusive)
            max: Valor máximo (inclusive)
            
        Returns:
            Número aleatorio entre min y max
            
        Raises:
            ValueError: Si min es mayor que max
        """
        if min > max:
            raise ValueError("min no puede ser mayor que max")
        return random.randint(min, max)