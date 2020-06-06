"""Modulo que que retorna a arvore de diretorios e arquivos do share."""

import os

from ..data.Config import Config

class Tree:
    """Modulo que que retorna a arvore de diretorios e arquivos do share."""

    def __init__(self, source):
        """source, Config.JSON > SHARE:SOURCE"""

        self.source = source

        self.tree = list()
        self.make_tree() 


    def get_tree(self):
        """Retorna arvore completa em formato de lista com dict aninhado."""
        
        return self.tree


    def make_tree(self):
        """ Funcao interna usada para criar a arvore."""

        for root, _ , files in os.walk(top=self.source, topdown=True):              
            self.tree.append({'source':root, 'files': files})
