"""Leitura do arquivo Host.JSON."""

from json import load


class Host:
    """Leitura do arquivo Hosts.JSON."""

    _pathHost = 'file-sync/conf/Hosts.JSON'

    def __init__(self):
        """Arquivo Hosts.JSON é lido."""
        with open(Host._pathHost, 'r') as file:
            self.hosts = load(file)

    
    def get_sync_level(self):
        """Retorna todos valores de SYNC_LEVEL em Hosts.JSON."""
        return self.hosts["SYNC_LEVEL"]

    
    def get_nodes(self):
        """Retorna todos valores de NODES em Hosts.JSON."""
        return self.hosts["NODES"]

    
    def get_nodes_name(self):
        """Retorna lista com somente o nome dos nodes."""
        return list(self.hosts.keys())

    
    def get_some_node(self, n_node):
        """Retorna valores de um nó específico, passado por parâmetro."""
        return self.hosts[n_node]

    
    def size(self):
        """Retorna contagem em inteiro dos nodes."""
        return(len(self.hosts))

if __name__ == '__main__':
    ...
