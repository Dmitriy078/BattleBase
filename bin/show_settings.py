import pygame
from bin.ui.button import Button
from bin.ui.toggle_but import ButtonToggle
from bin.ui.value_switch import ValueSwitch
from bin.ui.text import Text


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
        file = "resources/settings_image/workshop.png"
        self.but_apply_first = pygame.image.load("resources/buttons/Button_Blue_3Slides.png")  # Основная текстура
        self.but_apply_press = pygame.image.load(
            "resources/buttons/Button_Blue_3Slides_Pressed.png")  # Текстура при нажатии
        self.but_exit_first = pygame.image.load("resources/buttons/Button_Blue.png")  # Основная текстура
        self.but_exit_press = pygame.image.load(
            "resources/buttons/Button_Blue_Pressed.png")
        font = pygame.font.Font("resources/fonts/EpilepsySansBold.ttf", 30)

        self.switch = ValueSwitch(
            texture=self.but_exit_first,
            texture_press=self.but_exit_press,
            x=590,
            y=305,
            values=[str(i) for i in range(100)],
            select_value = '1',
            width=170,
            height=90,
            font=font,
            font_size=18,
            center_text=True,
            offset_text_x=5,
            offset_text_y=10,
            offset_text_press_x=2,
            offset_text_press_y=2,
            audio_player=self.audio
        )
        self.but_exit = Button(
            texture=self.but_exit_first,
            texture_press=self.but_exit_press,
            text='exit',
            x=320,
            y=465,
            width=170,
            height=90,
            text_color_rgb=(120, 100, 40),
            font=font,
            font_size=18,
            center_text=True,
            offset_text_x=5,
            offset_text_y=10,
            offset_text_press_x=2,
            offset_text_press_y=2,
            audio_player=self.audio
        )
        self.but_apply = Button(
            texture=self.but_apply_first,
            texture_press=self.but_apply_press,
            text='apply',
            x=310,
            y=355,
            width=190,
            height=90,
            text_color_rgb=(120, 100, 40),
            font=font,
            font_size=18,
            center_text=True,
            offset_text_x=5,
            offset_text_y=10,
            offset_text_press_x=2,
            offset_text_press_y=2,
            audio_player=self.audio
        )
        self.full_screen_text = Text(
    texture=None,  # У нас нет текстуры для текста
    text='full-screen mode',
    x=244,  # Центрируем текст
    y=132,
    width=300,
    height=100,
    text_color_rgb= (138, 9, 47),
    font=font,
    font_size=50,
    center_text=True,
    offset_text_x=0,
    offset_text_y=0)
        self.but_on = ButtonToggle(
            texture=self.but_apply_first,
            texture_press=self.but_apply_press,
            text='turn on',
            x=385,
            y=200,
            width=190,
            height=90,
            text_color_rgb=(120, 100, 40),
            font=font,
            font_size=18,
            center_text=True,
            offset_text_x=5,
            offset_text_y=10,
            offset_text_press_x=2,
            offset_text_press_y=2,
            audio_player=self.audio
        )
        self.but_off = ButtonToggle(
            texture=self.but_apply_first,
            texture_press=self.but_apply_press,
            text='turn off',
            x=195,
            y=200,
            width=190,
            height=90,
            text_color_rgb=(120, 100, 40),
            font=font,
            font_size=18,
            center_text=True,
            offset_text_x=5,
            offset_text_y=10,
            offset_text_press_x=2,
            offset_text_press_y=2,
            audio_player=self.audio
        )
        self.frame = pygame.image.load(file)
        self.frame = pygame.transform.scale(self.frame, self.resolution)
        self.but_exit.call = self.exit_settings


    def set_display(self):
        is_click = False
        while self.running:
            # self.screen.fill('white')
            self.screen.blit(self.frame, (0, 0))
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    is_click = True
                if event.type == pygame.MOUSEBUTTONUP:
                    is_click = False
            self.but_exit.update(is_click=is_click, mouse_pos=mouse_pos)  # Обновляем состояние кнопки
            self.but_exit.draw(self.screen)
            self.but_apply.update(is_click=is_click, mouse_pos=mouse_pos)  # Обновляем состояние кнопки
            self.switch.draw(self.screen)
            self.switch.update(is_click=is_click, mouse_pos=mouse_pos)  # Обновляем состояние кнопки
            self.but_off.draw(self.screen)
            self.but_off.update(is_click=is_click, mouse_pos=mouse_pos)
            self.but_on.draw(self.screen)
            self.but_on.update(is_click=is_click, mouse_pos=mouse_pos)
            self.full_screen_text.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
    def exit_settings(self):
        self.running  = False



