"""Leitura do arquivo Time.JSON."""

from json import load


class Time:
    """Leitura do arquivo Time.JSON."""

    pathTime = 'file-sync/conf/Time.JSON'

    def __init__(self):
        """Arquivo Time.JSON é lido."""

        self.times = str()
       
        with open(Time.pathTime, 'r') as file:
            self.times = load(file)
            self.time_default = self.times["DEFAULT"]



    def get_times(self):
        """Retorna todas as entradas de tempo."""
        return self.times


    def get_time_default(self):
        """Retorna a entrada de tempo DEFAULT."""
        return self.time_default

