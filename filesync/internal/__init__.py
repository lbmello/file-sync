"""Inicializador do pacote internal."""

"""Classe irá gerenciar as interações com o SO, como leitura de dados em pastas."""

from .changes import Changes
from .tree import Tree
from .ssh import Ssh
from .cron import cron

from ..enter import _time_objects_
from ..enter import _config_objects_

_cron_objs_ = list()

for time in _time_objects_:
    for config in _config_objects_:

        if time.name == config.time:
            # Instancia de Cron
            cron_object = (cron( time_obj = time, user = config.user))

            cron_object.set_crontab_all(command = '/bin/echo meu_ovo')

            _cron_objs_.append(cron_object)