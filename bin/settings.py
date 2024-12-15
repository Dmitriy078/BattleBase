import csv
class Settings:
    def __init__(self):
        self.load_settings()

    def load_settings(self):
        with open("../data/settings.csv", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=';')
            reader = list(reader)

        self.resolution = (reader[1], reader[2])


    def save_settings(self, ):
        pass
