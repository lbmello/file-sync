
from json import load
from importlib import util

from ..controller.PathFile import PathFile

class Network(object):
    """
    Classe de onde são lidos os valores dos arquivos de configuração e hosts.
    """

    def __init__(self):
        __path_config = Pathfile.path_config()
        __path_host = Pathfile.path_host()

        with open(__path_config, 'r') as __configfile:
            __config = load(__configfile)

            # CONTAGEM DE COMPARTILHAMENTOS
            self.share_count = len(__config["SHARE"])

            # SHARES - CONTEUDO COMPLETO DO SHARE
            self.shares = __config["SHARE"]

            # SHARE ID - SOMENTE OS IDs
            self.share_id = []

            for share in shares:
                self.share_id.append(share["ID"])

        __configfile.close()


        # ARQUIVO HOSTS SENDO LIDO
        with open(__path_host, 'r') as __hostfile:
            __hosts = load(__hostfile)

            # CONTAGEM DE HOSTS
            self.hosts_count = len(__hosts["NODES"])

            # NODES - CONTEUDO COMPLETO DOS NODES
            self.nodes = (__hosts["NODES"])

        __hostfile.close()

    def read_nodes(self):
        return self.nodes
        