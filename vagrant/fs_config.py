
import os
import shutil

# Diretorios
fs_project = '/mnt/file-sync'
fs_linux = '/etc/file-sync'

if os.path.exists(fs_linux):
    print(f'Diretorio {fs_linux} ja existe!')

# Cria pasta em /etc
if not os.path.exists(fs_linux):
    os.makedirs(fs_linux)

# Faz as copias do projeto, exceto venv  
shutil.copytree(src = fs_project, 
                dst = fs_linux, 
                copy_function = shutil.copy2, 
                dirs_exist_ok = True,
                ignore = lambda directory, contents: ['venv'] if directory == fs_project else [])


# Arquivos de conf e suas estruturas de dados
conf = f'{fs_linux}/conf/Config.JSON'
conf_data = '''
{
    "GLOBAL": {},
    "SHARE": []
}
'''

domain = f'{fs_linux}/conf/Domain.JSON'
domain_data = '''
{
    "NAME": "",
    "DOMAIN_ID": "",
    "KNOWN_MEMBER": ""
}
'''

hosts = f'{fs_linux}/conf/Hosts.JSON'
hosts_data = '''
{
	"NODES": {},
	"SYNC_LEVEL": {}
}
'''

time = f'{fs_linux}/conf/Time.JSON'
time_data = '''
{
    "DEFAULT":
    {
        "NAME": "DEFAULT",
        "SCHEDULE": "MTWTFSS",
        "OPERATOR": "EVERY",
        "FREQUENCY": "1",
        "TIME_UNITY":  "HRS"
    }   
}
'''

# Grava conteudos nos arquivos
files = {   
            conf:conf_data, 
            domain:domain_data, 
            hosts:hosts_data, 
            time:time_data
        }

for conf, data in files.items():
    print(conf)
    if conf != '/etc/file-sync/conf/Domain.JSON':
        _file = open(conf, 'w')
        _file.writelines(data)
        _file.close()