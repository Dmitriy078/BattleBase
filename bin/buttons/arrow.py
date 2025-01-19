import math

import pygame.sprite


class Arrow(pygame.sprite.Sprite):
    def __init__(self, res, settings, audio_player, name='arrow', pos=(0, 0), target_point=(0, 0)):
        super().__init__()
        self.audio_player = audio_player
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

        # Определяем вектор направления
        self.direction_x = self.target_point[0] - self.x
        self.direction_y = self.target_point[1] - self.y

        # Коррекция позиции, чтобы учесть смещение изображения
        offset_x = self.rect.width // 2
        offset_y = self.rect.height // 2

        if self.target_point[0] > self.x + offset_x:
            self.direction_x -= offset_x  # Вправо
        elif self.target_point[0] < self.x - offset_x:
            self.direction_x += offset_x  # Влево

        if self.target_point[1] > self.y + offset_y:
            self.direction_y -= offset_y  # Вниз
        elif self.target_point[1] < self.y - offset_y:
            self.direction_y += offset_y  # Вверх

        # Вычисляем угол для поворота изображения
        angle = math.degrees(math.atan2(-self.direction_y, self.direction_x))
        if -180 <= angle < -90 or 180 <= angle < 135:
            self.direction_x -= offset_x * 2
        if 1 <= angle < 90:
            self.direction_y -= offset_y * 2
        if 90 <= angle <= 135:
            self.direction_x -= offset_x
        if 85 < angle < 90:
            self.direction_x -= offset_x / 3
        # print(angle)

        angle = math.degrees(math.atan2(-self.direction_y, self.direction_x))
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)

        length = max(abs(self.direction_x) / self.speed_x, abs(self.direction_y) / self.speed_y)
        self.direction_x /= length
        self.direction_y /= length
        self.audio_player.play_sound('resources/sounds/firing the arrow.mp3')

    def update(self, enemy):
        for e in enemy:
            print(e.rect.x, self.x, e.rect.y, self.x)
            if pygame.sprite.collide_mask(self, e):
                print('Попадание')
                e.get_damage(self.damage)
                self.destroy()
                self.time = self.time_health
                return

        self.time += 1
        if self.time > self.time_health:
            self.destroy()
            return
        else:
            self.x += self.direction_x
            self.y += self.direction_y

            self.rect.x, self.rect.y = int(self.x), int(self.y)

    def destroy(self):
        self.audio_player.play_sound('resources/sounds/arrow hit.mp3')
        self.kill()
