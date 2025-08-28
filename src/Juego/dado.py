from collections.abc import generator

from src.servicios.generador_aleatorio import GeneradorAleatorio

class Dado:

    valores = { 1 : "as", 2 : "tontos",
                3 : "trenes", 4 : "cuadras",
                5 : "quinas", 6 : "sextas" }

    valor : int

    def __init__(self):
        generador = GeneradorAleatorio()
        self.valor = generador.generar(1,6)

    def obtener_valor(self):
        return self.valores[self.valor]

    def cambiar_valor(self):
        generador = GeneradorAleatorio()
        self.valor = generador.generar(1,6)