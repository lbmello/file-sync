import json
import os.path

# RELATIVE PATH DECLARATION
my_path = os.path.abspath(os.path.dirname(__file__))

pathConfig = os.path.join(my_path, "../conf/Config.JSON")


class Config:
        def __init__(self):
                self.share = "SHARE"

        with open(pathConfig, 'r') as file:
                config = json.load(file)

        def id(self):
                id = self.config[self.share]["ID"]
                return id

        def name(self):
                name = self.config[self.share]["NAME"]
                return name

        def descrition(self):
                description =self.config[self.share]["DESCRIPTION"]
                return description

        def author(self):
                author = self.config[self.share]["AUTHOR"]
                return author

        def enviroment(self):
                enviroment = self.config[self.share]["ENVIROMENT"]
                return enviroment

        def sync_level(self):
                sync_level = self.config[self.share]["SYNC_LEVEL"]
                return sync_level

        def node(self):
                node = self.config[self.share]["NODE"]
                return node

        def source(self):
                source = self.config[self.share]["SOURCE"]
                return source

        def user(self):
                user = self.config[self.share]["USER"]
                return user

        def destiny(self):
                destiny = self.config[self.share]["DESTINY"]
                return destiny

        def time(self):
                time = self.config[self.share]["TIME"]
                return time

print(Config().id)