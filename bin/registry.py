import os
import re
import sys

import pygame


# Класс для хранения статических ресурсов
class Registry:
    def __init__(self, resolution, settings):
        self.resolution = resolution
        self.settings = settings

        self.bg_main_menu = []
        self.textures = dict()
        self.t_bullets = dict()

        self.load_textures_background_main_menu()
        self.load_textures_characters()
        self.load_textures_bullets()

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

    def load_textures_characters(self):
        dead_frames = self.load_image('characters/dead.png', True)
        dead_frames = self.cut_sheet(dead_frames, 7, 2)
        frames = self.load_image('characters/archer_blue.png', True)
        frames = self.cut_sheet(frames, 8, 7)
        self.textures['archer_blue'] = {
            'left': {
                'idle': {
                    'frames': self.horisontal_invert(frames[0:6]),
                    't_change': self.settings.fps // 12
                },
                'walk': {
                    'frames': self.horisontal_invert(frames[8:14]),
                    't_change': self.settings.fps // 12
                },
                'attack': {
                    'frames': self.horisontal_invert(frames[32:40]),
                    't_change': self.settings.fps // 12
                },
                'dead': {
                    'frames': self.horisontal_invert(dead_frames),
                    't_change': self.settings.fps // 6
                }
            },
            'right':{
                'idle': {
                    'frames': frames[0:6],
                    't_change': self.settings.fps // 12
                },
                'walk': {
                    'frames': frames[8:14],
                    't_change': self.settings.fps // 12
                },
                'attack': {
                    'frames': frames[32:40],
                    't_change': self.settings.fps // 12
                },
                'dead': {
                    'frames': dead_frames,
                    't_change': self.settings.fps // 6
                }
            }
        }

    # Функция для загрузки снарядов
    def load_textures_bullets(self):
        self.t_bullets['arrow'] = pygame.transform.scale(self.load_image('bullets/arrow.png', True),
                                                     self.settings.arrow_size)

    # Функция для загрузки изображения
    def load_image(self, name, alpha=False):
        fullname = os.path.join('resources', name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()

        image = pygame.image.load(fullname)

        if alpha:
            image = image.convert_alpha()
        else:
            image = image.convert()

        return image

    # Функция для обрезки изображения
    def cut_sheet(self, sheet, columns, rows):
        rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        frames = []
        for j in range(rows):
            for i in range(columns):
                frame_location = (rect.w * i, rect.h * j)
                frames.append(pygame.transform.scale(sheet.subsurface(pygame.Rect(frame_location, rect.size)),
                                                     self.settings.cell_size))
        return frames

    # Функция для горизонтального инвертирование картинок
    def horisontal_invert(self, frames):
        fs = frames.copy()
        results = []
        for f in fs:
            results.append(pygame.transform.flip(f, True, False))
        return results