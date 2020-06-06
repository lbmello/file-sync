"""Módulo para identificar quando existiu alteracao em algum share."""

import hashlib

from ..data.Config import Config
from .tree import Tree

class Changes:
    """Modulo para identificar quando existiu alteracao em algum share."""

    def __init__(self, source):
        """source, Config.JSON > SHARE:SOURCE"""
        
        self.share = source
        self.checksum_files = []

        # Instancia de Tree
        self.tree_obj = Tree(f'{self.share}')
        
        self.update_tree()
        self.get_checksum()

        for folder in self.tree:
            _source = folder['source']
            _files = folder['files']

            if _files:
                for _file in _files:
                    open_file = open(f'{_source}/{_file}', 'r')

                    try:
                        checksum = hashlib.md5((open_file.read()).encode()).hexdigest()

                        print(f'hashs lidas com sucesso')
                    
                    except UnicodeDecodeError:
                        print(f'Erro no decode de {_file}')

                    self.checksum_files.append({'source':_source, 
                                               'file': _file,
                                               'checksum': checksum})


                    open_file.close()    
        

    def update_tree(self):
        self.tree = self.tree_obj.get_tree()

    def get_checksum(self):
        ...

    def get_actual_state(self):
        return self.checksum_files

    # TODO: Criar classe que leia os dados de algum documento JSON com o ultimo estado dos arquivos para comparacao. 
