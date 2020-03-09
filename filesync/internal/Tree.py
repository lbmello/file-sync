"""Módulo que que retorna a árvore de diretórios e arquivos do share_id 
repassado em formato str."""

import os

from ..data.Config import Config

class Tree():
    """Módulo que que retorna a árvore de diretórios e arquivos do share_id 
    repassado em formato str."""

    def __init__(self, share_id=str):
        self.share_id = share_id

        _config = Config()

        _shares = _config.get_share_config()
        
        for _share in _shares:
            if _share['ID'] == self.share_id:
                                
                source = (_share['SOURCE'])

        self.tree = []


        for root, dirs, files in os.walk(top=source, topdown=True):              
            self.tree.append({'source':root, 'files': files})
    

    def get_tree(self):
        """Retorna árvore completa em formato de lista com dict aninhado."""
        return self.tree


        
