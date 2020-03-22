import argparse

from doenca import Doenca
from corona_virus_command import CoronaVirusCommand
from gripe_command import GripeCommand

def execute(args):

    tipo_doenca = Doenca()
    corona = CoronaVirusCommand(tipo_doenca)
    gripe = GripeCommand(tipo_doenca)

    if (args.tipo == 'gripe'):
        gripe.execute
    elif args.tipo == 'corona':
        corona.execute
    else:
        print("Tipo de doença desconhecido!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Consultando os sintomas', prog="controle_doenca")
    parser.add_argument('--tipo', help='--tipo gripe | coronavirus')
    execute(parser.parse_args())