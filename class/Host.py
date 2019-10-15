''' Classe criada para gerenciamento dos Hosts, lidos no arquivo Hosts.JSON '''
from Network import Network
from os import path
from json import load


class Host(Network):

    def __init__(self):
        ''' Metodo Construtor da Classe '''

        # RELATIVE PATH DECLARATION
        my_path = path.abspath(
            path.dirname(__file__))

        pathHost = path.join(
            my_path, "../conf/Hosts.JSON")

        with open(pathHost, 'r') as file:
            hosts = load(file)

            json_nodes = (hosts["NODES"])

            print(json_nodes)
