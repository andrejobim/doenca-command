from command import Command
from doenca import Doenca

class CoronaVirusCommand(Command):

    def __init__(self, doenca):
        self.doenca = doenca

    @property
    def execute(self):
        self.doenca.get_sintomas_corona_virus