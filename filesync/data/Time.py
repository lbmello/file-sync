"""Leitura do arquivo Time.JSON."""

from json import load


class Time():
    """Classe criada para gerenciamento das entradas de tempo, do arquivo Time.JSON."""

    pathTime = 'conf/Time.JSON'

    def __init__(self):
        """Arquivo Time.JSON é lido."""
        with open(Time.pathTime, 'r') as file:
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
