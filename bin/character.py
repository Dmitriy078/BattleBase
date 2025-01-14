import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle Base")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

warrior_image = pygame.image.load('Archer_Blue_(NoArms).png')
warrior_rect = warrior_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()

    direction_x = mouse_x - warrior_rect.centerx
    direction_y = mouse_y - warrior_rect.centery

    distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
    if distance != 0:
        direction_x /= distance
        direction_y /= distance

    speed = 5
    warrior_rect.x += direction_x * speed
    warrior_rect.y += direction_y * speed

    # Ограничение движения в пределах окна
    if warrior_rect.left < 0:
        warrior_rect.left = 0
    if warrior_rect.right > WIDTH:
        warrior_rect.right = WIDTH
    if warrior_rect.top < 0:
        warrior_rect.top = 0
    if warrior_rect.bottom > HEIGHT:
        warrior_rect.bottom = HEIGHT

    screen.fill(WHITE)
    screen.blit(warrior_image, warrior_rect)
    pygame.display.flip()

pygame.quit()
