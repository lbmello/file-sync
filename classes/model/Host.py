"""Arquivo que monta a classe onde são lidos os arquivos dos Hosts."""

from Network import Network


class Host():
    """
    Classe criada para gerenciamento dos Hosts, lidos no arquivo Hosts.JSON.
    """
        
    def __init__(self):
        network = Network()
        
        nodes = Network.read_nodes()

        for key, value in nodes.items():
            self.nome = key
            self.ip = value[0]
            self.description = value[1]
            self.uid = value[2]
            self.edge = value[3]

        print(self.ip)
        print(self.description)
        print(self.uid)
        print(self.edge)

if __name__ == '__main__':
    Host()