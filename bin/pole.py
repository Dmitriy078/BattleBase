import pygame
import random


class PlayingField:
    def __init__(self):
        self.tiles = []
        self.generate_tiles()

    '''def load_level(filename):
        filename = "data/" + filename
        with open(filename, 'r') as mapFile:
            level_map = [line.strip() for line in mapFile]

        max_width = max(map(len, level_map))

        return list(map(lambda x: x.ljust(max_width, '.'), level_map))

    tile_images = {
        'wall': load_image('box.png'),
        'empty': load_image('grass.png')
    }
    player_image = load_image('mar.png')

    tile_width = tile_height = 50

    class Tile(pygame.sprite.Sprite):
        def __init__(self, tile_type, pos_x, pos_y):
            super().__init__(tiles_group, all_sprites)
            if tile_type == 'wall':
                walls_group.add(self)
            self.image = tile_images[tile_type]
            self.rect = self.image.get_rect().move(
                tile_width * pos_x, tile_height * pos_y)

    class Player(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            super().__init__(player_group, all_sprites)
            self.image = player_image
            self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)

        def update(self, *event):
            if event:
                if event[0].key == pygame.K_UP:
                    self.rect = self.image.get_rect().move(self.rect.x, self.rect.y - tile_height)
                    if pygame.sprite.spritecollideany(self, walls_group):
                        self.rect = self.image.get_rect().move(self.rect.x, self.rect.y + tile_height)
                if event[0].key == pygame.K_DOWN:
                    self.rect = self.image.get_rect().move(self.rect.x, self.rect.y + tile_height)
                    if pygame.sprite.spritecollideany(self, walls_group):
                        self.rect = self.image.get_rect().move(self.rect.x, self.rect.y - tile_height)
                if event[0].key == pygame.K_RIGHT:
                    self.rect = self.image.get_rect().move(self.rect.x + tile_width, self.rect.y)
                    if pygame.sprite.spritecollideany(self, walls_group):
                        self.rect = self.image.get_rect().move(self.rect.x - tile_width, self.rect.y)
                if event[0].key == pygame.K_LEFT:
                    self.rect = self.image.get_rect().move(self.rect.x - tile_width, self.rect.y)
                    if pygame.sprite.spritecollideany(self, walls_group):
                        self.rect = self.image.get_rect().move(self.rect.x + tile_width, self.rect.y)

    clock = pygame.time.Clock()
    start_screen()

    player = None

    all_sprites = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    walls_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()

    def generate_level(level):
        new_player, x, y = None, None, None
        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == '.':
                    Tile('empty', x, y)
                elif level[y][x] == '#':
                    Tile('wall', x, y)
                elif level[y][x] == '@':
                    Tile('empty', x, y)
                    p_x, p_y = x, y
        new_player = Player(p_x, p_y)
        return new_player, x, y

    player, level_x, level_y = generate_level(load_level('map1.txt'))
    
    t_e - @
    t_f1 - .
    t_f2 - /
    castle - #
    tower - |
    indicator - ?
    tree - $ '''
