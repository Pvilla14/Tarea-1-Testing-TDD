# Kata TDD: Simulador del Juego Dudo Chileno

## Estudiantes
- Pablo Villagrán Hermanns (2023439231)
- Daniel Ignacio Aburto Rivera (2023433900)
- Jorge Slimming Lagos (2023409901)

## Descripción del Proyecto
Este proyecto implementa un simulador del juego tradicional chileno "Dudo" utilizando metodología TDD (Test-Driven Development). El juego se basa en las reglas oficiales disponibles en [Don Pichuncho](https://www.donpichuncho.cl/aprende-a-jugar-dudo-en-cacho).

## Estructura del Proyecto
```
Tarea-1-Testing-TDD/
├── src/                    # Código fuente principal
│   ├── dado.py            # Clase Dado
│   ├── cacho.py           # Clase Cacho (conjunto de 5 dados)
│   ├── validador_apuesta.py # Validación de apuestas
│   ├── contador_pintas.py  # Conteo de pintas en el juego
│   ├── arbitro_ronda.py   # Lógica de arbitraje de rondas
│   └── gestor_partida.py  # Gestión completa de la partida
├── tests/                 # Pruebas unitarias
│   ├── test_dado.py
│   ├── test_cacho.py
│   ├── test_validador_apuesta.py
│   ├── test_contador_pintas.py
│   ├── test_arbitro_ronda.py
│   └── test_gestor_partida.py
├── .github/workflows/     # GitHub Actions para CI/CD
├── requirements.txt       # Dependencias del proyecto
└── README.md             # Este archivo
```

## Requisitos del Sistema
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

### 1. Clonar el Repositorio
```bash
git clone https://github.com/usuario/Tarea-1-Testing-TDD.git
cd Tarea-1-Testing-TDD
```

### 2. Crear Entorno Virtual (Recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

## Ejecución

### Ejecutar las Pruebas
```bash
# Ejecutar todas las pruebas
pytest

# Ejecutar pruebas con reporte de cobertura
pytest --cov=src --cov-report=html

# Ejecutar pruebas en modo verbose
pytest -v
```

### Usar el Simulador
```python
from src.Juego.gestor_partida import GestorPartida

# Crear una partida con 3 jugadores
gestor = GestorPartida()

# Iniciar el juego
gestor.ronda_inicial()

# El juego se ejecuta automáticamente con las reglas implementadas
```

## Funcionalidades Implementadas

### 🎲 Sistema de Dados
- **Dado**: Genera valores del 1-6 
- **Cacho**: Maneja un conjunto de 5 dados los cuales se pueden agitar y ocultar

### 🎯 Validación de Apuestas
- Verifica apuestas válidas (cantidad mayor o pinta superior)
- Maneja reglas especiales de los Ases como comodines
- Valida restricciones de apuestas iniciales

### 📊 Conteo de Pintas
- Cuenta apariciones de pintas específicas
- Maneja Ases como comodines automáticamente
- Soporte para rondas cuando el jugador tiene solamente un dado

### ⚖️ Arbitraje
- Determina quién gana cuando se "duda" o "calza"
- Maneja pérdida/obtención de dados

### 🎮 Gestión de Partida
- Administra múltiples jugadores
- Control de turnos y rondas
- Detección automática de condiciones especiales

## Metodología TDD Aplicada

El proyecto sigue estrictamente la metodología TDD con el patrón **RED-GREEN-REFACTOR**:

1. **🔴 RED**: Escribir test que falle
2. **🟢 GREEN**: Implementación mínima para pasar el test
3. **🔵 REFACTOR**: Mejorar el código manteniendo funcionalidad

Cada funcionalidad tiene commits específicos siguiendo este patrón.

## Integración Continua

El proyecto incluye GitHub Actions que:
- Ejecuta automáticamente todas las pruebas
- Se ejecuta en cada push y pull request

## Cobertura de Pruebas
El proyecto mantiene una cobertura superior al 90% en todas las clases principales:

```bash
# Generar reporte de cobertura
pytest --cov=src --cov-report=term-missing
```

## Contribuir al Proyecto

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Sigue la metodología TDD para cualquier cambio
4. Asegúrate de que todas las pruebas pasen
5. Crea un Pull Request

## Tecnologías Utilizadas
- **Python 3.8+**: Lenguaje principal
- **pytest**: Framework de testing
- **pytest-mock**: Mocking para pruebas
- **pytest-cov**: Cobertura de código
- **GitHub Actions**: CI/CD

## Licencia
Este proyecto es parte de un trabajo académico para el curso de Testing y TDD.

---
**Nota**: Para cualquier duda sobre el juego Dudo, consultar las [reglas oficiales](https://www.donpichuncho.cl/aprende-a-jugar-dudo-en-cacho).



