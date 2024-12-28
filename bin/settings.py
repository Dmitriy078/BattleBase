class Settings:
    def __init__(self):
        self.resolution = (800, 600)
        self.fps = 60
        self.load_settings()

    def load_settings(self):
        with open("data/settings.csv", encoding="utf-8") as file:
            strings = file.readlines()

            for string in strings:
                key, value = string.split(";")

                if key == "resolution":
                    self.resolution = tuple(map(int, value.split(',')))
                elif key == "fps":
                    self.fps = int(value)

    def save_settings(self,):
        pass
