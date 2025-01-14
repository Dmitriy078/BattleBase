import pygame

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

        self.all_characters = pygame.sprite.Group()
        self.player = Archer(self.registry, self.settings, 'archer_blue',
                             (self.settings.w // 2, self.settings.h // 2))
        self.all_characters.add(self.player)

    def game(self):
        while self.running:
            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            key_pressed_is = pygame.key.get_pressed()

            # Обновления
            self.all_characters.update()

            if key_pressed_is[pygame.K_a]:
                self.player.direction = 'left'
                self.player.status = 'walk'
            elif key_pressed_is[pygame.K_d]:
                self.player.direction = 'right'
                self.player.status = 'walk'
            else:
                self.player.status = 'idle'

            # Отрисовка
            self.screen.fill('white')
            self.all_characters.draw(self.screen)

            # Отображение
            pygame.display.flip()
            self.clock.tick(60)
