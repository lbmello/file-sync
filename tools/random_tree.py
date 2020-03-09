
import hashlib
import os
from datetime import datetime
from pathlib import Path
from random import randint
import threading



class Root():
    path = '/home/lucas/Documents/Python/teste_modules/tree/testeclass'
    
    levels = 5
    size = 10

    list_subdirs = []

    raise IndexError('Fila Vazia!') 

    @classmethod
    def add_subdir(cls):
        if len(cls.list_subdirs) == 0:
            for root, dirs, files in os.walk(top=Root.path, topdown=True):
                Root.list_subdirs.append(root)
                
    @classmethod
    def create_subfolders(cls):
        if len(cls.list_subdirs) != 0:
            pass


    def __init__(self):
        self.path = Root.path

        self.root_dirs = Root.gen_folder(path=f'{self.path}', n_folders=Root.n_folder_elements())

        self.root_files = Root.gen_files(path=f'{self.path}', n_files=Root.n_file_elements())


        # Se existirem arquivos no diretório, adiciona ao final da lista
        Root.add_subdir()

    def n_file_elements():
        """Retorna inteiro randomico entre 1 e 3*{size} para gerar arquivos."""
        
        return randint(1, (4 * Root.size))


    def n_folder_elements():
        """Retorna inteiro randomico entre 1 e {size} para gerar pastas."""
        return randint(1, (2 * Root.size))


    def random_value():
        """Retorna string com uma hash MD5 aleatoria de 1 a 1000000."""

        """TODO: Reescrever função!"""
        random_value = datetime.now()
        random_value = str(random_value)
        random_value = random_value.replace('-','').replace(':','').replace(' ','').replace('.','')
        random_value = random_value * (randint(0, 100000))
        random_value = bytes(random_value, encoding='utf8')

        obj = hashlib.md5()
        obj.update(random_value)

        return obj.hexdigest()

    def gen_folder(path=str, n_folders=int):    
        """Gera n{n_folders} pastas no diretorio informado em {path} e retorna lista com nomes das pastas."""

        folders_name = []

        for _ in range(n_folders):
            dir_name = Root.random_value()

            os.mkdir(f'{path}/{dir_name}')

            folders_name.append(dir_name)

        return folders_name


    def gen_files(path=str, n_files=int):
        """Gera n{n_files} arquivos no diretorio informado em {path} e retorna lista com nomes dos arquivos."""

        files_name = []

        for _ in range(n_files):
            file_name = Root.random_value()

            Path(f'{path}/{file_name}').touch()

            files_name.append(file_name)

        return files_name

class Subfolder(Root):

    def __init__(self, current_folder=Root.path):        
        if len(Root.list_subdirs) == 0:
            self.current_folder = current_folder
        else:
            self.current_folder = Root.list_subdirs[-1]

        self.subdirs = Root.gen_folder(path=self.current_folder, n_folders=Root.n_folder_elements())
        self.subfiles = Root.gen_files(path=self.current_folder, n_files=Root.n_file_elements())
    
        for subdir in self.subdirs:
            Root.list_subdirs.append(f'{self.current_folder}/{subdir}')


if __name__ == "__main__":
    root = Root()
    subfolder = Subfolder()

    print(root.list_subdirs)
