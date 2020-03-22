from abstract_doenca import AbstractDoenca

class Doenca(AbstractDoenca):

    @property
    def _falta_ar(self):
            print("> Falta de ar ?")
            
    @property
    def _nariz_escorrendo(self):
        print("> Nariz está escorrendo ?")

    @property
    def _dor_garganta(self):
        print("> Dor de garganta ?")

    @property
    def _tosse(self):
        print("> Tosse ?")

    @property
    def _febre(self):
        print("> Febre ?")

    @property
    def get_sintomas_corona_virus(self):
        super().get_sintomas_corona_virus()
        self._falta_ar
        self._nariz_escorrendo
        self._dor_garganta
        self._tosse
        self._febre

    @property
    def get_sintomas_gripe(self):
        super().get_sintomas_gripe()
        self._nariz_escorrendo
        self._dor_garganta
        self._tosse
        self._febre