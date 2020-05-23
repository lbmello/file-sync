
import threading

from filesync import data
from filesync import enter
# from filesync import exit
from filesync import internal
from filesync import network
# from filesync import sync
#from filesync.api import server
#from filesync import api



def main_data():
    """Instancias de leitura dos arquivos de dados."""

    d_host = data.Host()
    d_time = data.Time()
    d_config = data.Config()

    global nodes 
    nodes = d_host.get_nodes()
    
    global sync_levels
    sync_levels = d_host.get_sync_level()

    global _times_
    _times_ = d_time.get_times()
    
def main_enter():
    """ Declaracao dos objetos dos itens lidos em main_data."""

    global node_objects
    node_objects = list()
    
    global sync_level_objects
    sync_level_objects = list()

    global time_objects 
    time_objects = list()
    
    global config_objects 
    config_objects = list()

    # hosts.json, item NODES
    for node in nodes:
        line = (nodes[f'{node}'])
        
        _name = node
        _ip = (line['IP'])
        _description = (line['DESCRIPTION'])
        _uid = (line['UID'])
        _edge = (line['EDGE'])

        # Append
        node_objects.append(enter.Node( name = _name,
                                        ip = _ip, 
                                        description = _description, 
                                        uid = _uid, 
                                        edge = _edge))

    # hosts.json, item SYNC_LEVEL    
    for level in sync_levels:
        line = (sync_levels[f'{level}'])

        _members_uid = (line['UID'])

        # Append
        sync_level_objects.append(enter.sync_level( level = level, 
                                                    uid_members = _members_uid))

    # time.json, todos os itens
    for time in _times_:
        line = (_times_[f'{time}'])
        time_objects.append(enter.Time(time_data = line))

    # TODO: CRIAR MESMA LOGICA PARA CONFIG

def main_internal():
    ...
    #ch = internal.Changes('001')
    #print(ch.get_actual_state())

def _flask_server(ip):
    ...
    '''server.app.run( host=ip,
                    port='5000',
                    debug=False)'''

def main_api():
    ...
    #_flask_server('0.0.0.0')

    #cl = api.client(host='192.168.0.101', port=5000)
    #cl.send_config()

def main_network():
    for node in nodes:
        print(node)
        #nw = network.host_alive(f'{node.}')

if __name__ == "__main__":
    main_data()
    main_enter()