
import json

class Host:
    """Gravacao do arquivo Hosts.JSON."""

    _pathHost = 'file-sync/conf/Hosts.JSON'

    def __init__(self):
        """Arquivo Hosts.JSON é lido."""
        
        _file = open(Host._pathHost, 'r')
        self.hosts = json.load(_file)
        _file.close()

   
    def set_host(self, name, ip, description, uid, edge):
        data = {
                "IP": f'{ip}',
                "DESCRIPTION": f'{description}',
                "UID": f'{uid}',
                "EDGE": f'{edge}'
                }
        
        self.hosts["NODES"][f"{name}"] = (data)

        _file = open(Host._pathHost, 'w')
        json.dump(self.hosts, fp =_file)
        _file.close()
