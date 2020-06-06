"""Inicializador do pacote internal."""

"""Classe ira gerenciar as interações com o SO, como leitura de dados em pastas."""

# Modulos internos
from .cron import cron
from .folder import folder
from .changes import Changes
from .ssh import Ssh
from .tree import Tree

# Variaveis globais
from ..enter import _time_objects_
from ..enter import _config_objects_

## Operacao na cron

# Limpa crontab do usuario antes da execucao
cron.clear_crontab()

_cron_objs_ = list()
_folder_objects_ = list()

for time in _time_objects_:
    for config in _config_objects_:

        if time.name == config.time:
            # Instancia de cron
            cron_object = cron( time_obj = time, user = config.user)
            cron_object.set_crontab_all(command = f'file-sync share {config.name} sync')
            
            _cron_objs_.append(cron_object)

## Alteracoes


for config in _config_objects_:
    # Instancia de folder
    folder_object = folder(config.source)

    _folder_objects_.append(folder_object)

    
