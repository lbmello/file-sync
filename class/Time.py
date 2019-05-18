import json
import os.path

# RELATIVE PATH DECLARATION
my_path = os.path.abspath(os.path.dirname(__file__))

pathTime = os.path.join(my_path, "../conf/Time.JSON")


class Time:
    def __init__(self, time):
        self.time = time

    with open(pathTime, 'r') as file:
        json_time = json.load(file)

    def default(self):
        time_default = (self.json_time["DEFAULT"])
        return time_default

    def time_lab(self):
        time_lab = (self.json_time["LAB"])
        return(time_lab)