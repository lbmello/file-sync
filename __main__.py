
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

    global _nodes_ 
    _nodes_ = d_host.get_nodes()
    
    global _sync_levels_
    _sync_levels_ = d_host.get_sync_level()

    global _times_
    _times_ = d_time.get_times()
    
def main_enter():
    """ Declaracao dos objetos dos itens lidos em main_data."""

    global _node_objects_
    _node_objects_ = list()
    
    global _sync_level_objects_
    _sync_level_objects_ = list()

    global _time_objects_ 
    _time_objects_ = list()
    
    global _config_objects_ 
    _config_objects_ = list()

    # hosts.json, item NODES
    for node in _nodes_:
        line = (_nodes_[f'{node}'])
        
        _name = node
        _ip = (line['IP'])
        _description = (line['DESCRIPTION'])
        _uid = (line['UID'])
        _edge = (line['EDGE'])

        # Append
        _node_objects_.append(enter.Node( name = _name,
                                        ip = _ip, 
                                        description = _description, 
                                        uid = _uid, 
                                        edge = _edge))

    # hosts.json, item SYNC_LEVEL    
    for level in _sync_levels_:
        line = (_sync_levels_[f'{level}'])

        _members_uid = (line['UID'])

        # Append
        _sync_level_objects_.append(enter.sync_level( level = level, 
                                                    uid_members = _members_uid))

    # time.json, todos os itens
    for time in _times_:
        line = (_times_[f'{time}'])
        _time_objects_.append(enter.Time(time_data = line))

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
    for node in _nodes_:
        print(node)
        #nw = network.host_alive(f'{node.}')

if __name__ == "__main__":
    main_data()
    main_enter()