import pygame
class SettingsShow:
    def __init__(self, settings, resolution, audio, screen):
        self.settings = settings
        self.resolution = resolution
        self.audio = audio
        self.is_reboot = False
        self.size = self.width, self.height = self.settings.resolution
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()

    def set_display(self):
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
        file = "../resources/settings_image/workshop.png"
        frame = pygame.image.load(file).convert()
        frame = pygame.transform.scale(frame, self.resolution)



