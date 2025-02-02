import pygame.sprite


class Tree(pygame.sprite.Sprite):
    def __init__(self, texture, texture_destroy, settings, pos=(0, 0)):
        super().__init__()
        self.settings = settings
        self.image_orig = texture
        self.image_destroy = texture_destroy
        self.image = texture
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos