import pygame.sprite


class Block(pygame.sprite.Sprite):
    def __init__(self, texture, pos):
        super().__init__()
        self.image = texture
        print(self.image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
