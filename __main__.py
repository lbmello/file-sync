
import threading

from filesync import data
from filesync import enter
# from filesync import exit
from filesync import internal
from filesync import network
# from filesync import sync
#from filesync.api import server
#from filesync import api

# Variaveis globais para instancia  dos objetos de data
d_host = str()
d_time = str()
d_config = str()
d_domain = str()

# Variaveis globais de data
_nodes_ = None
_sync_levels_ = None
_times_ = None
_global_config_ = None
_share_config_ = None
_domain_ = None

# Variaveis globais de enter
_node_objects_ = None
_sync_level_objects_ = None
_time_objects_ = None
_config_objects_ = None
_domain_objects_ = None

def main_data():
    """Instancias de leitura dos arquivos de dados."""

    d_host = data.Host()
    d_time = data.Time()
    d_config = data.Config()
    d_domain = data.Domain()

    global _nodes_ 
    _nodes_ = d_host.get_nodes()
    
    global _sync_levels_
    _sync_levels_ = d_host.get_sync_level()

    global _times_
    _times_ = d_time.get_times()

    global _global_config_
    _global_config_ = d_config.get_global_config()

    global _share_config_
    _share_config_ = d_config.get_share_config()

    global _domain_
    _domain_ = d_domain.get_domain()
    
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

    global _domain_objects_
    _domain_objects_ = list()

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

    # config.json, item global
    for config in _global_config_:
        line = _global_config_[f'{config}']

        _global_name = _global_config_['NAME']
        _global_description = _global_config_['DESCRIPTION']
        _global_author = _global_config_['AUTHOR']
        _global_enviroment = _global_config_['ENVIROMENT']
        _global_sync_level = _global_config_['SYNC_LEVEL']
        _global_node = _global_config_['NODE']
        _global_source = _global_config_['SOURCE']
        _global_user = _global_config_['USER']
        _global_destiny = _global_config_['DESTINY']
        _global_time = _global_config_['TIME']
    
    # config.json, item share
    for config in _share_config_:
        for _ in config:
            _id_config = config['ID']

            try: config['NAME']
            except KeyError:
                _name = _global_name
            else:
                _name = config['NAME']

            try: config['DESCRIPTION']
            except KeyError:
                _name = _global_description
            else:
                _description = config['DESCRIPTION']
            
            try: config['AUTHOR']
            except KeyError:
                _author = _global_author
            else:
                _author = config['AUTHOR']

            try: config['ENVIROMENT']
            except KeyError:
                _enviroment = _global_enviroment
            else:
                _enviroment = config['ENVIROMENT']

            try: config['SYNC_LEVEL']
            except KeyError:
                _sync_level = _global_sync_level
            else:
                _sync_level = config['SYNC_LEVEL']

            try: config['NODE']
            except KeyError:
                _node = _global_node
            else:
                _node = config['NODE']

            try: config['SOURCE']
            except KeyError:
                _source = _global_source
            else:
                _source = config['SOURCE']

            try: config['USER']
            except KeyError:
                _user = _global_user
            else:
                _user = config['USER']
            
            try: config['DESTINY']
            except KeyError:
                _destiny = _global_destiny
            else:
                _destiny = config['DESTINY']
            
            try: config['TIME']
            except KeyError:
                _time = _global_time
            else:
                _time = config['TIME']
            
        _config_objects_.append(enter.Config(   id_config = _id_config, 
                                                name = _name,
                                                description = _description,
                                                author = _author,
                                                enviroment = _enviroment,
                                                sync_level = _sync_level,
                                                node = _node,
                                                source = _source,
                                                user = _user,
                                                destiny = _destiny,
                                                time = _time))

    # domain.json, todos os itens    
    for dom in _domain_:
        line = _domain_[f'{dom}']

        _domain_objects_.append(enter.domain())


def main_internal():
    # TODO: Passar usuário da tarefa
    for time in _time_objects_:
        internal.cron(time_obj=time, user='vagrant')

def main_sync():
    ...

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
    #main_internal()
