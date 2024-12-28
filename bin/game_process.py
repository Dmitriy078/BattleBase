import pygame

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

    def game(self):
        while self.running:
            self.screen.fill('white')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            pygame.display.flip()
            self.clock.tick(60)
