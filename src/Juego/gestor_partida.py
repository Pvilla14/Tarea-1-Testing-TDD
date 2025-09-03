from src.Juego.contador_pintas import ContadorPintas
from src.Juego.validador_apuesta import ValidadorApuesta
from src.Juego.cacho import Cacho
from src.Juego.arbitro_ronda import ArbitroRonda
import sys

class GestorPartida:

    valores_pintas = { "as": 1, "tontos": 2,
                        "trenes": 3, "cuadras": 4,
                        "quinas": 5, "sextas": 6
                    }
    valores_numeros = { 1: "as", 2: "tontos",
                        3: "trenes", 4: "cuadras",
                        5: "quinas", 6: "sextas"
                    }
    jugadores : list[Cacho]
    jugadores_obliga : list[bool]
    apuesta_actual : tuple[int, int]
    apuesta_anterior : tuple[int, int]
    direccion : str
    dados_iniciales : int
    validador : ValidadorApuesta
    contar_pintas : ContadorPintas
    arbitro : ArbitroRonda
    obligo : bool
    metodo_obliga : str

    def __init__(self):
        print("Bienvenido a una nueva partida de cachos. Indique la cantidad de jugadores: ")
        cant_jugadores = int(input())
        self.dados_iniciales = cant_jugadores * 5
        self.jugadores = [Cacho() for _ in range (cant_jugadores)]
        self.jugadores_obliga = [False for _ in range (cant_jugadores)]
        self.validador = ValidadorApuesta()
        self.obligo = False
        self.contar_pintas = ContadorPintas()
        self.arbitro = ArbitroRonda()

    def ronda_inicial(self, jugador_inicial : int = 0):

        for j in self.jugadores:
            j.agitar()

        if len(self.jugadores) == 1:
            self.fin_partida(jugador_inicial)

        self.obligo = self.verificar_obliga(jugador_inicial)


        print("Indique a que direccion quiere jugar: ")
        print("1)Derecha")
        print("2)Izquierda")
        direccion = int(input())

        while direccion != 1 and direccion != 2:
            print("Direccion invalida. Ingrese direccion nuevamente")
            direccion = int(input())

        if direccion == 1:
            self.direccion = 'Derecha'
        elif direccion == 2:
            self.direccion = 'Izquierda'

        while True:
            try:
                print("Ingrese su apuesta inicial: ")

                if not self.obligo:
                    print("Sus dados son:")
                    self.jugadores[jugador_inicial].cambiar_visibles()
                    print(self.jugadores[jugador_inicial].ver_dados())
                    self.jugadores[jugador_inicial].cambiar_visibles()

                else:
                    self.metodo_obliga = str.lower(input("Indique abierto o cerrado para metodo de obliga"))

                    if self.metodo_obliga == 'abierto':
                        print("Los dados de los contrincantes son: ")
                        self.ver_dados_contrincantes(jugador_inicial)

                    else:
                        print("Sus dados son:")
                        self.jugadores[jugador_inicial].cambiar_visibles()
                        print(self.jugadores[jugador_inicial].ver_dados())
                        self.jugadores[jugador_inicial].cambiar_visibles()

                print("Ingrese cantidad: ")
                apuesta_cant = int(input())
                print("Ingrese pinta: ")
                apuesta_pinta = str.lower(input())
                apuesta_inicial = (apuesta_cant, self.valores_pintas[apuesta_pinta])
                print(f"La apuesta es {apuesta_inicial}")
                self.validador.validar_apuesta_inicial(apuesta_inicial, self.jugadores[jugador_inicial].cant_dados)
                self.apuesta_actual = (apuesta_cant, self.valores_pintas[apuesta_pinta])
                break

            except ValueError as e:
                print(f"Apuesta inválida: {e}. Intente de nuevo.\n")

        self.apuesta_anterior = self.apuesta_actual
        self.rondas_siguientes(jugador_inicial)

    def rondas_siguientes(self, jugador_inicial : int = 0):

        jugador = self.jugador_siguiente(jugador_inicial)

        if not self.obligo:
            print("Sus dados son:")
            self.jugadores[jugador_inicial].cambiar_visibles()
            print(self.jugadores[jugador_inicial].ver_dados())
            self.jugadores[jugador_inicial].cambiar_visibles()

        else:
            self.metodo_obliga = str.lower(input("Indique abierto o cerrado para metodo de obliga"))

            if self.metodo_obliga == 'abierto':
                print("Los dados de los contrincantes son: ")
                self.ver_dados_contrincantes(jugador_inicial)

            else:
                print("Sus dados son:")
                self.jugadores[jugador_inicial].cambiar_visibles()
                print(self.jugadores[jugador_inicial].ver_dados())
                self.jugadores[jugador_inicial].cambiar_visibles()

        while True:
            print("Elija una opción: ")
            print("1) Apostar")
            print("2) Dudar")

            puede_calzar = self.arbitro.validar_calce(self.cant_dados_en_juego(), self.jugadores[jugador].ver_cant_dados(), self.dados_iniciales)
            puede_pasar = self.jugadores[jugador].cant_dados == 5

            if puede_calzar:
                print("3) Calzar")
            if puede_pasar:
                print("4) Pasar")

            try:
                accion = int(input())
            except ValueError:
                print("Debe ingresar un número válido.")
                continue

            # validaciones
            if accion == 1 or accion == 2:
                break
            if accion == 3 and puede_calzar:
                break
            if accion == 4 and puede_pasar:
                break

            print("Acción inválida, intente de nuevo.")

        if accion == 1: # subir la apuesta
            print("El jugador subio la apuesta")
            self.apuesta_actual = self.subir_apuesta(jugador)
            self.jugadores[jugador].cambiar_visibles()
            self.rondas_siguientes(jugador)

        elif accion == 2: # dudar la apuesta
            self.persona_duda(jugador)

        elif accion == 3: #calzar los dados
            self.persona_calza(jugador)

        elif accion == 4: # pasar
            self.jugadores[jugador].cambiar_visibles()
            self.rondas_siguientes(jugador)

    def subir_apuesta(self, jugador):
        """
            Pide al jugador su apuesta inicial y la valida.
            Retorna la apuesta válida (cantidad, pinta).
        """
        if self.obligo == False or self.jugadores[jugador].ver_cant_dados() == 1:
            while True:
                try:
                    print("Ingrese su apuesta inicial: ")
                    print(f"Sus dados son: {self.jugadores[jugador].ver_dados()}")

                    apuesta_cant = int(input("Ingrese cantidad: "))
                    apuesta_pinta = str.lower(input("Ingrese pinta: "))

                    apuesta_actual = (apuesta_cant, self.valores_pintas[apuesta_pinta])

                    self.validador.validar_apuesta_subsiguiente(self.apuesta_anterior, apuesta_actual)

                    return apuesta_actual

                except ValueError as e:
                    print(f"Apuesta inválida: {e}. Intente de nuevo.\n")

        else:
            while True:
                try:
                    apuesta_cant = int(input("Ingrese cantidad apuesta: "))
                    apuesta_actual = (apuesta_cant, self.apuesta_anterior[1])

                    self.validador.validar_apuesta_subsiguiente(self.apuesta_anterior, apuesta_actual)

                    return apuesta_actual
                except ValueError as e:
                    print(f"Apuesta incorrecta, intentar nuevamente")

    def persona_duda(self, jugador):
        """
            Resuelve la acción 'dudo' del jugador actual.
            Maneja pérdida de dados, eliminaciones y arranque de nueva ronda.
        """
        # Mostrar los dados ocultos de todos
        self.cambiar_estado_dados_otros_jugadores(jugador)

        cant_total_pinta = self.contar_pintas.contar_pinta(
            self.valores_numeros[self.apuesta_anterior[1]],
            self.jugadores
        )

        resultado = self.arbitro.resolver_duda(self.apuesta_anterior, cant_total_pinta)

        # Volver a ocultar los dados
        self.cambiar_estado_dados_otros_jugadores(jugador)
        self.jugadores[jugador].cambiar_visibles()

        if resultado == 'Apostador pierde':
            perdedor = self.jugador_anterior(jugador)
            self.jugadores[perdedor].perder_dado()
            print(f"El jugador {perdedor} ha perdido un dado.")

            # Si quedó eliminado
            if self.jugadores[perdedor].ver_cant_dados() == 0:
                print(f"El jugador {perdedor} ha sido eliminado.")
                self.jugadores.remove(self.jugadores[perdedor])
                self.ronda_inicial(jugador)

            self.ronda_inicial(perdedor)

        else:  # El jugador actual pierde
            self.jugadores[jugador].perder_dado()
            print(f"El jugador {jugador} ha perdido un dado.")

            # Si quedó eliminado
            if self.jugadores[jugador].ver_cant_dados() == 0:
                print(f"El jugador {jugador} ha sido eliminado.")
                self.jugadores.remove(self.jugadores[jugador])
                self.ronda_inicial(self.jugador_anterior(jugador))

            self.ronda_inicial(jugador)

    def persona_calza(self, jugador):

        self.cambiar_estado_dados_otros_jugadores(jugador)
        cant_total_pinta = self.contar_pintas.contar_pinta(self.valores_numeros[self.apuesta_anterior[1]], self.jugadores, usar_comodines= not self.obligo)

        if self.arbitro.resolver_calce(self.apuesta_anterior, cant_total_pinta, ):
            # Si el calce es correcto
            print(f"El jugador {jugador} acertó el calce. Recupera un dado.")
            self.jugadores[jugador].recuperar_dado()
            self.ronda_inicial(jugador)

        else:
            # Si el calce es incorrecto
            print(f"El jugador {jugador} falló el calce y pierde un dado.")
            self.jugadores[jugador].perder_dado()

            if self.jugadores[jugador].ver_cant_dados() == 0:
                print(f"El jugador {jugador} ha sido eliminado.")
                self.jugadores.remove(jugador)
                self.ronda_inicial(self.jugador_anterior(jugador))
            print(jugador)
            self.ronda_inicial(jugador)

    def jugadores_restantes(self):
        return len(self.jugadores)

    def jugador_anterior(self, jugador_actual):
        if self.direccion == 'Derecha':
            return (jugador_actual - 1) % len(self.jugadores)
        else:
            return (jugador_actual + 1) % len(self.jugadores)

    def jugador_siguiente(self, jugador_actual):
        if self.direccion == 'Derecha':
            return (jugador_actual + 1) % len(self.jugadores)
        else:
            return (jugador_actual - 1) % len(self.jugadores)

    def cambiar_estado_dados_otros_jugadores(self, jugador_actual):
        for j in self.jugadores:
            if j != jugador_actual:
                j.cambiar_visibles()

    def quitar_dado_jugador(self, jugador):
        self.jugadores[jugador].perder_dado()

    def cant_dados_en_juego(self):
        cant = 0
        for j in self.jugadores:
            cant += j.ver_cant_dados()

        return cant

    def verificar_obliga(self, jugador_inicial):
        if self.jugadores[jugador_inicial].ver_cant_dados() == 1 and self.jugadores_obliga[jugador_inicial] == False:
            self.jugadores_obliga[jugador_inicial] = True # una vez obligado no se puede volver a obligar
            return True

        else:
            return False

    def ver_dados_contrincantes(self, jugador):
        i = 0
        for j in self.jugadores:
            j.cambiar_visibles()
            if j != jugador:
                i += 1
                print(f"Dados jugador {i}:")
                print(j.ver_dados())
                j.cambiar_visibles()

    def limitar_dados(self, cant):
        for j in self.jugadores:
            for i in range(5 - cant):
                j.perder_dado()

    def fin_partida(self, jugador):
        print(f"La partida a terminado")
        sys.exit(0)