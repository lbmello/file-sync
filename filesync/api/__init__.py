
from .server import app
from .client import client

from .root import index
from .hosts import hosts_input, hosts_view

# Execucao do servidor, na porta 8080
app.run(host='0.0.0.0', port=8080, debug=True)
