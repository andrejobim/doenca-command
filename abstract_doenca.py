from abc import ABC, abstractmethod

class AbstractDoenca(ABC):

    _texto = " Você está com algum desses sintomas ?"

    @abstractmethod
    def get_sintomas_corona_virus(self):
        print("Corona Virus:" + self._texto)
        print()

    @abstractmethod
    def get_sintomas_gripe(self):
        print("Gripe:" + self._texto)
        print()      
