import os
import pygame
class MainMenu:
    def __init__(self):
        super().__init__()
        self.is_reboot = False
        pygame.init()
        self.size = self.width, self.height = 800, 600
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            self.draw()
        pygame.quit()

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
