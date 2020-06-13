"""Modulo responsavel pelas rotas de /."""

import markdown
import os

from .server import app
from ..enter import _node_objects_

@app.route("/")
def index():
    """ Retorna documentacao do projeto."""

    with open(os.path.dirname(app.root_path) + '/fs.md', "r") as markdown_file:

        content = markdown_file.read()

        return markdown.markdown(content)

