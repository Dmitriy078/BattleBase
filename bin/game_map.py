import os.path

import pygame

from bin.block import Block


class GameMap:
    def __init__(self, registry, settings, level):
        self.level = level
        self.registry = registry
        self.settings = settings
        self.grid = None
        self.all_solid_objects = pygame.sprite.Group()
        self.load_level()

    def load_level(self):
        if not os.path.exists(f'resources/maps/{self.level}.csv'):
            print('Файла карты нет')
            return

        data = None
        with open(f'resources/maps/{self.level}.csv', 'r', encoding='utf-8') as file:
            data = [row.rstrip().split(';') for row in file.readlines()]
        print(data)

        self.grid = [[] for i in range(len(data))]
        for row in range(len(data)):
            for col in range(len(data[row])):
                if 'elevation' in data[row][col]:
                    cell = data[row][col].split('_')
                    pos = (col * self.settings.cell_size, row * self.settings.cell_size,)
                    block = Block(self.registry.terrain['elevation'][int(cell[1])], pos)
                    self.all_solid_objects.add(block)
