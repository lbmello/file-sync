import os

# CÓPIA SIMPLES DE ARQUIVO, USANDO O RSYNC DO LINUX
def copy_file(orig, user, ip, path):
     os.system('rsync -avzh -e ssh %s %s@%s:%s' %(orig, user, ip, path))
     # COMANDO => rsync -avzh /home/share/sync/* vagrant 10.0.0.10 /tmp/rsync/
     #print('rsync -avzh %s %s@%s %s' %(orig, user, ip, path))
     #print("origin", orig)
     #print("user", user)
     #print("ip", ip)
     #print("path", path)