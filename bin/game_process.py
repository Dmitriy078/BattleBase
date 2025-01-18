import pygame

from bin.camera import Camera
from bin.characters.archer import Archer

CELL_SIZE = 50

class GameProcess:
    def __init__(self, settings, registry, audio, screen):
        self.settings = settings
        self.registry = registry
        self.audio = audio
        self.is_reboot = False
        self.size = self.width, self.height = self.settings.resolution
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()

        self.all_bullets_blue = pygame.sprite.Group()
        self.all_characters_blue = pygame.sprite.Group()
        self.player = Archer(self.registry, self.settings, 'archer_blue',
                             (self.settings.w // 2, self.settings.h // 2))
        self.all_characters_blue.add(self.player)

        bot = Archer(self.registry, self.settings, 'archer_blue',
                             (self.settings.w // 2 + 50, self.settings.h // 2))
        self.all_characters_blue.add(bot)

    def control_player(self, key_pressed_is):
        if key_pressed_is[pygame.K_a]:
            self.player.control['left'] = True
            self.player.control['right'] = False
        elif key_pressed_is[pygame.K_d]:
            self.player.control['left'] = False
            self.player.control['right'] = True
        else:
            self.player.control['left'] = False
            self.player.control['right'] = False

        if key_pressed_is[pygame.K_w]:
            self.player.control['up'] = True
            self.player.control['down'] = False
        elif key_pressed_is[pygame.K_s]:
            self.player.control['up'] = False
            self.player.control['down'] = True
        else:
            self.player.control['up'] = False
            self.player.control['down'] = False

        if key_pressed_is[pygame.K_SPACE]:
            self.player.control['attack'] = True
        else:
            self.player.control['attack'] = False


    # Игровой цикл
    def game(self):
        camera = Camera(self.settings)
        while self.running:
            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            key_pressed_is = pygame.key.get_pressed()
            mouse_pos = pygame.mouse.get_pos()

            # Обновления
            self.all_characters_blue.update(mouse_pos, self.all_bullets_blue)
            self.all_bullets_blue.update()
            if self.player:
                self.control_player(key_pressed_is)
                camera.update(self.player)
            for sprite in self.all_characters_blue:
                camera.apply(sprite)
            for sprite in self.all_bullets_blue:
                camera.apply(sprite)

            # Отрисовка
            self.screen.fill('white')
            self.all_characters_blue.draw(self.screen)
            self.all_bullets_blue.draw(self.screen)

            # Отображение
            pygame.display.flip()
            self.clock.tick(60)
