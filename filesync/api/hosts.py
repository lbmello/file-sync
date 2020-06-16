"""Modulo responsavel pelas rotas de /hosts/."""

from flask import request
import json

from .server import app
from ..enter import _node_objects_
from ..data.write import Host as write_hosts

PREFIX = "/hosts/"

# Views

@app.route(f"{PREFIX}", methods=['GET', 'POST'])
def hosts():
    """Rotas de /hosts.

    GET, Visualiza toda colecao existente em Hosts.JSON
    POST, Adiciona novo host em Hosts.JSON. Paramentros:
        hostname,
        ip,
        description,
        uid,
    """

    if request.method == 'GET':
        json_file = dict()

        for node in _node_objects_:
            
            json_file[node.name] = ({   f'ip':f'{node.ip}',
                                        f'description' : f'{node.description}',
                                        f'uid' : f'{node.uid}',
                                        f'edge' : f'{node.edge}'
                                })                          

        return json_file

    if request.method == 'POST':
        node = write_hosts()

        _hostname = str(request.args.get('hostname'))
        _ip = str(request.args.get('ip'))
        _description = str(request.args.get('description'))
        _uid = str(request.args.get('uid'))
        _edge = ''

        node.set_host(  name = _hostname,
                        ip = _ip,
                        description = _description,
                        uid = _uid,
                        edge = _edge)

        return f'registro do host {_hostname} criado com sucesso', 200


@app.route(f"/{PREFIX}/hostname/<name>", methods=['GET'])
def one_host_view(name):
    """Retorna somente o host solicitado."""

    json_file = dict()

    for node in _node_objects_:

            json_file[node.name] = ({   f'ip':f'{node.ip}',
                                        f'description' : f'{node.description}',
                                        f'uid' : f'{node.uid}',
                                        f'edge' : f'{node.edge}'
                                })                          

            if node.name == name:
                return (json_file[node.name], 200)
    
    return ('Valor nao encontrado', 404)
