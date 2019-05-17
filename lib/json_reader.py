# IMPORT JSON CONFIG FILE

import json
import os.path

# RELATIVE PATH DECLARATION
my_path = os.path.abspath(os.path.dirname(__file__))

pathHost = os.path.join(my_path, "../conf/Hosts.JSON")
pathConfig = os.path.join(my_path, "../conf/Config.JSON")
pathTime = os.path.join(my_path, "../conf/Time.JSON")


# FUNCTION THAT READ READ AND RETURN self.share VALUES FROM THE FILE conf\Config.JSON
class Config:
        def __init__(self, share):
                self.share = share

        with open(pathConfig, 'r') as file:
                config = json.load(file)

        def id(self):
                id = self.config[self.share]["ID"]
                return id

        def name(self):
                name = self.config[self.share]["NAME"]
                return name

        def descrition(self):
                description =self. config[self.share]["DESCRIPTION"]
                return description

        def author(self):
                author = self.config[self.share]["AUTHOR"]
                return author

        def enviroment(self):
                enviroment = self.config[self.share]["ENVIROMENT"]
                return enviroment

        def sync_level(self):
                sync_level = self.config[self.share]["SYNC_LEVEL"]
                return sync_level

        def node(self):
                node = self.config[self.share]["NODE"]
                return node

        def source(self):        
                source = self.config[self.share]["SOURCE"]
                return source

        def user(self):        
                user = self.config[self.share]["USER"]
                return user

        def destiny(self):              
                destiny = self.config[self.share]["DESTINY"]
                return destiny

        def time(self):        
                time = self.config[self.share]["TIME"]
                return time
                
# FUNCTION THAT READ THE FILE conf\Hosts.JSON AND RETURN THE VALUES
class Hosts:
        def __init__(self, hosts):
                self.hosts = hosts

        with open(pathHost, 'r') as file:
                hosts = json.load(file)

        def nodes(self):
                #PART THE VALUES OF VARIABLES IN EACH ITEM OS JSON FILE     
                nodes = (hosts["NODES"])
                return nodes

        def level0(self):   
                level0 = (hosts["SYNC_LEVEL"]["LEVEL_0"])
                return level0

        def level1(self):
                level1 = (hosts["SYNC_LEVEL"]["LEVEL_1"])
                return level1

        def level2(self):
                level2 = (hosts["SYNC_LEVEL"]["LEVEL_2"])
                return level2

        # RETURN THE NAME OF ALL HOSTS USING THE LIST NODES
        nodes = []
        for keys,values in json_nodes.items():
            nodes.append(keys)        
        
        # RETURN THE SYNC LEVEL 0
        level0 = []
        for keys, values in json_level0.items():
            level0.append(values)
        
        # RETURN THE SYNC LEVEL 1
        level1 = []
        for keys, values in json_level1.items():
            level1.append(values)

        # RETURN THE SYNC LEVEL 2
        level2 = []
        for keys, values in json_level2.items():
            level2.append(values)

        # RETURN THE IP ADDRESSES
        nodesKeys = []
        ip = []
        description = []
        uid = []
        edge = []
        
        # READ THE NODES AND PUT THEM IN A LIST
        nodes_keys = json_nodes.keys()
        for i in range (len(nodes_keys)):
                temp_var = list(nodes_keys)[i]
                nodesKeys.append(temp_var)

        # READ THE NODES ITEMS
        for i in range (len(nodesKeys)):
                # IP
                hostsIp = (hosts["NODES"][nodesKeys[i]]["IP"])
                ip.append(hostsIp)
                # DESCRIPTION
                hostDescription = (hosts["NODES"][nodesKeys[i]]["DESCRIPTION"])
                description.append(hostDescription)
                # UID
                hostUid = (hosts["NODES"][nodesKeys[i]]["UID"])
                uid.append(hostUid)
                # EDGE
                hostEdge = (hosts["NODES"][nodesKeys[i]]["EDGE"])
                edge.append(hostEdge)

        return(json_nodes, json_level0, json_level1, json_level2, nodes, level0, level1, level2, ip, description, uid, edge)
        

# FUNCTION THAT READ THE FILE conf\Time.JSON AND RETURN THE VALUES
def json_time_read():
        with open(pathTime, 'r') as file:
                time = json.load(file)

        time_default = (time["DEFAULT"])

        time_lab = (time["LAB"])
    
        return(time_default, time_lab)

     
# FUNCTION THAT RETURN THE VALUES FROM "GLOBAL" ITEM IN Config.JSON FILE
def json_global_read():

        with open(pathConfig, 'r') as file:
                config = json.load(file)        

        global_user = config["GLOBAL"]["USER"]
        
        global_time = config["GLOBAL"]["TIME"]
        
        return (global_user, global_time)