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


    def update_tree(self):
        """Reseta self.tree com dados do objeto de tree."""

        self.tree = self.tree_obj.get_tree()

    def get_checksum(self):
        """Pega tree instanciado e gera hash dos arquivos.

        Salva dados no formato:
        {'source': 'path', 'file': 'file_name', 'checksum': 'MD5_checksum'}
        """

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

        self._set_changes_file()


    def get_actual_state(self):
        """Retorna se True se o diretorio .fs foi criado no share."""

        return self.checksum_files


    def _set_changes_file(self):
        """Cria arquivo CHANGES.json em .fs de cada share."""

        ch_file = open(f'{self.share}/.fs/CHANGES.json', 'w+')
        
        for line in self.checksum_files:
            ch_file.write(f'{line}')

        ch_file.close()
