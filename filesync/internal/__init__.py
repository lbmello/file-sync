"""Inicializador do pacote internal."""

import sys

# Modulos internos
from .cron import cron
from .folder import folder
from .changes import Changes
#from .ssh import Ssh
#from .tree import Tree
from .sync import sync
from .domain import domain
from .localhost import localhost

# Variaveis globais
from ..enter import _time_objects_
from ..enter import _config_objects_
from ..enter import _node_objects_

## Operacao na cron

# Limpa crontab do usuario antes da execucao
cron.clear_crontab()

_cron_objs_ = list()
_folder_objs_ = list()
_sync_objects_ = list()

for time in _time_objects_:
    for config in _config_objects_:

        if time.name == config.time:
            # Instancia de cron
            cron_object = cron(time_obj=time, user=config.user, name=config.name)
            cron_object.set_crontab_all(command = f'file-sync --sync {config.name}')
            
            _cron_objs_.append(cron_object)

## Alteracoes

for config in _config_objects_:
    # Instancia de folder
    folder_object = folder(source = config.source)
    _folder_objs_.append(folder_object)

    # Instancia de Changes
    changes_object = Changes(source = config.source)
    changes_object.get_actual_state()

    # Instancia de sync
    for hst in _node_objects_:
        sync_object = sync( name = config.name,
                            source = config.source,
                            destiny = config.destiny, 
                            user = config.user,
                            ip = hst.ip)

        _sync_objects_.append(sync_object)

# Domain
dom = domain()