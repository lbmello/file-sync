""" Identifica se o arquivo de hosts tem a entrada de localhost,
caso nao, cria esta entrada. devera ser executado por join_myself
de internal.domain."""

import socket

from ..data.write import Host as write_host

class localhost:

    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.name = 'localhost'
        self.description = 'maquina_local'

        write_host_object = write_host()
        write_host_object.set_host( name = self.name,
                                    ip = self.ip,
                                    description = self.description,
                                    uid = '000',
                                    edge = '')
        print('localhost criado')

    def get_ip(self):
        """ Retorna ip da inteface de rede do localhost (nao da loopback)."""

        return self.ip

    
    def get_name(self):
        """ Retorna nome padrao do localhost."""

        return self.name


    def get_description(self):
        """ Retorna descricao do localhost."""

        return self.description