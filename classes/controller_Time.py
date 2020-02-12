
from classes.model_Time import Time


class controller_Time():

    def __init__(self):
        self.time = Time()


    def format_date(self):
        print(self.time)

if __name__ == "__main__":
    teste = controller_Time()
    teste.format_date()

