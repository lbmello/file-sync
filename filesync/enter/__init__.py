"""Inicializador do pacote enter."""

from .Node import Node
from .Time import Time
from .sync_level import sync_level
from .Config import Config
from .domain import domain

from ..data import _nodes_, _sync_levels_, _times_, _global_config_, _share_config_, _domain_

# Variaveisglobais de Enter
_node_objects_ = list()
_sync_level_objects_ = list()
_time_objects_ = list()
_config_objects_ = list()
_domain_objects_ = list()

def main():
    global _node_objects_

    global _sync_level_objects_

    global _time_objects_ 

    global _config_objects_ 

    global _domain_objects_

    # hosts.json, item NODES
    for node in _nodes_:
        line = (_nodes_[f'{node}'])
        
        _name = node
        _ip = (line['IP'])
        _description = (line['DESCRIPTION'])
        _uid = (line['UID'])
        _edge = (line['EDGE'])

        # Append
        _node_objects_.append(Node( name = _name,
                                        ip = _ip, 
                                        description = _description, 
                                        uid = _uid, 
                                        edge = _edge))

    # hosts.json, item SYNC_LEVEL    
    for level in _sync_levels_:
        line = (_sync_levels_[f'{level}'])

        _members_uid = (line['UID'])

        # Append
        _sync_level_objects_.append(sync_level( level = level, 
                                                    uid_members = _members_uid))

    # time.json, todos os itens
    for time in _times_:
        line = (_times_[f'{time}'])
        _time_objects_.append(Time(time_data = line))

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
            
        _config_objects_.append(Config(   id_config = _id_config, 
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

        _domain_objects_.append(domain())



main()