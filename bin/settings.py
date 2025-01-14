class Settings:
    def __init__(self):
        self.full_screen_mode = False
        self.resolution = (800, 600)
        self.w, self.h = self.resolution
        self.fps = 60
        self.cell_size = (self.resolution[0] // 12.5, self.resolution[1] // 9.375)
        self.load_settings()

    def load_settings(self):
        with open("data/settings.csv", encoding="utf-8") as file:
            strings = file.readlines()

            for string in strings:
                key, value = string.replace('\n', '').split(";")

                if key == "resolution":
                    self.resolution = tuple(map(int, value.split(',')))
                    self.w, self.h = self.resolution
                    self.cell_size = (self.resolution[0] // 12.5, self.resolution[1] // 9.375)
                elif key == "fps":
                    self.fps = int(value)
                elif key == "full_screen_mode":
                    print(key, value, True if value == 'True' else False)
                    if value == 'True':
                        self.full_screen_mode = True
                    else:
                        self.full_screen_mode = False

    def save_settings(self,):
        with open("data/settings.csv", 'w', encoding="utf-8") as file:
            data = f'''name_parameter;value
full_screen_mode;{self.full_screen_mode}
resolution;{self.w},{self.h}
fps;{self.fps}'''
