# Arquivo principal do projeto onde as demais funções são executadas em sequência.
from lib import copy as cp

cp.copy_file('/home/share/sync/*','vagrant','192.168.15.10','/tmp/rsync/')