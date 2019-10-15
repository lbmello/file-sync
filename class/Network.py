"""Arquivo que monta a classe onde são lidos os arquivos dos Shares."""

from json import load
from os import path


class Network(object):
    """Classe de onde são lidos os arquivos dos Shares."""

    def __init__(self):
        """Metodo construtor."""
        # RELATIVE PATH DECLARATION
        my_path = path.abspath(
            path.dirname(__file__))

        pathConfig = path.join(
            my_path, "../conf/Config.JSON")

        with open(pathConfig, 'r') as file:
            self.config = load(file)

            self.share_count = len(self.config["SHARE"])

            # SHARES - CONTEUDO COMPLETO DO SHARE
            self.shares = self.config["SHARE"]

            # SHARE ID - SOMENTE OS IDs
            self.share_id = []

            for share in self.shares:
                self.share_id.append(share["ID"])
