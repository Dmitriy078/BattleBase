import pygame.sprite


# класс кустов
class Bush(pygame.sprite.Sprite):
    def __init__(self, texture, texture_destroy, settings):
        super().__init__()
        self.settings = settings
        self.image_orig = texture
        self.image_destroy = texture_destroy
        self.image = texture
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()