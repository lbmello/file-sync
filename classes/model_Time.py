"""Módulo que gerencia a classe onde são lidos as entradas de tempo."""

from json import load


class model_Time():
    """Classe criada para gerenciamento das entradas de tempo, do arquivo Time.JSON."""

    _path_time = '../../conf/Time.JSON'

    def __init__(self):
        """Arquivo Time.JSON é lido."""
        with open(model_Time._path_time, 'r') as file:
            self.time = load(file)

    def get_times(self):
        """Retorna todas as entradas de tempo."""
        return self.time

    def get_time_default(self):
        """Retorna a entrada de tempo DEFAULT."""
        return self.time["DEFAULT"]


if __name__ == "__main__":
    teste = model_Time()
    t = teste.get_times()
    print(t)
