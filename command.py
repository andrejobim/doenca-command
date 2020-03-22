from abc import ABC, abstractmethod

class Command:

    @abstractmethod
    def execute(self):
        pass