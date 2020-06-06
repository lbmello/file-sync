"""Módulo para identificar quando existiu alteracao em algum share."""

import hashlib

from ..data.Config import Config
from .tree import Tree

class Changes:
    """Modulo para identificar quando existiu alteracao em algum share."""

    def __init__(self, share_id=str):
        """Inicializador de Changes. Exige share_id em formato str."""
        
        self.share = share_id

        # Instância de Tree
        _tree_obj = Tree(f'{self.share}')
        self.tree = _tree_obj.get_tree()
        
        self.checksum_files = []

        for folder in self.tree:
            _source = folder['source']
            _files = folder['files']

            if _files:
                for _file in _files:
                    open_file = open(f'{_source}/{_file}', 'r')

                    try:
                        checksum = hashlib.md5((open_file.read()).encode()).hexdigest()
                    
                    except UnicodeDecodeError:
                        print(f'Erro no decode de {_file}')

                    self.checksum_files.append({'source':_source, 
                                               'file': _file,
                                               'checksum': checksum})

                    open_file.close()

    def get_actual_state(self):
        return self.checksum_files

    # TODO: Criar classe que leia os dados de algum documento JSON com o ultimo estado dos arquivos para comparacao. 

if __name__ == "__main__":
    teste = Changes('001')