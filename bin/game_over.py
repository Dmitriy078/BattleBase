import pygame


# класс конца игры
class GameOver:
    def __init__(self, settings, registry, audio, screen):
        self.settings = settings
        self.w, self.h = self.settings.resolution
        self.screen = screen
        self.registry = registry
        self.audio = audio
        self.audio.set_sound_volume(self.settings.sound / 100)
        self.audio.play_music('resources/music/main_menu.mp3')
        self.running = True
        self.clock = pygame.time.Clock()

    def set_display(self):
        while self.running and not self.settings.reboot:
            self.screen.fill((0, 0, 0))
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            # Отображение
            pygame.display.flip()
            self.clock.tick(60)
