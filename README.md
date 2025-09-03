# Kata TDD: Simulador del Juego Dudo Chileno

## Estudiantes:

- Pablo Villagrán Hermanns (2023439231)
-
-

## Contexto
El Dudo es un juego tradicional chileno que se juega con dados en "cachos". Nosotros implementamos una versión de juego en la cual manejamos distintas clases para lograr ejecutar el juego para distintas personas y que sean capaces de realizar las distintas acciones indicadas en la siguiente página: https://www.donpichuncho.cl/aprende-a-jugar-dudo-en-cacho

## Objetivos
- Aplicar TDD con Python3 y pytest y pytest-mock
- Usar mocking cuando sea apropiado
- Diseñar clases con responsabilidades claras
- Manejar lógica de juego compleja paso a paso
- Introducción a CI con GitHub Actions 

## Requerimientos Funcionales

### Sistema de Dados y Pintas
Implementa una clase `Dado` que:
- Genere valores del 1 al 6
- Use las denominaciones tradicionales:
  - 1: "As", 2: "Tonto", 3: "Tren", 4: "Cuadra", 5: "Quina", 6: "Sexto"

Implementa una clase `Cacho` que:
- Contenga 5 dados
- Permita "agitar" (regenerar valores)
- Oculte/muestre los dados según el estado del juego

### Validador de Apuestas
Implementa una clase `ValidadorApuesta` que verifique:
- Si una nueva apuesta es válida (mayor cantidad o pinta superior)
- Las reglas especiales de los Ases:
  - Al cambiar A ases: dividir cantidad actual por 2 (par: +1, impar: redondear arriba)
  - Al cambiar DE ases: multiplicar por 2 y sumar 1
- Que no se pueda partir con Ases (excepto con un dado)

### Contador de Pintas
Implementa una clase `ContadorPintas` que:
- Cuente apariciones de una pinta específica en todos los dados
- Trate los Ases como comodines (suman a cualquier pinta apostada)
- Maneje el caso especial cuando los Ases NO son comodines (ronda de un dado)

### Árbitro del Juego
Implementa una clase `ArbitroRonda` que:
- Determine el resultado cuando un jugador "duda"
- Maneje la lógica de "calzar" (debe ser exacto)
- Decida quién pierde/gana un dado
- Valide las condiciones para "calzar" (mitad de dados en juego O jugador con un dado)

### Gestor de Partida
Implementa una clase `GestorPartida` que:
- Administre múltiples jugadores y sus dados
- Determine quién inicia cada ronda
- Maneje el flujo de turnos
- Detecte cuándo alguien queda con un dado (para activar reglas especiales)

## Aspectos Técnicos

Para la implementación usamos la metodología TDD, con el fin de asegurarnos que al nuestras clases cumplieran con los requerimientos indicados por las reglas del juego, para ello nos dividimos el trabajo y cada uno implementó ciertas clases y se preocupo de cumplir por lo parámetros indicados.

Junto con esto trabajamos usando GitHub Actions, el cual nos permitía saber cunado nuestros test estaban siendo correctamente validados, y cuando ocurría algun error leve lo pudiesemos corregir.

### Mocking 
Dentro del proyecto utilizamos mokin para testear en un ambiente controlado el juego, llegando a tener test con moking en casi todas nuestras clases, dado que la aleatoriedad que nos proporcionaba el generador aleatorio de los dados no siempre era combeniente, por lo que en algunas ocaciones era preferible trabajar con valores generados intencionalmente.



## Metodología TDD - Commits Obligatorios


### Patrón de Commits Requerido
Para cada funcionalidad, deben hacer **exactamente 3 commits** en este orden:

1. **🔴 ROJO**: `git commit -m "RED: test para [funcionalidad] - falla como esperado"`
   - Solo el test, sin implementación
   - El test debe fallar por la razón correcta
   - Ejecutar `pytest` debe mostrar el fallo

2. **🟢 VERDE**: `git commit -m "GREEN: implementación mínima para [funcionalidad]"`
   - Código mínimo para hacer pasar el test
   - Ejecutar `pytest` debe mostrar todos los tests pasando
   - No importa si el código es "feo" en esta etapa

3. **🔵 REFACTOR**: `git commit -m "REFACTOR: mejora código de [funcionalidad]"`
   - Mejorar la implementación sin cambiar funcionalidad
   - Todos los tests siguen pasando
   - Solo si hay algo que refactorizar (sino omitir este commit)

    

## Entregables
1. Código fuente con cobertura de pruebas > 90%
2. Todas las pruebas deben pasar
3. Implementación que siga principios SOLID
4. Historial de commits en el formato descrito
5. README con instrucciones de ejecución
6. Una GitHub Action que ejecute sus tests (¡Verde por el último commit!)



