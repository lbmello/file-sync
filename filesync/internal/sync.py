
import subprocess

class sync:
    def __init__(self, name, source, destiny, user, ip):
        self.name = name
        self.source = source
        self.destiny = destiny
        self.user = user
        self.ip = ip


    def send_data(self):
        cmd = f'rsync -az {self.source} {self.user}@{self.ip}:{self.destiny}'
        print(cmd)
        #status, output = subprocess.getstatusoutput(cmd)

        #print('status ', status)
        #print('output ', output)