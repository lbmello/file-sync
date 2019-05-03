# IMPORT JSON CONFIG FILE

import json

# FUNCTION THAT READ READ AND RETURN "SHARE" VALUES FROM THE FILE conf\Config.JSON
def json_config_read():      
    with open('conf/Config.JSON', 'r') as file:
        config = json.load(file)
      
        share_id = config["SHARE"]["ID"]
    
        share_name = config["SHARE"]["NAME"]
        
        share_description = config["SHARE"]["DESCRIPTION"]
        
        share_author = config["SHARE"]["AUTHOR"]
        
        share_enviroment = config["SHARE"]["ENVIROMENT"]
        
        share_sync_level = config["SHARE"]["SYNC_LEVEL"]
        
        share_node = config["SHARE"]["NODE"]
        
        share_source = config["SHARE"]["SOURCE"]
        
        share_user = config["SHARE"]["USER"]
                
        share_destiny = config["SHARE"]["DESTINY"]
        
        share_time = config["SHARE"]["TIME"]
        
        return (share_id, share_name, share_description, share_author, share_enviroment, share_sync_level, share_node, share_source, share_user, share_destiny, share_time)
    

# FUNCTION THAT READ THE FILE conf\Hosts.JSON AND RETURN THE VALUES
def json_hosts_read():
        with open('conf/Hosts.JSON', 'r') as file:
                hosts = json.load(file)

        #PART THE VALUES OF VARIABLES IN EACH ITEM OS JSON FILE     
        json_nodes = (hosts["NODES"])
        #json_syncLevel = (hosts["SYNC_LEVEL"])
        json_level0 = (hosts["SYNC_LEVEL"]["LEVEL_0"])
    
        json_level1 = (hosts["SYNC_LEVEL"]["LEVEL_1"])
    
        json_level2 = (hosts["SYNC_LEVEL"]["LEVEL_2"])
    
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
        with open('conf/Time.JSON', 'r') as file:
                time = json.load(file)

        time_default = (time["DEFAULT"])

        time_lab = (time["LAB"])
    
        return(time_default, time_lab)
     
     
     
     
# FUNCTION THAT RETURN THE VALUES FROM "GLOBAL" ITEM IN Config.JSON FILE
def json_global_read():

        with open('conf/Config.JSON', 'r') as file:
                config = json.load(file)        

        global_user = config["GLOBAL"]["USER"]
        
        global_time = config["GLOBAL"]["TIME"]
        
        return (global_user, global_time)