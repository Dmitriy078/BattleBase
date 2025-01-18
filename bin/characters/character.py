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

        self.health = 100
        self.speed_x = self.settings.fps // 30 * (self.settings.w // 800)
        self.speed_y = self.settings.fps // 30 * (self.settings.h // 600)

        self.control = {
            'up': False,
            'down': False,
            'left': False,
            'right': False,
            'attack': False
        }

        self.bullet = None

    def update(self, mouse_pos, all_bullets):
        self.time += 1

        if self.time >= self.res.textures[self.name][self.direction][self.status]['t_change']:
            self.time = 0
            self.current_frame += 1

        if self.time == 0:
            if self.current_frame >= len(self.res.textures[self.name][self.direction][self.status]['frames']):
                if self.status == 'dead':
                    self.is_destroy = True
                    self.kill()
                elif self.status == 'attack':
                    self.status = 'idle'
                    self.time = 0
                    self.current_frame = 0
                else:
                    self.current_frame = 0

            if not self.is_destroy:
                self.image = self.res.textures[self.name][self.direction][self.status]['frames'][self.current_frame]

        if self.health > 0:
            if self.control['up']:
                self.y -= self.speed_y
                if self.status != 'attack':
                    self.status = 'walk'
            elif self.control['down']:
                self.y += self.speed_y
                if self.status != 'attack':
                    self.status = 'walk'

            if self.control['left']:
                self.x -= self.speed_x
                self.direction = 'left'
                if self.status != 'attack':
                    self.status = 'walk'
            elif self.control['right']:
                self.x += self.speed_x
                self.direction = 'right'
                if self.status != 'attack':
                    self.status = 'walk'

            if self.control['attack']:
                if self.status != 'attack':
                    self.status = 'attack'
                    self.time = 0
            elif (not self.control['up'] and not self.control['down'] and not self.control['left'] and
                  not self.control['right'] and not self.status == 'attack'):
                self.status = 'idle'
        else:
            self.status = 'dead'

        self.rect.x, self.rect.y = int(self.x), int(self.y)
