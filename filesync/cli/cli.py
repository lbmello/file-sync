
from fnmatch import fnmatch

from ..internal import _sync_objects_
from ..internal import _cron_objs_
from ..internal import _config_objects_
from ..internal import _node_objects_
from ..internal.domain import domain

from ..data.write import Host as write_hosts
from ..data.write import Config as write_config

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

            if parameter[0] == '--host':
                cli_hosts(parameter[1])

            if parameter[0] == '--config':
                cli_config(parameter[1])

            if parameter[0] == '--domain':
                cli_domain(parameter[1])


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


class cli_hosts(cli):

    def __init__(self, argument):
        self.argument = argument

        self.node = write_hosts()

        if self.argument == 'add':
            _hostname = str(input('Informe o Nome do Host: '))
            _ip = str(input('Informe o IP do Host: '))
            _description = str(input('Informe alguma descriçao do Host: '))
            _uid = str(input('Informe o UID do Host: '))
            _edge = ''

            self.node.set_host(name = _hostname,
                                ip = _ip,
                                description = _description,
                                uid = _uid,
                                edge = _edge)


class cli_config(cli):

    def __init__(self, argument):
        self.argument = argument

        self.config = write_config()

        if self.argument == 'add':
            _id = str(input('Informe o ID da config: ')),
            _name = str(input('Informe o nome da config: ')),
            _description = str(input('Informe a descricao: ')),
            _author = str(input('Informe o autor: ')),
            _enviroment = str(input('Informe o ambiente de execucao: ')),
            _sync_level = str(input('Informe o sync level: ')),
            _node = str(input('Informe o tipo de node: ')),
            _source = str(input('Informe o diretorio de origem: ')),
            _user = str(input('Informe o usuario para execucao: ')),
            _destiny = str(input('Informe o diretorio de destino: ')),
            _time = str(input('Informe o padrao de tempo: ')),

            self.config.set_config( id = _id,
                                    name = _name,
                                    description = _description,
                                    author = _author,
                                    enviroment = _enviroment,
                                    sync_level = _sync_level,
                                    node = _node,
                                    source = _source,
                                    user = _user,
                                    destiny = _destiny,
                                    time = _time)

class cli_domain:
    
    def __init__(self, argument):
        self.argument = argument
        self.domain = domain()

        if self.argument == 'create':
            _domain = str(input('Informe o nome do novo domnio: ')),

            self.domain.create_domain(domain_name = _domain)

        if self.argument == 'list':
            print(self.domain.get_domain_id())