"""Modulo responsavel pelas rotas de /config/."""

from flask import jsonify

from .server import app
from ..enter import _config_objects_

PREFIX = "/config"

# Views

@app.route(f"{PREFIX}", methods=['GET'])
def config_view():
    """Retorna todas as tarefas de sincronia."""

    json_file = dict()

    for config in _config_objects_:
        
        json_file[config.name] = ({
                                    f'id' : config.id,
                                    f'name' : config.name,
                                    f'description' : config.description,
                                    f'author' : config.author,
                                    f'enviroment' : config.enviroment,
                                    f'sync_level' : config.sync_level,
                                    f'node' : config.node,
                                    f'source' : config.source,
                                    f'user' : config.user,
                                    f'destiny' : config.destiny,
                                    f'time' : config.time
                                })

    return json_file


@app.route(f"/{PREFIX}/task/<string:name>", methods=['GET'])
def one_config_view(name):
    """Retorna somente a tarefa de sincronia solicitada."""

    json_file = dict()

    for config in _config_objects_:
        
        json_file[config.name] = ({
                                    f'id' : config.id,
                                    f'name' : config.name,
                                    f'description' : config.description,
                                    f'author' : config.author,
                                    f'enviroment' : config.enviroment,
                                    f'sync_level' : config.sync_level,
                                    f'node' : config.node,
                                    f'source' : config.source,
                                    f'user' : config.user,
                                    f'destiny' : config.destiny,
                                    f'time' : config.time
                                })                       

        if config.name == name:
            return (json_file[config.name], 200)
    
    return ('Valor nao encontrado', 404)


# Inputs