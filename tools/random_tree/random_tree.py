
from datetime import datetime
import hashlib
import os
from pathlib import Path
from random import randint

from queue import Queue

class Root(object):
    path = '/tmp/testetree'
    levels = 8
    size = 2
    debug = False

    def __init__(self):
        self.path = Root.path

        try:
            os.mkdir(self.path)
            if Root.debug == True:
                print(f'Diretório raiz criado em {self.path}')
        
        except FileExistsError:
            if Root.debug == True:
                print('Diretório Raiz já criado!')
    
    @classmethod
    def add_existing_subdir_to_queue(cls):
        """Se a fila estiver vazia, percorre o diretório atual e adiciona subpastas na fila."""

        if FolderQueue.is_empty():
            for dirpath, _, _ in os.walk(top=cls.path, topdown=True):
                FolderQueue.fila.push(dirpath)

    @classmethod
    def n_file_elements(cls):
        """Retorna inteiro randomico entre 1 e 3*{size} para gerar arquivos."""
        
        return randint(1, (3 * Root.size))

    @classmethod
    def n_folder_elements(cls):
        """Retorna inteiro randomico entre 1 e 2*{size} para gerar pastas."""
        
        return randint(1, (2 * Root.size))

    @classmethod
    def random_value(cls):
        """Retorna string com uma hash MD5 aleatoria, gerada a partir da hora atual, multiplicado por um valor de 1 a 1000000."""

        #TODO: Reescrever altaracao dos valores!
        random_value = datetime.now()
        random_value = str(random_value)
        random_value = random_value.replace('-','').replace(':','').replace(' ','').replace('.','')
        random_value = random_value * (randint(0, 1000000))
        random_value = bytes(random_value, encoding='utf8')

        obj = hashlib.md5()
        obj.update(random_value)

        return obj.hexdigest()

class Folder(Root):
    def __init__(self):
        self.path = Root.path  

    def create_branch(self):
        """Cria o path completo dos galhos e os adiciona na fila."""

        begin_folders = Folder.gen_folder_name(path=self.path, n_folders=Root.n_folder_elements())

        for branch in begin_folders:
            for _ in range(Root.levels):
                branch = f'{branch}/{Root.random_value()}'

            FolderQueue.fila.push(branch)
    
    def tree_to_queue(self):
        """Roda um tree e adiciona todas as pastas na fila."""

        tree = Tree().get_tree(path=self.path)

        for folder in tree:
            FolderQueue.fila.push(folder)
    
    @classmethod
    def create_queue_folders(cls):
        """Limpa a fila e cria as pastas."""

        if Root.debug == True:
            print('Criando pastas!')

        for _ in range(FolderQueue.fila.len()):
            folder = FolderQueue.fila.pop()
            
            os.makedirs(folder)

    @classmethod
    def create_queue_subfolders(cls):
        """Limpa a fila e cria as subpastas."""

        if Root.debug == True:
            print('Criando subpastas!')

        for _ in range(FolderQueue.fila.len()):
            folder = FolderQueue.fila.pop()
            subfolder = Root.random_value()

            os.makedirs(f'{folder}/{subfolder}')

    @classmethod
    def gen_folder_name(cls, path=str, n_folders=int):    
        """Gera n{n_folders} de nomes para pasta e retorna lista com nomes das pastas."""
        
        folders_name = []

        for _ in range(n_folders):
            dir_name = Root.random_value()

            folders_name.append(f'{Folder.path}/{dir_name}')

        return folders_name

class Files():
    def __init__(self):
        self.path = Folder.path
    
    @classmethod
    def gen_files(cls, n_files):
        """Gera n{n_files} arquivos no diretorio informado em {path} e retorna lista com nomes dos arquivos."""
        
        if not FolderQueue.is_empty():
            folder = FolderQueue.fila.pop()

            for _ in range(n_files):
                file_name = Root.random_value()
                Path(f'{folder}/{file_name}').touch()

    @classmethod
    def create_queue_files(cls):
        """Limpa a fila e cria os arquivos."""

        if Root.debug == True:
            print('Criando arquivos!')

        if not FolderQueue.is_empty():
            for _ in range(FolderQueue.fila.len()):                
                cls.gen_files(n_files=Root.n_file_elements())
    

class FolderQueue():
    fila = Queue()

    @classmethod
    def is_empty(cls):
        """Retorna se a fila está vazia."""
        if cls.fila.len() == 0:
            return True
        else:
            return False

class Tree():
    def __init__(self):
        self.tree = []

    def get_tree(self, path):
        """ Retorna a lista das pastas."""

        for root, _, _ in os.walk(top=path, topdown=True):              
            self.tree.append(f'{root}')
        return self.tree

if __name__ == "__main__":
    # Quando instanciado, já adiciona o default path na fila para criação
    root = Root()

    # Cria os galhos da arvore
    folder = Folder()
    folder.create_branch()
    folder.create_queue_folders()

    # Realimenta a fila com os paths e cria subpastas
    folder.tree_to_queue()
    folder.create_queue_subfolders()

    # Realimenta a fila  com paths e cria os arquivos
    folder.tree_to_queue()
    files = Files()
    files.create_queue_files()
    