from command import Command
from doenca import Doenca

class GripeCommand(Command):

    def __init__(self, doenca):
        self.doenca = doenca

    @property
    def execute(self):
        self.doenca.get_sintomas_gripe