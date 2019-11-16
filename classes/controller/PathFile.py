
from os import path

class PathFile(object):
    """
    Classe responsável pelos retornos dos caminhos do sistema.
    """

    def __init__(self):
        """
        Método construtor de Pathfile.
        """        
        __my_path = path.abspath(
            path.dirname(__file__))
        
        self.path_config = path.join(
            __my_path, "../../conf/Config.JSON")
               
        self.path_host = path.join(
            __my_path, "../../conf/Hosts.JSON")

    def path_config(self):
        """Retorna o caminho absoluto do arquivo Config.JSON."""

        return self.path_config

    def path_host(self):
        """Retorna o caminho absoluto do arquivo Hosts.JSON."""

        return self.path_host
