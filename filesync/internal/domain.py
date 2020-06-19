
import requests
import platform

from ..enter.domain import domain as enter_domain
from ..data.write.Host import Host as write_host
from ..enter import _node_objects_
from ..internal.localhost import localhost


class domain:

    def __init__(self):
        _enter_domain_obj = enter_domain()
        
        self.name = _enter_domain_obj.name
        self.domain_id = _enter_domain_obj.domain_id
        self.known_member = _enter_domain_obj.known_member
        self.state = _enter_domain_obj.state

        self.join_myself()


    def join_myself(self):
        """ Caso o host no esteja no dominio, envia meus dados 
        ao ip conhecido para juntar-se."""
        
        if self.state != 'JOIN':
            localhost_obj = localhost()
            
            uri = f'http://{self.known_member}:8080/domain/join?domain_id={self.domain_id}&domain_name={self.name}&new_host_ip={localhost_obj.get_ip()}&new_host_description={localhost_obj.get_description()}&new_host_name={localhost_obj.get_name()}'
            
            response = requests.post(uri)

            # TODO: Consolidar valor de JOIN no arquivo de configuracao de domain

            return response            


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
        
        return f'sucesso ao ingressar no dominio.'


    def check_domain(self):
        """ Verifica com os outros membros se o dominio segue valendo."""
        # Talvez acionar validate_domain do outro host
        ...

    
    def validate_domain(self, domain_id, domain_name):
        """ Valida se o domain ID recebido for igual ao domain ID do dominio."""

        if self.state == 'JOIN':
            if domain_id == self.domain_id and domain_name == self.name:
                return (True,'')
            
            else:
                return (False, 'Dados enviados nao coincidem com as credenciais do dominio!')
        return (False, 'Membro nao pertence ao dominio.')
