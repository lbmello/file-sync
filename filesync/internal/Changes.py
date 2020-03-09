"""Módulo para identificar quando existiu alteração em algum share."""

import os
import subprocess
import hashlib

from ..data.Config import Config
from .Tree import Tree

class Changes():
    """Módulo para identificar quando existiu alteração em algum share."""

    def __init__(self, share_id=str):
        """Inicializador de Changes. Exige share_id em formato str."""
        
        self.share = share_id

        tree_obj = Tree(f'{self.share}')
        self.tree = tree_obj.get_tree()

        for folder in self.tree:
            _source = folder['source']
            _files = folder['files']

            md5_obj = hashlib.md5()

            self.checksum_files = []

            if len(_files) > 1:
                for _file in _files:
                    _file = bytes(_file, encoding='utf8')
                    
                    md5_obj.update(_file)

                    checksum = md5_obj.hexdigest()
                    
                    self.checksum_files.append({'source':_source, 
                                               'file': _file,
                                               'checksum': checksum})

    def get_actual_state(self):
        # TODO: Criar classe que leia os dados de algum documento JSON com o ultimo estado dos arquivos para comparação. 
        pass