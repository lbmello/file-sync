"""Cliente que envia dados aos demais hosts."""

import json
import requests

from ..data.Config import Config
from ..data.Host import Host
from ..data.Time import Time

class client:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send_config(self):
        _config = Config()
        
        data_json = json.dumps(_config.config)
        payload = {'json_payload': data_json}

        #requests.post(f'http://{self.host}:{self.port}/config/post/', data=payload)

        url = f'http://{self.host}:{self.port}/config/post/'

        headers= {}

        response = requests.request("POST", url, headers=headers, data = payload)

        print(response.text.encode('utf8'))


    def send_hosts(self):
        _hosts = Host()

        data_json = json.dumps(_hosts.hosts)
        payload = {'json_payload': data_json}

        requests.get(f'http://{self.host}:{self.port}', data=payload)


    def send_time(self):
        _time = Time()

        data_json = json.dumps(_time.time)
        payload = {'json_payload': data_json}

        requests.get(f'http://{self.host}:{self.port}', data=payload)
