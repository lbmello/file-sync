import os

# CÓPIA SIMPLES DE ARQUIVO, USANDO O RSYNC DO LINUX
def cp_rsync(orig, user, ip, path):
     os.system('rsync -avzh %s %s@%s:%s' %(orig, user, ip, path))

'''# VARIAVEIS DE TESTE PASSADAS AO MÉTODO, POSTERIORMENTE SERÃO INCLUSAS NO CÓDIGO LENDO DE UM ARQUIVO XML/JSON
test_orig = '/home/share/sync/*'
test_user = 'vagrant'
test_ip = '192.168.15.10'
test_path = '/tmp/rsync/
'''

#cp_rsync(test_orig,test_user,test_ip,test_path)