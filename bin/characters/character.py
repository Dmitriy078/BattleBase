import pygame.sprite


# класс героев
class Character(pygame.sprite.Sprite):
    def __init__(self, res, settings, audio_player, name, pos=(0, 0)):
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

    # обнавление
    def update(self, mouse_pos, all_bullets, camera, solid_objects, is_ai=False):
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

            collide = pygame.sprite.spritecollideany(self, solid_objects)
            if collide:
                if self.rect.colliderect(collide.rect):
                    # Определение расстояний между границами спрайта и границами коллидера
                    right_distance = collide.rect.left - self.rect.right  # расстояние до левой грани коллайдера
                    left_distance = collide.rect.right - self.rect.left  # расстояние до правой грани коллайдера
                    bottom_distance = collide.rect.top - self.rect.bottom  # расстояние до верхней грани коллайдера
                    top_distance = collide.rect.bottom - self.rect.top  # расстояние до нижней грани коллайдера

                    # Определение минимального расстояния столкновения
                    min_distance = min(abs(right_distance), abs(left_distance), abs(bottom_distance), abs(top_distance))

                    if min_distance == abs(right_distance):  # Столкновение справа
                        self.x += right_distance  # Сдвигаем спрайт влево
                    elif min_distance == abs(left_distance):  # Столкновение слева
                        self.x += left_distance  # Сдвигаем спрайт вправо

                    if min_distance == abs(bottom_distance):  # Столкновение снизу
                        self.y += bottom_distance  # Сдвигаем спрайт вверх
                    elif min_distance == abs(top_distance):  # Столкновение сверху
                        self.y += top_distance  # Сдвигаем спрайт вниз

            if self.control['attack']:
                if self.status != 'attack':
                    self.status = 'attack'
                    self.time = 0
            elif (not self.control['up'] and not self.control['down'] and not self.control['left'] and
                  not self.control['right'] and not self.status == 'attack'):
                self.status = 'idle'

            if is_ai:
                self.ai_controller()
        else:
            self.status = 'dead'

        self.rect.x, self.rect.y = int(self.x), int(self.y)

    # поломка
    def get_damage(self, damage):
        self.health -= damage
        self.damage_time_i = 1

    # повреждение изображения
    def get_damage_image(self, image):
        damage_image = image.copy()
        for x in range(damage_image.get_width()):
            for y in range(damage_image.get_height()):
                pixel_color = damage_image.get_at((x, y))
                if pixel_color[0] > 0 or pixel_color[1] > 0 or pixel_color[2] > 0:
                    damage_image.set_at((x, y), pygame.Color(255, pixel_color[1], pixel_color[2]))
        return damage_image

    def ai_controller(self):
        pass
