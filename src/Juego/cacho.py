from src.Juego.dado import Dado

class Cacho:

    cant_dados : int
    visibles : bool = False
    dados : list[Dado]
    dados_extra : int

    def __init__(self):
        self.cant_dados = 5
        self.dados = [Dado() for _ in range(self.cant_dados)]
        self.dados_extra = 0

    def ver_cant_dados(self):
        return self.cant_dados

    def ver_dados_extra(self):
        return self.dados_extra

    def cambiar_visibles(self):
        self.visibles = not self.visibles

    def ver_dados(self):
        if self.visibles == False:
            return None
        else:
            return [dado.obtener_valor() for dado in self.dados]

    def perder_dado(self):
        if self.dados_extra == 0:
            self.cant_dados -= 1
            self.dados.pop()

        else:
            self.dados_extra -= 1

    def agitar(self):
        for dado in self.dados:
            dado.cambiar_valor()

    def recuperar_dado(self):
        if self.cant_dados == 5:
            self.dados_extra += 1

        else:
            self.dados.append(Dado())
            self.cant_dados += 1
