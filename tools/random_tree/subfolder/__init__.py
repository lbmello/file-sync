from root import Root

class Subfolder(Root):

    def __init__(self, current_folder=Root.path):        
        self.current_folder = current_folder

        #self.subdirs = Root.gen_folder(path=self.current_folder, n_folders=Root.n_folder_elements())
        #self.subfiles = Root.gen_files(path=self.current_folder, n_files=Root.n_file_elements())
    
        self.subdirs = Root.gen_folder_name(path=self.current_folder, n_folders=Root.n_folder_elements())

        for subdir in self.subdirs:
            Root.list_subdirs.push(f'{self.current_folder}/{subdir}')

        
    def get_subdirs(self):
        return self.subdirs