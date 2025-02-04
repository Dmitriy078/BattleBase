import pygame.sprite


# класс деревьев
class Tree(pygame.sprite.Sprite):
    def __init__(self, textures, settings, pos=(0, 0)):
        super().__init__()
        self.settings = settings
        self.frames = textures
        self.image = self.frames[0]
        self.current = 0
        self.time = 0
        self.time_to_next = self.settings.fps // 3

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

    def update(self):
        self.time += 1
        if self.time >= self.time_to_next:
            self.current = (self.current + 1) % len(self.frames)
            self.image = self.frames[self.current]
            self.time = 0
