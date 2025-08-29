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