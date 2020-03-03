"""Leitura do arquivo de Config.JSON."""

from json import load


class Config():
    """Classe criada para gerenciamento das Configurações, do arquivo Config.JSON."""
    
    _path_config = 'conf/Config.JSON'

    def __init__(self):
        """Arquivo Config.JSON é lido."""
        with open(Config._path_config, 'r') as file:
            self.config = load(file)

    def get_global_config(self):
        """Retorna apenas configurações globais."""
        return self.config["GLOBAL"]

    def get_share_config(self):
        """Retorna apenas configurações referentes aos Shares."""
        return self.config["SHARE"]

    def get_share_counter(self):
        """Retorna contagem total dos Shares."""
        return (len(self.config['SHARE']))

    def get_share_by_id(self, n_id):
        """Retorna Share solicitado via parâmetro como ID (str) para select."""  
        _n_id = str(n_id)
        _shares = self.config['SHARE']

        _keys = []
        _values = []

        for _index, _share in enumerate(_shares):
            _keys.append(_share.keys())
            _values.append(_share.values())

            if n_id in _values[_index]:
                return _share         

    def get_share_by_name(self, nome):
        """Retorna Share solicitado via parâmetro como nome (str) para select."""
        _nome = str(nome)
        _shares = self.config['SHARE']

        _keys = []
        _values = []

        for _index, _share in enumerate(_shares):
            _keys.append(_share.keys())
            _values.append(_share.values())

            if _nome in _values[_index]:
                return _share

        
if __name__ == "__main__":
    teste = model_Config()
    a = teste.get_share_by_id('Share_Teste1')
    print(a)    