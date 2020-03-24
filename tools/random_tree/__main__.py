from random_tree import Root, Folder, Files

if __name__ == "__main__":
    pass
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