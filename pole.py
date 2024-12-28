import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры игрового поля
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 50

class PlayingField:
    def __init__(self):
        self.tiles = []
        self.generate_tiles()

    def reserse(self):
        self.stone_texture = pygame.image.load('Tilemap_Elevation.png')
        self.grass_texture = pygame.image.load('08.png')
        self.tree_texture = pygame.image.load('Tree.png')
        self.bush_texture = pygame.image.load('01.png')

    def generate_tiles(self):
        for x in range(0, SCREEN_WIDTH, CELL_SIZE):
            column = []
            for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
                if random.random() < 0.1:
                    tile = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                    column.append(("bush_texture", tile))
                    column.append(("tree_texture", tile))
                else:
                    tile = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                    column.append(("stone_texture", tile))
            self.tiles.append(column)

    def draw(self, screen):
        for column in self.tiles:
            for _, tile in column:
                if _ == "stone_texture":
                    pygame.draw.rect(screen, (0, 0, 0), tile)
                else:
                    pygame.draw.rect(screen, (255, 255, 255), tile)

# Создаем игровое окно
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Playing Field")

playing_field = PlayingField()

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    playing_field.draw(screen)

    pygame.display.flip()

pygame.quit()
