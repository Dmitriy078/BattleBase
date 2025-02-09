import pygame.sprite
from bin.game_over import GameOver


# класс замков
class Castle(pygame.sprite.Sprite):
    def __init__(self, texture, texture_destroy, settings, pos=(0, 0)):
        super().__init__()
        self.settings = settings
        self.image_orig = texture
        self.image_destroy = texture_destroy
        self.image = texture
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

        self.health = 100

        self.damage_time = self.settings.fps // 2
        self.damage_time_i = 1

    def update(self):
        if self.health <= 0:
            if self.damage_time_i == 0:
                self.damage_time_i = 1
                self.image = self.image_destroy
            else:
                self.damage_time_i += 1
                if self.damage_time_i >= self.damage_time * 3:
                    self.kill()
                    # set_show = GameOver(self.settings)
                    # set_show.set_display()

        else:
            if self.damage_time_i:
                self.damage_time_i += 1
                if self.damage_time_i >= self.damage_time:
                    self.image = self.image_orig
                    self.damage_time_i = 0

    def get_damage(self, damage):
        if self.health > 0:
            self.health -= damage
            self.damage_time_i = 1
            self.image = self.get_damage_image(self.image)

            if self.health <= 0:
                self.damage_time_i = 0

    def get_damage_image(self, image):
        damage_image = image.copy()
        for x in range(damage_image.get_width()):
            for y in range(damage_image.get_height()):
                pixel_color = damage_image.get_at((x, y))
                if pixel_color[0] > 0 or pixel_color[1] > 0 or pixel_color[2] > 0:
                    damage_image.set_at((x, y), pygame.Color(255, pixel_color[1], pixel_color[2]))
        return damage_image