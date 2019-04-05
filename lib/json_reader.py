# IMPORT JSON CONFIG FILE

import json

# FUNCTION THAT READ THE FILE conf\Config.JSON AND RETURN THE VALUES
def json_config_read():
            
#   READ THE FILE conf\Config.JSON

    with open('conf\Config.JSON', 'r') as file:
        config = json.load(file)
        
#   RECEIVE THE VALIES FROM "GLOBAL" ITEM IN Config.JSON FILE
    global_user = config["GLOBAL"]["USER"]
    return global_user
    
    global_schedule = config["GLOBAL"]["SCHEDULE"]
    return global_schedule 
    
    global_frequency = config["GLOBAL"]["FREQUENCY"]
    return global_frequency
    
      
    # RECEIVE THE VALUES FROM "SHARE" ITEM IN Config.JSON FILE    
    shareId = config["SHARE"]["ID"]
    return shareId
    
    share_name = config["SHARE"]["NAME"]
    return share_name
    
    share_description = config["SHARE"]["DESCRIPTION"]
    return share_description
    
    share_author = config["SHARE"]["AUTHOR"]
    return share_author
    
    share_enviroment = config["SHARE"]["ENVIROMENT"]
    return share_enviroment
    
    share_sync_level = config["SHARE"]["SYNC_LEVEL"]
    return share_sync_level
    
    share_node = config["SHARE"]["NODE"]
    return share_node
    
    share_source = config["SHARE"]["SOURCE"]
    return share_source
    
    share_user = config["SHARE"]["USER"]
    return share_user
    
    share_ip = config["SHARE"]["IP"]
    return share_ip
    
    share_destiny = config["SHARE"]["DESTINY"]
    return share_destiny
    
    share_time = config["SHARE"]["TIME"]
    return share_time
        
# Criar leitura do arquivo Time.JSON 
#return(time_schedule)
#return(time_frequency)
    

# FUNCTION THAT READ THE FILE conf\Hosts.JSON AND RETURN THE VALUES
def json_hosts_read():
    
#   READ THE FILE conf\Hosts.JSON
    with open('conf\Hosts.JSON', 'r') as file:
        hosts = json.load(file)

#   PART THE VALUES OF VARIABLES IN EACH ITEM OS JSON FILE     
    json_nodes = (hosts["NODES"])
    #json_syncLevel = (hosts["SYNC_LEVEL"])
    json_level0 = (hosts["SYNC_LEVEL"]["LEVEL_0"])
    json_level1 = (hosts["SYNC_LEVEL"]["LEVEL_1"])
    json_level2 = (hosts["SYNC_LEVEL"]["LEVEL_2"])
    
#   RETURN THE NAME OF ALL HOSTS USING THE LIST NODES
    nodes = []
    for keys,values in json_nodes.items():
        nodes.append(keys)        
    
#   RETURN THE SYNC LEVEL 0
    level0 = []
    for keys, values in json_level0.items():
        level0.append(values)
    
#   RETURN THE SYNC LEVEL 1
    level1 = []
    for keys, values in json_level1.items():
        level1.append(values)
        
#   RETURN THE SYNC LEVEL 2
    level2 = []
    for keys, values in json_level2.items():
        level2.append(values)
       
json_hosts_read()