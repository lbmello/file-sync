
from ..data.Host import Host


class Node():

    def __init__(self, name=str,ip=str, description=str, uid=int, edge=str):
        
        self.name = name 
        self.ip = ip
        self.description = description
        self.uid = uid
        self.edge = edge

if __name__ == "__main__":
    pass
