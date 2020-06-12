
import sys

from .filesync import data
from .filesync import enter
# from .filesync import exit
from .filesync import internal
from .filesync.cli import cli
#from .filesync import network
# from .filesync import sync
# from .filesync.api import server
# from .filesync import api


## Envio do argv para o modulo CLI
cli_object = cli(sys.argv)