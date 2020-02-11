
from json import load
from importlib import util

from classes.controller.PathFile import PathFile

class Network(object):
    """
    Classe de onde são lidos os valores dos arquivos de configuração e hosts.
    """

    __path_config = PathFile.get_path_config()
    __path_host = PathFile.get_path_host()

   # ARQUIVO CONFIG SENDO LIDO
    with open(__path_config, 'r') as __configfile:
        __config = load(__configfile)

        # CONTAGEM DE COMPARTILHAMENTOS
        share_count = len(__config["SHARE"])
        
        # SHARES - CONTEUDO COMPLETO DO SHARE
        shares = __config["SHARE"]
        
        # SHARE ID - SOMENTE OS IDs
        share_id = []
        
        for share in shares:
            share_id.append(share["ID"])

    __configfile.close()


    @classmethod
    def get_share_count(cls):
        return cls.share_count

    @classmethod
    def get_share_id(cls):
        return cls.share_id


    # ARQUIVO HOSTS SENDO LIDO
    with open(__path_host, 'r') as __hostfile:
        __hosts = load(__hostfile)

        # CONTAGEM DE HOSTS
        hosts_count = len(__hosts["NODES"])
        
        # NODES - CONTEUDO COMPLETO DOS NODES
        nodes = (__hosts["NODES"])
    
    __hostfile.close()


    @classmethod
    def get_nodes(cls):
        return cls.nodes
        