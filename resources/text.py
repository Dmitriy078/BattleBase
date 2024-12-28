import pygame


# Класс компонента "Надписи"/"Текста"
class Text:
    # Инициализация параметров
    def __init__(self, texture, text, x, y, width, height, text_color_rgb, font, font_size, center_text, offset_text_x, offset_text_y):
        self.is_pressed = False
        self.is_motion = False
        self.x = x
        self.y = y
        self.text = text
        self.text_color = text_color_rgb
        self.image = texture
        self.font_size = font_size
        self.font = pygame.font.SysFont(font, font_size)
        self.rect = pygame.Rect(x, y, width, height)
        self.offset_text_x = offset_text_x
        self.offset_text_y = offset_text_y
        self.center_text = center_text

    # Функция инвертирования цветов
    def inverse_color(self, color):
        return (255 - color[0],
                255 - color[1],
                255 - color[2])

    # Функция установки текста
    def set_text(self, text):
        self.text = text

    # Отрисовка текста
    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)

        text_render = self.font.render(self.text, True, self.inverse_color(self.text_color))
        if self.center_text:
            text_rect = text_render.get_rect(center=self.rect.center)
        else:
            text_rect = text_render.get_rect()
        text_rect.x += self.font_size // 16
        text_rect.x -= self.offset_text_x
        text_rect.y += self.font_size // 16
        text_rect.y -= self.offset_text_y
        screen.blit(text_render, text_rect)

        text_render = self.font.render(self.text, True, self.text_color)
        if self.center_text:
            text_rect = text_render.get_rect(center=self.rect.center)
        else:
            text_rect = text_render.get_rect()
        text_rect.x -= self.offset_text_x
        text_rect.y -= self.offset_text_y
        screen.blit(text_render, text_rect)
