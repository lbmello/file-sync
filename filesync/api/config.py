"""Modulo responsavel pelas rotas de /config/."""

from flask import request

from .server import app
from ..enter import _config_objects_

from ..data.write import Config as write_config

PREFIX = "/config"


@app.route(f"{PREFIX}", methods=['GET','POST'])
def config_view():
    """Retorna todas as tarefas de sincronia."""

    json_file = dict()

    if request.method == 'GET':
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

        return json_file, 200

    if request.method == 'POST':
        config = write_config()

        _id = str(request.args.get('id')),
        _name = str(request.args.get('name')),
        _description = str(request.args.get('description')),
        _author = str(request.args.get('author')),
        _enviroment = str(request.args.get('enviroment')),
        _sync_level = str(request.args.get('sync_level')),
        _node = str(request.args.get('node')),
        _source = str(request.args.get('source')),
        _user = str(request.args.get('user')),
        _destiny = str(request.args.get('destiny')),
        _time = str(request.args.get('time'))


        config.set_config(  id = _id,
                            name = _name,
                            description = _description,
                            author = _author,
                            enviroment = _enviroment,
                            sync_level = _sync_level,
                            node = _node,
                            source = _source,
                            user = _user,
                            destiny = _destiny,
                            time = _time)

        return f'registro de configuraçao {_name} criado com sucesso', 200


@app.route(f"/{PREFIX}/task/<string:name>", methods=['GET'])
def one_config_view(name):
    """Retorna somente a tarefa de sincronia solicitada."""

    json_file = dict()

    if request.method == 'GET':
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