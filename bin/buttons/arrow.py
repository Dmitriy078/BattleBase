import math

import pygame.sprite


class Arrow(pygame.sprite.Sprite):
    def __init__(self, res, settings, name='arrow', pos=(0, 0), target_point=(0, 0)):
        super().__init__()
        self.original_image = res.t_bullets[name]
        self.image = res.t_bullets[name]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.damage = 10
        self.speed_x = settings.fps // 5 * (settings.w // 800)
        self.speed_y = settings.fps // 5 * (settings.h // 600)

        self.time_health = settings.fps * 5
        self.time = 0
        self.x, self.y = pos
        self.target_point = target_point

        self.speed = settings.fps // 5 * (settings.w // 800)
        # Определяем угол
        self.direction_x = self.target_point[0] - self.x
        self.direction_y = self.target_point[1] - self.y

        # Нормализуем вектор
        length = math.hypot(self.direction_x, self.direction_y)
        if length != 0:  # Проверка деления на ноль
            self.direction_x /= length
            self.direction_y /= length

        # Умножаем на скорость
        self.direction_x *= self.speed
        self.direction_y *= self.speed

        # Вычисляем угол для поворота изображения
        angle = math.degrees(math.atan2(-self.direction_y, self.direction_x))
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.time += 1
        if self.time > self.time_health:
            self.kill()
            return
        else:
            self.x += self.direction_x
            self.y += self.direction_y

            self.rect.x, self.rect.y = int(self.x), int(self.y)
