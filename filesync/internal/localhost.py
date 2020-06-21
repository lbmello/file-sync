""" Identifica se o arquivo de hosts tem a entrada de localhost,
caso nao, cria esta entrada. devera ser executado por join_myself
de internal.domain."""

import socket

from ..data.write import Host as write_host
from ..enter import _node_objects_

class localhost:
    """ Classe responsavel pela criaçao do registro de localhost em Hosts.JSON."""

    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.name = 'localhost'
        self.description = 'maquina_local'

        self._set_hostname()


    def _set_hostname(self):
        """ Percorre lista dos nodes e cria localhost, caso nao exista."""

        if not _node_objects_:
            write_host_object = write_host()
            write_host_object.set_host( name = self.name,
                                        ip = self.ip,
                                        description = self.description,
                                        uid = '000',
                                        edge = '')

            return f'LOCALHOST: Registro de localhost inserido em Hosts.JSON.' 

        else:
            for node in _node_objects_: 
                if 'localhost' != node.name:
                    write_host_object = write_host()
                    write_host_object.set_host( name = self.name,
                                        ip = self.ip,
                                        description = self.description,
                                        uid = '000',
                                        edge = '')
                
                    return f'LOCALHOST: Ja existem dados no arquivo de hosts, registro de localhost inserido em Hosts.JSON.' 

            else:

                return f'LOCALHOST: Registro de localhost ja existe em Hosts.JSON.'


    def get_ip(self):
        """ Retorna ip da inteface de rede do localhost (nao da loopback)."""

        return self.ip

    
    def get_name(self):
        """ Retorna nome padrao do localhost."""

        return self.name


    def get_description(self):
        """ Retorna descricao do localhost."""

        return self.description