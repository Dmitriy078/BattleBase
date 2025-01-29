import pygame
from bin.ui.button import Button
from bin.ui.toggle_but import ButtonToggle
from bin.ui.value_switch import ValueSwitch
from bin.ui.text import Text


class SettingsMenu:
    def __init__(self, settings, resolution, audio, screen):
        self.settings = settings
        self.resolution = resolution
        self.audio = audio
        self.is_reboot = False
        self.w, self.h = self.settings.resolution
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

        self.full_screen_text = Text(
            texture=None,  # У нас нет текстуры для текста
            text='full-screen mode',
            x=self.settings.w * 0.42,  # Центрируем текст
            y=self.settings.h * 0.3,
            width=300,
            height=100,
            text_color_rgb=(138, 9, 47),
            font=font,
            font_size=self.w * self.h // 75000,
            center_text=True,
            offset_text_x=0,
            offset_text_y=0)
        self.overall_volume_text = Text(
            texture=None,  # У нас нет текстуры для текста
            text='Overall volume',
            x=self.settings.w * 0.25,  # Центрируем текст
            y=self.settings.h * 0.4,
            width=300,
            height=100,
            text_color_rgb=(138, 9, 47),
            font=font,
            font_size=self.w * self.h // 75000,
            center_text=True,
            offset_text_x=0,
            offset_text_y=0)
        self.frame_rate_text = Text(
            texture=None,  # У нас нет текстуры для текста
            text='Frame rate',
            x=self.settings.w * 0.57,  # Центрируем текст
            y=self.settings.h * 0.4,
            width=300,
            height=100,
            text_color_rgb=(138, 9, 47),
            font=font,
            font_size=self.w * self.h // 75000,
            center_text=True,
            offset_text_x=0,
            offset_text_y=0)

        self.switch_full_screen_mode = ValueSwitch(
            texture=self.but_exit_first,
            texture_press=self.but_exit_press,
            x=self.settings.w * 0.45,  # Центрируем текст
            y=self.settings.h // 2 - (self.settings.h * 0.2 // 2),
            values=['Yes', 'No'],
            select_value='No' if self.settings.full_screen_mode == False else 'Yes',
            width=self.settings.w * 0.12,
            height=self.settings.h * 0.12,
            font=font,
            font_size=self.w * self.h // 75000,
            center_text=True,
            offset_text_x=5,
            offset_text_y=10,
            offset_text_press_x=2,
            offset_text_press_y=2,
            audio_player=self.audio
        )
        self.switch_volume = ValueSwitch(
            texture=self.but_exit_first,
            texture_press=self.but_exit_press,
            x=self.settings.w * 0.3,
            y=self.settings.h * 0.5,
            values=[str(i) for i in range(0, 101, 10)],
            select_value=str(self.settings.sound),
            width=140,
            height=90,
            font=font,
            font_size=self.w * self.h // 75000,
            center_text=True,
            offset_text_x=5,
            offset_text_y=10,
            offset_text_press_x=2,
            offset_text_press_y=2,
            audio_player=self.audio
        )
        self.switch_rate = ValueSwitch(
            texture=self.but_exit_first,
            texture_press=self.but_exit_press,
            x=self.settings.w * 0.62,
            y=self.settings.h * 0.5,
            values=[str(i) for i in range(45, 91, 15)],
            select_value=str(self.settings.fps),
            width=140,
            height=90,
            font=font,
            font_size=self.w * self.h // 75000,
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
            x=self.settings.w * 0.457,
            y=self.settings.h * 0.75,
            width=170,
            height=90,
            text_color_rgb=(138, 9, 47),
            font=font,
            font_size=self.w * self.h // 75000,
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
            x=self.settings.w * 0.45,
            y=self.settings.h * 0.6,
            width=190,
            height=90,
            text_color_rgb=(138, 9, 47),
            font=font,
            font_size=self.w * self.h // 75000,
            center_text=True,
            offset_text_x=5,
            offset_text_y=10,
            offset_text_press_x=2,
            offset_text_press_y=2,
            audio_player=self.audio
        )
        self.but_apply.call = self.save_settings

        self.frame = pygame.image.load(file)
        self.frame = pygame.transform.scale(self.frame, self.resolution)
        self.but_exit.call = self.exit_settings

    def do_full_screen(self):
        screen_info = pygame.display.Info()
        screen_width, screen_height = screen_info.current_w, screen_info.current_h
        self.screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    def set_display(self):
        is_click = False
        while self.running and not self.settings.reboot:
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

            self.but_apply.draw(self.screen)
            self.but_apply.update(is_click=is_click, mouse_pos=mouse_pos)  # Обновляем состояние кнопки

            self.switch_full_screen_mode.draw(self.screen)
            self.switch_full_screen_mode.update(is_click=is_click, mouse_pos=mouse_pos)

            self.switch_volume.draw(self.screen)
            self.switch_volume.update(is_click=is_click, mouse_pos=mouse_pos)  # Обновляем состояние кнопки

            self.switch_rate.draw(self.screen)
            self.switch_rate.update(is_click=is_click, mouse_pos=mouse_pos)  # Обновляем состояние кнопки

            self.full_screen_text.draw(self.screen)
            self.overall_volume_text.draw(self.screen)
            self.frame_rate_text.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

    def save_settings(self):
        temp = self.switch_full_screen_mode.get_value()
        if temp == 'Yes':
            self.settings.full_screen_mode = True
        else:
            self.settings.full_screen_mode = False
        self.settings.sound = self.switch_volume.get_value()
        self.settings.fps = int(self.switch_rate.get_value())

        self.settings.reboot = True
        self.settings.save_settings()

    def exit_settings(self):
        self.running = False
