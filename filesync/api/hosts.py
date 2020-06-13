"""Modulo responsavel pelas rotas de /hosts/."""

from flask import jsonify

from .server import app
from ..enter import _node_objects_


@app.route("/hosts/")
def hosts_view():
    json_file = dict()

    for index, node in enumerate(_node_objects_):
        
        json_file[index] = ({   f'name':f'{node.name}',
                                f'ip':f'{node.ip}',
                                f'description' : f'{node.description}',
                                f'uid' : f'{node.uid}',
                                f'edge' : f'{node.edge}'
                            })                          

    return json_file

@app.route("/hosts/insert")
def hosts_input():
    json_file = dict()

    for index, node in enumerate(_node_objects_):
        
        json_file[index] = ({   f'name':f'{node.name}',
                                f'ip':f'{node.ip}',
                                f'description' : f'{node.description}',
                                f'uid' : f'{node.uid}',
                                f'edge' : f'{node.edge}'
                            })                          

    return json_file