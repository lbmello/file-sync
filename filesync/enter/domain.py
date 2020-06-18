
from ..data.Domain import Domain

class domain:

    def __init__(self):
        data_obj = Domain()
        self.domain_data = data_obj.get_domain()
        
        self.name = self.domain_data['NAME']
        self.domain_id = self.domain_data['DOMAIN_ID']
        self.known_member = self.domain_data['KNOWN_MEMBER']
        self.state = None
    