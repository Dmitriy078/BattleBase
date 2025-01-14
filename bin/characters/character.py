import pygame.sprite


class Character(pygame.sprite.Sprite):
    def __init__(self, res, settings, name, pos=(0,0)):
        super().__init__()
        self.res = res
        self.settings = settings
        self.name = name

        self.time = 0
        self.current_frame = 0
        self.direction = 'right'
        self.status = 'idle'
        self.is_destroy = False

        self.image = self.res.textures[name][self.direction][self.status]['frames'][self.current_frame]
        self.rect = self.image.get_rect()
        self.x, self.y = self.rect.x, self.rect.y = pos

        self.speed_x = self.settings.fps // 12 * (self.settings.w // 800)
        self.speed_y = self.settings.fps // 12 * (self.settings.h // 600)

    def update(self):
        self.time += 1

        if self.time >= self.res.textures[self.name][self.direction][self.status]['t_change']:
            self.time = 0
            self.current_frame += 1

        if self.time == 0:
            if self.current_frame >= len(self.res.textures[self.name][self.direction][self.status]['frames']):
                if self.status == 'dead':
                    self.is_destroy = True
                    self.kill()
                else:
                    self.current_frame = 0

            if not self.is_destroy:
                self.image = self.res.textures[self.name][self.direction][self.status]['frames'][self.current_frame]

        if self.status == 'walk':
            if self.direction == 'left':
                self.x -= self.speed_x
            else:
                self.x += self.speed_x

        self.rect.x, self.rect.y = int(self.x), int(self.y)
