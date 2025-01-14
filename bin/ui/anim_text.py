from bin.ui.text import Text
import pygame
class AnimatedText(Text):
    def __init__(self, texture, text, x, y, width, height, text_color_rgb, font, font_size, center_text, offset_text_x, offset_text_y):
        #          , text_color_rgb, center_text, offset_text_x, offset_text_y
        super().__init__(texture, text, x, y, width, height, text_color_rgb, font, font_size, center_text, offset_text_x, offset_text_y)
        self.animation_time = 0  # Время для анимации
        self.text_color_rgb = text_color_rgb
        self.fade_speed = 2  # Скорость затухания
        self.is_fading_in = True  # Указывает, затухает ли текст

    def update(self):
        # Обновление цвета текста для анимации
        if self.is_fading_in:
            if self.text_color_rgb[3] < 255:  # Прозрачность
                self.color = (self.text_color_rgb[0], self.text_color_rgb[1], self.text_color_rgb[2], min(255, self.text_color_rgb[3] + self.fade_speed))
            else:
                self.is_fading_in = False
        else:
            if self.text_color_rgb[3] > 0:
                self.text_color_rgb = (self.text_color_rgb[0], self.text_color_rgb[1], self.text_color_rgb[2], max(0, self.text_color_rgb[3] - self.fade_speed))
            else:
                self.is_fading_in = True  # Перезапустить анимацию

    def draw(self, screen):
        # Изменение цвета для работы с прозрачностью
        original_color = pygame.Color(*self.text_color_rgb)  # Сохраняем оригинальный цвет
        text_render = self.font.render(self.text, True, original_color)
        if self.center_text:
            text_rect = text_render.get_rect(center=self.rect.center)
        else:
            text_rect = text_render.get_rect(topleft=(self.x + self.offset_text_x, self.y + self.offset_text_y))

        screen.blit(text_render, text_rect)


# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Анимированный текст в Pygame")

# Инициализация шрифта
font = pygame.font.SysFont('Arial', 50)

# Создание экземпляра анимированного текста
animated_text = AnimatedText(
    texture=None,  # У нас нет текстуры для текста
    text='Привет, мир!',
    x=WIDTH // 2,  # Центрируем текст
    y=HEIGHT // 2,
    width=300,
    height=100,
    text_color_rgb= (33, 33, 33),
    font=font,
    font_size=50,
    center_text=True,
    offset_text_x=0,
    offset_text_y=0
)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    animated_text.update()  # Обновляем состояние кнопки
    animated_text.draw(screen)