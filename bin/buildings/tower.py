import pygame.sprite

from bin.bullets.arrow import Arrow


class Tower(pygame.sprite.Sprite):
    def __init__(self, res, texture, texture_destroy, settings, audio, pos=(0, 0)):
        super().__init__()
        self.res = res
        self.settings = settings
        self.audio = audio
        self.image_orig = texture
        self.image_destroy = texture_destroy
        self.image = texture
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

        self.health = 100

        self.damage_time = self.settings.fps // 2
        self.damage_time_i = 1

        # Задаем радиус проверки
        self.detection_radius_x = self.settings.cell_size[0] * 5
        self.detection_radius_y = self.settings.cell_size[1] * 5

        self.time_to_attack = self.settings.fps
        self.time_attack = 1

    def update(self, all_bullets, solid_objects, enemies):
        if self.health <= 0:
            if self.damage_time_i == 0:
                self.damage_time_i = 1
                self.image = self.image_destroy
            else:
                self.damage_time_i += 1
                if self.damage_time_i >= self.damage_time * 3:
                    self.kill()

        else:
            if self.damage_time_i:
                self.damage_time_i += 1

                if self.damage_time_i >= self.damage_time:
                    self.image = self.image_orig
                    self.damage_time_i = 0

        if self.time_attack:
            if self.time_attack >= self.time_to_attack:
                self.time_attack = 0
            else:
                self.time_attack += 1
        else:
            # Проверка всех врагов на наличие в области вокруг башни
            for enemy in enemies:
                if self.rect.colliderect(enemy.rect.inflate(self.detection_radius_x, self.detection_radius_y)):
                    arrow = Arrow(self.res, self.settings, self.audio, pos=(self.rect.x, self.rect.y),
                                  target_point=(enemy.x, enemy.y))
                    all_bullets.add(arrow)
                    self.time_attack = 1
                    return

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

