
import os

class folder:
    """Modulo que gerencia os diretorios internos do projeto."""
    
    def __init__(self, source):
        """source, Config.JSON > SHARE:SOURCE"""

        self.path = source
        self.fs_folder = f'{self.path}/.fs'
        print(self.fs_folder)


        if self.folder_exist() == False:
            print(self.create_folder())

    
    def folder_exist(self):
        """Identifica se o diretorio oculto do projeto existe."""

        return os.path.exists(self.fs_folder)


    def create_folder(self):
        """Cria o diretorio oculto do projeto."""

        try:
            os.makedirs(self.fs_folder)

            raise f'diretorio {self.fs_folder} criado com sucesso!'
        
        except:
            raise f'erro nao tratado ao criar {self.fs_folder}'''