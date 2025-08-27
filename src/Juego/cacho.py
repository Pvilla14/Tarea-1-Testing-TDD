from src.Juego.dado import Dado

class Cacho:

    cant_dados : int
    visibles : bool = False
    dados : list[Dado]

    def __init__(self):
        self.cant_dados = 5
        self.dados = [Dado() for _ in range(self.cant_dados)]

    def ver_cant_dados(self):
        return self.cant_dados

    def cambiar_visibles(self):
        self.visibles = not self.visibles

    def ver_dados(self):
        if self.visibles == False:
            return None
        else:
            return [dado.obtener_valor() for dado in self.dados]
