"""Módulo que gerencia a classe onde são lidos os arquivos dos Hosts."""

from json import load


class model_Host():
    """Classe criada para gerenciamento dos Hosts, do arquivo Hosts.JSON."""

    _pathHost = '../../conf/Hosts.JSON'

    def __init__(self):
        """Arquivo Hosts.JSON é lido."""
        with open(model_Host._pathHost, 'r') as file:
            self.hosts = load(file)

    def get_sync_level(self):
        """Retorna valores de SYNC_LEVEL em Hosts.JSON."""
        return self.hosts["SYNC_LEVEL"]

    def get_nodes(self):
        """Retorna valores de NODES em Hosts.JSON."""
        return self.hosts["NODES"]


if __name__ == '__main__':
    teste = model_Host()
    teste.get_nodes()
