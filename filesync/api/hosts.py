"""Modulo responsavel pelas rotas de /hosts/."""

from flask import jsonify

from .server import app
from ..enter import _node_objects_

PREFIX = "/hosts"

# Views

@app.route(f"{PREFIX}", methods=['GET'])
def hosts_view():
    json_file = dict()

    for node in _node_objects_:
        
        json_file[node.name] = ({   f'ip':f'{node.ip}',
                                    f'description' : f'{node.description}',
                                    f'uid' : f'{node.uid}',
                                    f'edge' : f'{node.edge}'
                            })                          

    return json_file


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
            

# Inputs

# TODO: Aplicar logica de post
@app.route(f"/{PREFIX}/insert")
def hosts_input():
    ...
