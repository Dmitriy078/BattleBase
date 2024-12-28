import pygame
from resources.button import Button
from resources.text import Text

# Параметры окна
WIDTH, HEIGHT = 800, 600
FPS = 60

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Кнопка в Pygame")

# Загрузка изображений для кнопки
button_texture = pygame.image.load("../resources/buttons/Button_Blue_3Slides.png")  # Основная текстура
button_texture_press = pygame.image.load("../resources/buttons/Button_Blue_3Slides_Pressed.png")  # Текстура при нажатии

# Создание шрифта
font = 'Arial'


# Инициализация звукового воспроизведителя
class AudioPlayer:
    def play_sound(self, sound_name):
        # Здесь можно добавить код для воспроизведения звука
        print(f"Звук '{sound_name}' воспроизведён.")


audio_player = AudioPlayer()

# Создание кнопки
button = Button(
    texture=button_texture,
    texture_press=button_texture_press,
    text='ghb!',
    x=350,
    y=250,
    width=100,
    height=50,
    text_color_rgb = (120, 100, 40),
    font=font,
    font_size=30,
    center_text=True,
    offset_text_x=5,
    offset_text_y=5,
    offset_text_press_x=2,
    offset_text_press_y=2,
    audio_player=audio_player
)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка нажатия кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                button.update(is_click=True, mouse_pos=event.pos)
                button.draw(screen)  # Отрисовка кнопки

        # Обработка отпускания кнопки мыши
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Левая кнопка мыши
                button.update(is_click=False, mouse_pos=event.pos)

    # Получение позиции курсора мыши для обновления состояния кнопки
    mouse_pos = pygame.mouse.get_pos()
    button.update(is_click=False, mouse_pos=mouse_pos)  # Обновляем состояние кнопки


    # Отрисовка
    screen.fill((0, 0, 0))  # Заливка фона
    button.draw(screen)  # Отрисовка кнопки
    pygame.display.flip()  # Обновление экрана

    # Ограничение FPS
    pygame.time.Clock().tick(FPS)

pygame.quit()
