"""Arquivo da classe Node."""

from ..data.Host import Host


class Node():
    """Retorna os valores contidos na primeira parte do arquivo Hosts.JSON."""

    def __init__(self):
        """Instancia objeto da classe Host()."""
        hosts = Host()

        self.node = hosts.get_nodes()

    def size(self):
        """Retorna contagem em inteiro dos nodes."""
        return(len(self.node))

    def get_nodes_name(self):
        """Retorna lista com o nome dos nodes."""
        return list(self.node.keys())

    def get_some_node(self, n_node):
        """Retorna valores de um nó específico, passado por parâmetro."""
        return self.node[n_node]


if __name__ == "__main__":
    pass
