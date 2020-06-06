
import os
import shutil

# Diretorios
fs_project = '/home/filesync/conf/'
fs_linux = '/etc/filesync/'

# Cria pasta em /etc
if not os.path.exists(fs_linux):
    os.makedirs(fs_linux)

# Arquivos de conf
conf = 'Config.JSON'
domain = 'Domain.JSON'
hosts = 'Hosts.JSON'
time = 'Time.JSON'

files = [conf, domain, hosts, time]

# Copia arquivos para a pasta no Linux
for conf_file in files:
    origin = f'{fs_project}/{conf_file}'
    destiny = f'{fs_linux}/{conf_file}'

    shutil.copyfile(src = origin, dst = destiny)