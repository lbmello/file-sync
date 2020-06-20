
# imports projeto
from .server import app
from .client import client

# Import das rotas
from .root import index
from .hosts import hosts, one_host_view
from .config import config_view, one_config_view
from .domain import domain_join

# TODO: Alterar execuçao para webserver
app.run(host='0.0.0.0', port=8080, debug=True)
