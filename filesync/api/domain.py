"""Modulo responsavel pelas rotas de /domain/."""

from flask import request
import json

from .server import app
from ..enter import _domain_objects_
from ..internal import dom


PREFIX = "/domain"

@app.route(f"{PREFIX}/join", methods=['POST'])
def domain_join():
    """Rotas de /domain.

    POST, Recebe dados e verifica se os valores sao validos
    para o ingresso.
        domain_name,
        domain_id,
        new_host_ip,
        new_host_description,
        new_hostname,
    """

    if request.method == 'POST':
        _domain_name = request.args.get('domain_name')
        _domain_id = request.args.get('domain_id')
        _new_host_ip = request.args.get('new_host_ip')
        _new_host_description = request.args.get('new_host_description')
        _new_hostname = request.args.get('new_host_name')

        internal_domain_obj = dom

        test_domain, reason = internal_domain_obj.validate_domain(  domain_id = _domain_id,
                                                                    domain_name = _domain_name)


        if test_domain == True:                                           
            join_domain = internal_domain_obj.join_domain(  new_host_ip = _new_host_ip,
                                                            new_host_description = _new_host_description,
                                                            new_hostname = _new_hostname)
            return join_domain

        else:
            return reason