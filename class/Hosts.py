import json
import os.path

# RELATIVE PATH DECLARATION
my_path = os.path.abspath(os.path.dirname(__file__))

pathHost = os.path.join(my_path, "../conf/Hosts.JSON")


class Hosts:
        def __init__(self, host):
            self.hosts = host

        with open(pathHost, 'r') as file:
            hosts = json.load(file)

        nodes = (hosts["NODES"])
        level0 = (hosts["SYNC_LEVEL"]["LEVEL_0"])
        level1 = (hosts["SYNC_LEVEL"]["LEVEL_1"])
        level2 = (hosts["SYNC_LEVEL"]["LEVEL_2"])
        level3 = (hosts["SYNC_LEVEL"]["LEVEL_4"])
        level4 = (hosts["SYNC_LEVEL"]["LEVEL_5"])

        def full_nodes(self,):
            full_nodes = self.nodes
            return full_nodes        

        # RETORNA OS DADOS DE CADA SYNC LEVEL EM FORMA DE LISTA
        def nodes_list(self):
            nodes_list = []
            for keys, values in self.nodes.items():
                nodes_list.append(keys)  
            return nodes_list      
        
        # RETORNA OS VALORES DO SYNC_LEVEL 0
        def level0_list(self):
            level0_list = []
            for keys, values in self.level0.items():
                level0_list.append(values)
            return level0_list
                
        # RETORNA OS VALORES DO SYNC_LEVEL 1
        def level1_list(self):
            level1_list = []
            for keys, values in self.level1.items():
                level1_list.append(values)
            return level1_list

        # RETORNA OS VALORES DO SYNC_LEVEL 2
        def level2_list(self):
            level2_list = []
            for keys, values in self.level2.items():
                level2_list.append(values)
            return level2_list

        # RETORNA OS VALORES DO SYNC_LEVEL 3
        def level3_list(self):
            level3_list = []
            for values in self.level3.items():
                level3_list.append(values)
            return level3_list

        # RETORNA OS VALORES DO SYNC_LEVEL 4
        def level4_list(self):
            level4_list = []
            for values in self.level4.items():
                level4_list.append(values)
            return level4_list

        # RETORNA O ENDEREÇO IP
        '''nodesKeys = []
        ip = []
        description = []
        uid = []
        edge = []
        
        # LÊ OS NODES E OS COLOCA EM UMA LISTA
        nodes_items = nodes_items()
        nodes_keys = nodes_list.keys()
        for i in range (len(nodes_keys)):
                temp_var = list(nodes_keys)[i]
                nodesKeys.append(temp_var)

        # LÊ OS NODE_ITEMS
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
                edge.append(hostEdge)'''

        #return(json_nodes, json_level0, json_level1, json_level2, nodes, level0, level1, level2, ip, description, uid, edge)