
import json

class Config:
    """Gravacao do arquivo Config.JSON."""

    _pathConfig = 'file-sync/conf/Config.JSON'

    def __init__(self):
        """Arquivo Config.JSON é lido."""
        
        _file = open(Config._pathConfig, 'r')
        self.config = json.load(_file)
        _file.close()

   
    def set_config(self, id, name, description, author, enviroment, sync_level, node, source, user, destiny, time):

        data =  {"ID": str(id),
                "NAME": name,
                "DESCRIPTION": description,
                "AUTHOR": author,
                "ENVIROMENT": enviroment,
                "SYNC_LEVEL": sync_level,
                "NODE": node,
                "SOURCE": source,
                "USER": user,
                "DESTINY": destiny,
                "TIME": time}
        
        self.config["SHARE"].append(data)

        _file = open(Config._pathConfig, 'w')
        json.dump(self.config, fp =_file)
        _file.close()
