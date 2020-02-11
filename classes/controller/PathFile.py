
from os import path

class PathFile(object):
    """
    Classe responsável pelos retornos dos caminhos do sistema.
    """
    
    __my_path = path.abspath(
    path.dirname(__file__))
        
    path_config = path.join(
        __my_path, "../../conf/Config.JSON")
               
    path_host = path.join(
        __my_path, "../../conf/Hosts.JSON")

    @classmethod
    def get_path_config(cls):
        """Retorna o caminho absoluto do arquivo Config.JSON."""

        return cls.path_config

    def get_path_host(cls):
        """Retorna o caminho absoluto do arquivo Hosts.JSON."""

        return cls.path_host
