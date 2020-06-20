
import platform
import requests

from ..data.write.Host import Host as write_host
from ..data.write.Domain import Domain as domain_write
from ..enter import _node_objects_
from ..enter.domain import domain as enter_domain
from ..internal.localhost import localhost
from .misc import random_md5


class domain:
    """Modulo que gerencia as operaçoes entre Dominios."""

    def __init__(self):
        """Incilizador de internal.domain. Le dados de enter.domain."""

        _enter_domain_obj = enter_domain()
        
        self.name = _enter_domain_obj.name
        self.domain_id = _enter_domain_obj.domain_id
        self.known_member = _enter_domain_obj.known_member
        self.state = _enter_domain_obj.state

        if self.state != 'LOCALHOST' or '':
            self.join_myself()
            self._write_domain_file()


    def create_domain(self, domain_name):
        """ Cria dominio de host unico, para aguardar mais conexoes."""

        self.name = domain_name
        self.domain_id = random_md5()
        self.known_member = 'LOCALHOST'
        self.state = 'JOIN'
        
        self._write_domain_file()

        return f'DOMAIN: Dominio {self.name} criado com sucesso.'


    def join_myself(self):
        """ Caso o host no esteja no dominio, envia meus dados 
        ao ip conhecido para juntar-se."""
        
        if self.state != 'JOIN':
            localhost_obj = localhost()
            
            #  self.known_member != 'LOCALHOST'

            if self.known_member != 'LOCALHOST':
                if self.known_member:
                    print('kmember: ', type(self.known_member))
                    uri = f'http://{self.known_member}:8080/domain/join?domain_id={self.domain_id}&domain_name={self.name}&new_host_ip={localhost_obj.get_ip()}&new_host_description={localhost_obj.get_description()}&new_host_name={localhost_obj.get_name()}'
            
                    response = requests.post(uri)

                    return response

                else:
                    return 'DOMAIN: Membro conhecido nao informado.'

            else:
                return 'DOMAIN: Domnio local de host unico criado, nao precisa tentar JOIN em nenhum host.'


    def join_domain(self, new_hostname, new_host_ip, new_host_description):
        """ Faz ingresso do novo membro no domnio."""
        
        write_host_obj = write_host()
        write_host_obj.set_host(name = new_hostname,
                                ip = new_host_ip,
                                description = new_host_description,
                                uid = '',
                                edge = '')
                            
        for node in _node_objects_:
            print(platform.node(),node.name)
            if platform.node() != node.name:
               uri = f'http://{node.ip}:8080/hosts/?hostname={new_host_description}&ip={new_host_ip}&description={new_host_description}'

               response = requests.post(uri)
        
        return f'DOMAIN: Sucesso ao ingressar no dominio.'


    def check_domain(self):
        """ Verifica com os outros membros se o dominio segue valendo."""
        # Talvez acionar validate_domain do outro host
        ...

    
    def validate_domain(self, domain_id, domain_name):
        """ Valida se o domain ID recebido for igual ao domain ID do dominio. Acionado via API."""

        if self.state == 'JOIN':
            if domain_id == self.domain_id and domain_name == self.name:
                return (True,'')
            
            else:
                return (False, 'Dados enviados nao coincidem com as credenciais do dominio!')
        return (False, 'Membro nao pertence ao dominio.')


    def _write_domain_file(self):
        """ Funçao interna, usada para consisir dados no arquivo Domain.JSON."""
        
        domain_write_object = domain_write()
        domain_write_object.set_domain( name = self.name,
                                        domain_id = self.domain_id,
                                        known_member = self.known_member,
                                        state = self.state)
