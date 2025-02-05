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
        self.terrain = dict()
        self.copse = dict()

        self.load_textures_background_main_menu()
        self.load_textures_characters()
        self.load_textures_bullets()
        self.load_textures_terrain()
        self.load_textures_building()
        self.load_textures_greenery()

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
        for i in ('archer_blue', 'archer_red'):
            dead_frames = self.load_image('characters/dead.png', True)
            dead_frames = self.cut_sheet(dead_frames, 7, 2)
            frames = self.load_image(f'characters/{i}.png', True)
            frames = self.cut_sheet(frames, 8, 7)

            self.textures[i] = {
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
                        't_change': self.settings.fps // 10
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
                        't_change': self.settings.fps // 10
                    }
                }
            }

        for i in ('warrior_blue', 'warrior_red'):
            dead_frames = self.load_image('characters/dead.png', True)
            dead_frames = self.cut_sheet(dead_frames, 7, 2)
            frames = self.load_image(f'characters/{i}.png', True)
            frames = self.cut_sheet(frames, 6, 8)

            self.textures[i] = {
                'left': {
                    'idle': {
                        'frames': self.horisontal_invert(frames[0:5]),
                        't_change': self.settings.fps // 12
                    },
                    'walk': {
                        'frames': self.horisontal_invert(frames[6:11]),
                        't_change': self.settings.fps // 12
                    },
                    'attack': {
                        'frames': self.horisontal_invert(frames[12:17]),
                        't_change': self.settings.fps // 12
                    },
                    'dead': {
                        'frames': self.horisontal_invert(dead_frames),
                        't_change': self.settings.fps // 10
                    }
                },
                'right':{
                    'idle': {
                        'frames': frames[0:5],
                        't_change': self.settings.fps // 12
                    },
                    'walk': {
                        'frames': frames[6:11],
                        't_change': self.settings.fps // 12
                    },
                    'attack': {
                        'frames': frames[12:17],
                        't_change': self.settings.fps // 12
                    },
                    'dead': {
                        'frames': dead_frames,
                        't_change': self.settings.fps // 10
                    }
                }
            }

        for i in ('support_blue', 'support_red'):
            dead_frames = self.load_image('characters/dead.png', True)
            dead_frames = self.cut_sheet(dead_frames, 7, 2)
            frames = self.load_image(f'characters/{i}.png', True)
            frames = self.cut_sheet(frames, 7, 5)

            self.textures[i] = {
                'left': {
                    'idle': {
                        'frames': self.horisontal_invert(frames[0:6]),
                        't_change': self.settings.fps // 12
                    },
                    'walk': {
                        'frames': self.horisontal_invert(frames[7:13]),
                        't_change': self.settings.fps // 12
                    },
                    'attack': {
                        'frames': self.horisontal_invert(frames[14:20]),
                        't_change': self.settings.fps // 12
                    },
                    'dead': {
                        'frames': self.horisontal_invert(dead_frames),
                        't_change': self.settings.fps // 10
                    }
                },
                'right':{
                    'idle': {
                        'frames': frames[0:6],
                        't_change': self.settings.fps // 12
                    },
                    'walk': {
                        'frames': frames[7:13],
                        't_change': self.settings.fps // 12
                    },
                    'attack': {
                        'frames': frames[14:20],
                        't_change': self.settings.fps // 12
                    },
                    'dead': {
                        'frames': dead_frames,
                        't_change': self.settings.fps // 10
                    }
                }
            }

        # тут загружаем остальных

    # Функция для загрузки снарядов
    def load_textures_bullets(self):
        self.t_bullets['arrow'] = pygame.transform.scale(self.load_image('bullets/arrow.png', True),
                                                     self.settings.arrow_size)

    # функция для загрузки текстур поля
    def load_textures_terrain(self):
        frames = self.load_image(f'terrain/elevation.png', True)
        frames = self.cut_sheet(frames, 4, 8)
        self.terrain['elevation'] = frames

        frames = self.load_image(f'terrain/flat.png', True)
        frames = self.cut_sheet(frames, 10, 4)
        self.terrain['flat'] = frames

    def load_textures_greenery(self):
        frames = self.load_image(f'copse/tree.png', True)
        frames = self.cut_sheet(frames, 4, 3)
        self.copse['tree'] = frames[0:4]

        frames = self.load_image(f'copse/bush.png', True)
        frames = pygame.transform.scale(frames, self.settings.cell_size)
        self.copse['bush'] = frames

        frames = self.load_image(f'copse/indicator_red.png', True)
        frames = pygame.transform.scale(frames, self.settings.cell_size)
        self.copse['indicator_red'] = frames

        frames = self.load_image(f'copse/indicator_blue.png', True)
        frames = pygame.transform.scale(frames, self.settings.cell_size)
        self.copse['indicator_blue'] = frames

    # функция для загрузки текстур строений
    def load_textures_building(self):
        dead_frames = self.load_image('copse/castle_destroyed.png', True)
        frames = self.load_image(f'copse/castle_blue.png', True)
        frames = pygame.transform.scale(frames, self.settings.cell_size)
        dead_frames = pygame.transform.scale(dead_frames, self.settings.cell_size)
        self.copse['castle_blue'] = frames
        self.copse['castle_blue_destroyed'] = dead_frames

        dead_frames = self.load_image('copse/castle_destroyed.png', True)
        frames = self.load_image(f'copse/castle_red.png', True)
        frames = pygame.transform.scale(frames, self.settings.cell_size)
        dead_frames = pygame.transform.scale(dead_frames, self.settings.cell_size)
        self.copse['castle_red'] = frames
        self.copse['castle_red_destroyed'] = dead_frames

        dead_frames = self.load_image('copse/tower_destroyed.png', True)
        frames = self.load_image(f'copse/tower_blue.png', True)
        frames = pygame.transform.scale(frames, self.settings.cell_size)
        dead_frames = pygame.transform.scale(dead_frames, self.settings.cell_size)
        self.copse['tower_blue'] = frames
        self.copse['tower_blue_destroyed'] = dead_frames

        dead_frames = self.load_image('copse/tower_destroyed.png', True)
        frames = self.load_image(f'copse/tower_red.png', True)
        frames = pygame.transform.scale(frames, self.settings.cell_size)
        dead_frames = pygame.transform.scale(dead_frames, self.settings.cell_size)
        self.copse['tower_red'] = frames
        self.copse['tower_red_destroyed'] = dead_frames

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