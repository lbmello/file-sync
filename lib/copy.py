import os

# CÓPIA SIMPLES DE ARQUIVO, USANDO O RSYNC DO LINUX
def copy_file(orig, user, ip, path):
     os.system('rsync -avzh %s %s@%s:%s' %(orig, user, ip, path))