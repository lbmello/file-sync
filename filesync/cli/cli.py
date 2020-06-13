
from fnmatch import fnmatch

from ..internal import _sync_objects_
from ..internal import _cron_objs_
from ..internal import _config_objects_
from ..internal import _node_objects_

from .python3_install import python3_install

class cli():
    
    def __init__(self, argv):
        self.argv = argv
        self.parameters = list()

        self.read_parameters()

        for parameter in self.parameters:
            if parameter[0] == '--sync':
                cli_sync(parameter[1])

            if parameter[0] == '--init':
                cli_init(parameter[1])

            if parameter[0] == '--share':
                cli_share(parameter[1])

            if parameter[0] == '--install':
                cli_install(parameter[1])

            if parameter[0] == '--crontab':
                cli_crontab(parameter[1])


    def read_parameters(self):
        """ Percorre argv, identifica o padrao -- 
        e adiciona a posicao subsquente do argv 
        em dicionario.        
        """

        for index, line in enumerate(self.argv):
            #print(index, line)
            
            if (fnmatch(name=line, pat='--*') == True):
                self.parameters.append((line, self.argv[index + 1]))


class cli_sync(cli):
    
    def __init__(self, argument):
        self.argument = argument
        
        for s in _sync_objects_:

            # Sincroniza um share | --sync NOME_SHARE
            if self.argument == s.name:
                s.send_data()
            
            # Sincroniza todos shares |--sync all
            if self.argument == 'all':
                s.send_data()


class cli_init(cli):

    def __init__(self, argument):
        ...


class cli_share(cli):

    def __init__(self, argument):
        ...


class cli_install(cli):

    def __init__(self, argument):
        self.argument = argument

        if self.argument == 'python3':
            python3_install()


class cli_crontab(cli):
    
    def __init__(self, argument):
        self.argument = argument

        for c in _cron_objs_:
            # Adc uma entrada de crontab | --crontab NOME_SHARE
            if self.argument == c.name:
                c.set_crontab_all(command = f'file-sync --sync {self.argument}')
            
            # Adc todas as tarefas no crontab | --crontab all
            if self.argument == 'all':
                for config in _config_objects_:
                    c.set_crontab_all(command = f'file-sync --sync {config.name}')