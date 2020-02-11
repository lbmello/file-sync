"""Arquivo que monta a classe onde são lidos os arquivos dos Hosts."""

from json import load


class Host():
    """Classe criada para gerenciamento dos Hosts, do arquivo Hosts.JSON."""

    _pathHost = '../../conf/Hosts.JSON'

    def __init__(self):
        """Arquivo Hosts.JSON é lido."""
        with open(Host._pathHost, 'r') as file:
            self.hosts = load(file)

    def get_sync_level(self):
        """Retorna valores de SYNC_LEVEL em Hosts.JSON."""
        return self.hosts["SYNC_LEVEL"]

    def get_nodes(self):
        """Retorna valores de NODES em Hosts.JSON."""
        return self.hosts["NODES"]


if __name__ == '__main__':
    Host()
