import pygame
import random

pygame.init()

#параметры окна
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Игровое поле')

#загрузка текстур
stone_texture = pygame.image.load('Tilemap_Elevation.png')
grass_texture = pygame.image.load('08.png')
tree_texture = pygame.image.load('Tree.png')
bush_texture = pygame.image.load('01.png')
#размер текстур
texture_size = 32  # пиксели

#генерация игрового поля
game_board = []
for i in range(width // texture_size):
    column = []
for j in range(height // texture_size):
    texture = grass_texture if random.random() < 0.8 else stone_texture
    column.append(texture)
    game_board.append(column)

#добавление деревьев, кустов и домов
for i in range(width // texture_size):
    for j in range(height // texture_size):
        if random.random() < 0.3:
            game_board[i][j] = tree_texture
        elif random.random() < 0.05:
            game_board[i][j] = bush_texture
        elif random.random() < 0.01:
            game_board[i][j] = grass_texture

#отрисовка игрового поля
for i in range(width // texture_size):
    for j in range(height // texture_size):
        screen.blit(game_board[i][j], (i * texture_size, j * texture_size))

#обновление экрана
pygame.display.flip()

#основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#завершение работы pygame
pygame.quit()