"""Leitura do arquivo Domain.JSON."""

from json import load


class Domain:
    """Leitura do arquivo Domain.JSON."""

    pathTime = 'file-sync/conf/Domain.JSON'

    def __init__(self):
        """Arquivo Domain.JSON é lido."""

        self.domain = str()
       
        with open(Domain.pathTime, 'r') as file:
            self.domain = load(file)


    def get_domain(self):
        """Retorna todas as entradas de tempo."""
        return self.domain
