import os.path

import pygame.display


# класс настроек - параметров
class Settings:
    def __init__(self):
        self.display = 0
        self.resolutions = pygame.display.list_modes(display=self.display)
        self.full_screen_mode = False
        self.sound = 60
        if (1600, 900) in self.resolutions:
            self.resolution = (1600, 900)
        else:
            self.resolution = self.resolutions[0]
        self.w, self.h = self.resolution
        self.fps = 60
        self.cell_size = (self.resolution[0] // 12.5, self.resolution[1] // 9.375)
        self.arrow_size = (self.resolution[0] // 30, self.resolution[1] // 22.5)
        self.reboot = False
        self.load_settings()

    def load_settings(self):
        if not os.path.exists('data/settings.csv'):
            self.save_settings()

        with open("data/settings.csv", encoding="utf-8") as file:
            strings = file.readlines()

            for string in strings:
                key, value = string.replace('\n', '').split(";")

                if key == "resolution":
                    self.resolution = tuple(map(int, value.split(',')))
                    self.w, self.h = self.resolution
                    self.cell_size = (self.resolution[0] // 12.5, self.resolution[1] // 9.375)
                    self.arrow_size = (self.resolution[0] // 30, self.resolution[1] // 22.5)
                elif key == "fps":
                    self.fps = int(value)
                elif key == "full_screen_mode":
                    if value == 'True':
                        self.full_screen_mode = True
                    else:
                        self.full_screen_mode = False
                elif key == "s_volume":
                    self.sound = int(value)
                elif key == "fps":
                    self.fps = int(self.fps)

    def save_settings(self):
        if not os.path.exists("data"):
            os.mkdir('data')

        with open("data/settings.csv", 'w', encoding="utf-8") as file:
            data = f'''name_parameter;value
full_screen_mode;{self.full_screen_mode}
resolution;{self.w},{self.h}
s_volume;{self.sound}
fps;{self.fps}'''
            file.write(data)
