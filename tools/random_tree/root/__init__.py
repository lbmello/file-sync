"""Modulo root."""

import hashlib
import os
from datetime import datetime
from pathlib import Path
from random import randint

from queue import Queue

class Root():
    """Classe que gerencia a raiz do tree."""

    path = '/home/lucas/Documents/Python/teste_modules/tree/testeclass'
    last_dir = ''
    
    levels = 5
    size = 10

    # Declaração de fila
    list_subdirs = Queue()

    @classmethod
    def add_subdir(cls):
        if cls.list_subdirs.len() == 0:
            for dirpath, dirname, files in os.walk(top=f'Root.path', topdown=True):
                Root.list_subdirs.push(dirpath)
                print('DIRPATH: ', dirpath)
                
    @classmethod
    def create_subfolder(cls):
        """Consumer para criação das pastas."""
        while True:

            if Root.list_subdirs.len() != 0:
                #if Root.list_subdirs.peek() != Root.path:
                element = Root.list_subdirs.pop()
                

                try:
                    os.mkdir(path=element)
                    return element

                except FileExistsError:
                    #Root.list_subdirs.pop()
                    print('Arquivo existe')

    def __init__(self):
        """Inicializador do módulo root."""
        
        # Se existirem arquivos no diretório, adiciona ao final da fila
        #Root.add_subdir()

        self.path = Root.path

        self.root_dirs = Root.gen_folder_name(path=f'{self.path}', n_folders=Root.n_folder_elements())

        for directory in self.root_dirs:
            Root.list_subdirs.push(directory)

        #self.root_files = Root.gen_files(path=f'{self.path}', n_files=Root.n_file_elements())


    def n_file_elements():
        """Retorna inteiro randomico entre 1 e 3*{size} para gerar arquivos."""
        
        return randint(1, (4 * Root.size))


    def n_folder_elements():
        """Retorna inteiro randomico entre 1 e {size} para gerar pastas."""
        return randint(1, (2 * Root.size))


    def random_value():
        """Retorna string com uma hash MD5 aleatoria de 1 a 1000000."""

        #TODO: Reescrever altaracao dos valores!
        random_value = datetime.now()
        random_value = str(random_value)
        random_value = random_value.replace('-','').replace(':','').replace(' ','').replace('.','')
        random_value = random_value * (randint(0, 100))
        random_value = bytes(random_value, encoding='utf8')

        obj = hashlib.md5()
        obj.update(random_value)

        return obj.hexdigest()

    '''def gen_folder(path=str, n_folders=int):    
        """Gera n{n_folders} pastas no diretorio informado em {path} e retorna lista com nomes das pastas."""

        folders_name = []

        for _ in range(n_folders):
            dir_name = Root.random_value()

            os.mkdir(f'{path}/{dir_name}')

            folders_name.append(dir_name)

        return folders_name'''

    def gen_folder_name(path=str, n_folders=int):    
        """Gera n{n_folders} de nomes para pasta e retorna lista com nomes das pastas."""
        path = path

        folders_name = []

        for _ in range(n_folders):
            dir_name = Root.random_value()

            folders_name.append(f'{path}/{dir_name}')

        return folders_name


    def gen_files(path=str, n_files=int):
        """Gera n{n_files} arquivos no diretorio informado em {path} e retorna lista com nomes dos arquivos."""

        files_name = []

        for _ in range(n_files):
            file_name = Root.random_value()

            Path(f'{path}/{file_name}').touch()

            files_name.append(file_name)

        return files_name