import os.path

import pygame

from bin.block import Block
from bin.buildings.castle import Castle
from bin.buildings.tower import Tower
from bin.characters.archer import Archer
from bin.characters.support import Support
from bin.characters.swordsman import Swordsman


class GameMap:
    def __init__(self, registry, settings, audio, level):
        self.level = level
        self.registry = registry
        self.settings = settings
        self.audio = audio
        self.grid = None


        self.all_bullets_blue = pygame.sprite.Group()
        self.all_characters_blue = pygame.sprite.Group()
        self.all_castle_blue = pygame.sprite.Group()
        self.all_tower_blue = pygame.sprite.Group()

        self.all_bullets_red = pygame.sprite.Group()
        self.all_characters_red = pygame.sprite.Group()
        self.all_castle_red = pygame.sprite.Group()
        self.all_tower_red = pygame.sprite.Group()

        self.all_solid_objects = pygame.sprite.Group()
        self.all_not_solid_objects = pygame.sprite.Group()

        self.player = None
        self.player_character = 'archer'

        self.load_level()

    def load_level(self):
        if not os.path.exists(f'resources/maps/{self.level}.csv'):
            print('Файла карты нет')
            return

        data = None
        with open(f'resources/maps/{self.level}.csv', 'r', encoding='utf-8') as file:
            data = [row.rstrip().split(';') for row in file.readlines()]

        self.grid = [[] for i in range(len(data))]
        for row in range(len(data)):
            for col in range(len(data[row])):
                cell = data[row][col].split('.')

                for e in cell:
                    if 'elevation' in e:
                        temp = e.split('_')
                        pos = (col * self.settings.cell_size[0], row * self.settings.cell_size[1])
                        block = Block(self.registry.terrain['elevation'][int(temp[1])], pos)
                        self.all_solid_objects.add(block)

                    if 'flat' in e:
                        temp = e.split('_')
                        pos = (col * self.settings.cell_size[0], row * self.settings.cell_size[1])
                        block = Block(self.registry.terrain['flat'][int(temp[1])], pos)
                        self.all_not_solid_objects.add(block)

                    if 'red' in e:
                        if 'castle_red' in e:
                            pos = (col * self.settings.cell_size[0], row * self.settings.cell_size[1])
                            block = Castle(self.registry.copse['castle_red'],
                                           self.registry.copse['castle_red_destroyed'],
                                           self.settings,
                                           pos)
                            self.all_castle_red.add(block)

                        if 'tower_red' in e:
                            pos = (col * self.settings.cell_size[0], row * self.settings.cell_size[1])
                            block = Tower(self.registry.copse['tower_red'],
                                           self.registry.copse['tower_red_destroyed'],
                                           self.settings,
                                           pos)
                            self.all_tower_red.add(block)

                        if 'archer' in e:
                            pos = (col * self.settings.cell_size[0], row * self.settings.cell_size[1])
                            temp = Archer(self.registry, self.settings, self.audio, 'archer_red', pos)
                            self.all_characters_red.add(temp)

                        if 'warrior' in e:
                            pos = (col * self.settings.cell_size[0], row * self.settings.cell_size[1])
                            temp = Swordsman(self.registry, self.settings, self.audio, 'warrior_red', pos)
                            self.all_characters_red.add(temp)

                        if 'support' in e:
                            pos = (col * self.settings.cell_size[0], row * self.settings.cell_size[1])
                            temp = Support(self.registry, self.settings, self.audio, 'support_red', pos)
                            self.all_characters_red.add(temp)

                    if 'blue' in e:
                        if 'castle_blue' in e:
                            pos = (col * self.settings.cell_size[0], row * self.settings.cell_size[1])
                            block = Castle(self.registry.copse['castle_blue'],
                                           self.registry.copse['castle_blue_destroyed'],
                                           self.settings,
                                           pos)
                            self.all_castle_blue.add(block)

                        if 'tower_blue' in e:
                            pos = (col * self.settings.cell_size[0], row * self.settings.cell_size[1])
                            block = Tower(self.registry.copse['tower_blue'],
                                           self.registry.copse['tower_blue_destroyed'],
                                           self.settings,
                                           pos)
                            self.all_tower_blue.add(block)

                        if 'archer' in e:
                            pos = (col * self.settings.cell_size[0], row * self.settings.cell_size[1])
                            temp = Archer(self.registry, self.settings, self.audio, 'archer_blue', pos)
                            self.all_characters_blue.add(temp)

                        if 'warrior' in e:
                            pos = (col * self.settings.cell_size[0], row * self.settings.cell_size[1])
                            temp = Swordsman(self.registry, self.settings, self.audio, 'warrior_blue', pos)
                            self.all_characters_blue.add(temp)

                        if 'support' in e:
                            pos = (col * self.settings.cell_size[0], row * self.settings.cell_size[1])
                            temp = Support(self.registry, self.settings, self.audio, 'support_blue', pos)
                            self.all_characters_blue.add(temp)

                    if 'player' in e:
                        temp = e.split('_')
                        pos = (col * self.settings.cell_size[0], row * self.settings.cell_size[1])
                        if self.player_character == 'archer':
                            temp = Archer(self.registry, self.settings, self.audio, 'archer_blue', pos)

                        self.all_characters_blue.add(temp)
                        self.player = temp
