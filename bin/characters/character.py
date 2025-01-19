import pygame.sprite


class Character(pygame.sprite.Sprite):
    def __init__(self, res, settings, audio_player, name, pos=(0,0)):
        super().__init__()
        self.res = res
        self.settings = settings
        self.name = name
        self.audio_player = audio_player

        self.time = 0
        self.current_frame = 0
        self.direction = 'right'
        self.status = 'idle'
        self.is_destroy = False

        self.image = self.res.textures[name][self.direction][self.status]['frames'][self.current_frame]
        self.rect = self.image.get_rect()
        self.x, self.y = self.rect.x, self.rect.y = pos

        self.health = 100
        self.damage_time = self.settings.fps // 2
        self.damage_time_i = 0
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

    def update(self, mouse_pos, all_bullets, camera):
        self.time += 1

        if self.damage_time_i:
            self.damage_time_i += 1

            if self.damage_time_i >= self.damage_time:
                self.damage_time_i = 0

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
                if self.damage_time_i:
                    self.image = self.get_damage_image(self.image)

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

    def get_damage(self, damage):
        self.health -= damage
        self.damage_time_i = 1

    def get_damage_image(self, image):
        damage_image = image.copy()
        for x in range(damage_image.get_width()):
            for y in range(damage_image.get_height()):
                pixel_color = damage_image.get_at((x, y))
                if pixel_color[0] > 0 or pixel_color[1] > 0 or pixel_color[2] > 0:
                    damage_image.set_at((x, y), pygame.Color(255, pixel_color[1], pixel_color[2]))
        return damage_image