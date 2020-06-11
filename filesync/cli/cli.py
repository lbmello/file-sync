
from fnmatch import fnmatch

from ..internal import _sync_objects_

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
        for s in _sync_objects_:
            if argument == s.name:
                s.send_data()

class cli_init(cli):

    def __init__(self, argument):
        ...

class cli_share(cli):

    def __init__(self, argv):
        ...