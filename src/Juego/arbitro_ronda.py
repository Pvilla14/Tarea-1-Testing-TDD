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
        return dados_jugador == 1 or dados_restantes >= self.mitad(dados_iniciales)

    def mitad(self, total):
        return (total + 1) // 2