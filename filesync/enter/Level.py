"""Retorna os valores contidos na segunda parte do arquivo Hosts.JSON."""

from ..data.Host import Host


class Level():
    """Retorna os valores contidos na segunda parte do arquivo Hosts.JSON."""

    def __init__(self):
        """Instancia objeto da classe Host()."""
        hosts = Host()

        self.level = hosts.get_sync_level()

    def size(self):
        """Retorna inteiro com a contagem dos niveis."""
        return(len(self.level))

    def get_some_level(self, n_level):
        """Retorna dicionario com valor do nivel passado por parametro."""
        """Compara se o nivel informado existe no arquivo Hosts.
        JSON, identificando se ele é menor que a contagem total
        de todos os niveis."""
        _size = self.size()

        if n_level >= _size:
            return ("Numero do nivel invalido, Maximo é {}").format(_size)

        else:
            _level = 'LEVEL_{}'.format(n_level)

            return self.level[_level]


if __name__ == "__main__":
    teste = Level()
    print(teste.get_some_level(4))
