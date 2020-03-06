
import hashlib
import os
from pathlib import Path
from random import randint
import threading


path = '/home/lucas/Documents/Python/teste_modules/tree/teste2'
levels = 1
size = 5

def n_file_elements():
    return randint(0, (3 * size))


def n_folder_elements():
    return randint(0, size)


def random_value():
    rand_int = bytes(randint(1,1000000))
      
    obj = hashlib.md5()
    obj.update(rand_int)

    return obj.hexdigest()


def gen_folder(path=str, qtd_folders=int):    
    folders_name = []
    
    for _ in range(qtd_folders):
        dir_name = random_value()

        os.mkdir(f'{path}/{dir_name}')

        folders_name.append(dir_name)

    return folders_name


def gen_files(path=str, qtd_files=int):
    files_name = []

    for _ in range(qtd_files):
        file_name = random_value()
        
        Path(f'{path}/{file_name}').touch()

        files_name.append(file_name)

    return files_name

if __name__ == "__main__":
    current_path = path
    
    for time in range(levels):

        # Gera arquivos na raiz
        gen_files(current_path, n_file_elements())
        
        # Gera pastas na raiz
        time_root_folders = gen_folder(current_path, n_folder_elements())

        for subdir in time_root_folders:
            gen_files(current_path, n_file_elements())

            subdir_folders = gen_folder(f'{current_path}/{subdir}', n_folder_elements())

            for subsubdir in subdir_folders:
                gen_folder(f'{current_path}/{subdir}/{subsubdir}', n_folder_elements())


