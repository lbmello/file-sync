
import json

class Domain:
    """Gravacao do arquivo Domain.JSON."""

    _pathDomain = 'file-sync/conf/Domain.JSON'

    def __init__(self):
        """Modulo responsavel por gravar dados em Domain.JSON."""
        
        _file = open(Domain._pathDomain, 'r')
        self.domain = json.load(_file)
        _file.close()

   
    def set_domain(self, name, domain_id, known_member, state):
        data = {
                "NAME": f'{name}',
                "DOMAIN_ID": f'{domain_id}',
                "KNOWN_MEMBER": f'{known_member}',
                "STATE": f'{state}'
                }
        
        self.domain = (data)

        _file = open(Domain._pathDomain, 'w')
        json.dump(self.domain, fp =_file)
        _file.close()
