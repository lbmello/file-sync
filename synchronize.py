# Arquivo principal do projeto onde as demais funções são executadas em sequência.
from lib import copy as cp
from lib import json_reader as jreader

# READ THE TIME CONFIG
time_default, time_lab = jreader.json_time_read()

# READ THE GLOBAL CONFIG
global_user, global_time = jreader.json_global_read()

# READ THE HOSTS CONFIG
json_nodes, json_level0, json_level1, json_level2, nodes, level0, level1, level2, ip, description, uid, edge = jreader.json_hosts_read()

# READ THE SHARE CONFIG
share_id, share_name, share_description, share_author, share_enviroment, share_sync_level, share_node, share_source, share_user, share_destiny, share_time = jreader.json_config_read()


# RUN THE SYNC WITH IP ARRAY
for i in range(len(ip)):
    cp.copy_file(share_source,share_user,ip[i],share_destiny)