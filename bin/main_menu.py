import os
import pygame
import ctypes


class MainMenu:
    def __init__(self, settings):
        self.frames = []
        self.frame_current = 0
        self.time = 0
        self.is_reboot = False

        self.size = self.width, self.height = 800, 680
        self.screen = pygame.display.set_mode(self.size)
        self.running = True
        self.show()


        self.load_textures()

    def show(self):
        self.load_textures()
        clock = pygame.time.Clock()
        time = 0
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                self.screen.blit(self.frames[self.frame_current], (0, 0))
            clock.tick(60)
            pygame.display.flip()
            time += 1
            if time >= 3:
                self.frame_current = (self.frame_current + 1) % len(self.frames)
                time = 0
    def load_textures(self):
        gif_files = ['./resources/menu/' + f for f in os.listdir('./resources/menu') if f.endswith('.gif')]
        for file in gif_files:
            self.frame = pygame.image.load(file).convert()
            self.frame = pygame.transform.scale(pygame.image.load(file).convert(), self.size)
            self.frames.append(self.frame)
    def draw(self, screen):
        screen.fill((216, 194, 255))
        font = pygame.font.Font(None, 50)
        text = font.render("Hello, Pygame!", True, (100, 255, 100))
        text_x = self.width // 2 - text.get_width() // 2
        text_y = self.height // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 1)


        if not os.path.exists("data"):
            os.makedirs("data")

    def show_menu(self):
        pass
