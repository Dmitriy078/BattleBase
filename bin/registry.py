import os
import re
import pygame


# Класс для хранения статических ресурсов
class Registry:
    def __init__(self, resolution):
        self.resolution = resolution

        self.bg_main_menu = []

        self.load_textures_background_main_menu()

    def load_textures_background_main_menu(self):
        self.bg_main_menu.clear()
        directory = 'resources/menu/'
        gif_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.gif')]

        def extract_number(filename):
            match = re.search(r'(\d+)', filename)
            return int(match.group(0)) if match else float('inf')

        gif_files = sorted(gif_files, key=extract_number)

        for file in gif_files:
            frame = pygame.image.load(file).convert()
            frame = pygame.transform.scale(frame, self.resolution)
            self.bg_main_menu.append(frame)