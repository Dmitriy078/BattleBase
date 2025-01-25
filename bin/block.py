import pygame.sprite


class Block(pygame.sprite.Sprite):
    def __init__(self, texture, pos=(0, 0)):
        super().__init__()
        self.image = texture
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
