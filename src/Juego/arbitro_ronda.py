class ArbitroRonda:
    def resolver_duda(self, apuesta, conteo_real):
        cantidad, pinta = apuesta
        if conteo_real < cantidad:
            return 'Apostador pierde'
        else:
            return 'Dudador pierde'

    def resolver_calce(self, apuesta, conteo_real):
        cantidad, pinta = apuesta
        if conteo_real == cantidad:
            return 'Apostador gana'
        else:
            return 'Apostador pierde'

    def validar_calce(self, dados_restantes, dados_jugador, dados_iniciales):
        if dados_jugador == 1:
            return True

        mitad_dados = self.mitad(dados_iniciales)
        if dados_restantes >= mitad_dados:
            return True

        return False

    def mitad(self, total):
        return (total + 1) // 2