import pygame

from bin.game_process import GameProcess
from bin.settings import Settings
from bin.show_settings import SettingsShow
from bin.ui.button import Button


class MainMenu:
    def __init__(self, settings, registry, audio, screen):
        self.settings = settings
        self.registry = registry
        self.audio = audio
        self.audio.play_music('resources/music/main_menu.mp3')

        self.frames = self.registry.bg_main_menu
        self.frame_current = 0
        self.time = 0
        self.is_reboot = False

        self.size = self.width, self.height = self.settings.resolution
        self.screen = screen
        self.running = True
        # Загрузка изображений для кнопки
        button_texture = pygame.image.load("resources/buttons/Button_Blue_3Slides.png")  # Основная текстура
        button_texture_press = pygame.image.load(
            "resources/buttons/Button_Blue_3Slides_Pressed.png")  # Текстура при нажатии

        # Создание шрифта
        font = "Arial"
        # "resources\fonts\EpilepsySans.ttf"
        # "resources\fonts\EpilepsySansBold.ttf"
        font = pygame.font.Font("resources/fonts/EpilepsySansBold.ttf", 30)
        self.but_play = Button(
            texture=button_texture,
            texture_press=button_texture_press,
            text='play',
            x=310,
            y=295,
            width=170,
            height=70,
            text_color_rgb=(138, 9, 47),
            font=font,
            font_size=18,
            center_text=True,
            offset_text_x=5,
            offset_text_y=10,
            offset_text_press_x=2,
            offset_text_press_y=2,
            audio_player=self.audio
        )
        self.but_play.call = self.open_game

        self.but_settings = Button(
            texture=button_texture,
            texture_press=button_texture_press,
            text='settings',
            x=310,
            y=365,
            width=170,
            height=70,
            text_color_rgb=(138, 9, 47),
            font=font,
            font_size=48,
            center_text=True,
            offset_text_x=5,
            offset_text_y=10,
            offset_text_press_x=2,
            offset_text_press_y=2,
            audio_player=self.audio
        )
        self.but_settings.call = self.run_settings
        self.but_exit = Button(
            texture=button_texture,
            texture_press=button_texture_press,
            text='exit',
            x=310,
            y=435,
            width=170,
            height=70,
            text_color_rgb=(138, 9, 47),
            font=font,
            font_size=48,
            center_text=True,
            offset_text_x=5,
            offset_text_y=10,
            offset_text_press_x=2,
            offset_text_press_y=2,
            audio_player=self.audio
        )
        self.but_exit.call = self.exit_game

    def show_menu(self):

        clock = pygame.time.Clock()
        time = 0
        right = False
        is_click = False
        while self.running:
            mouse_pos = pygame.mouse.get_pos()
            self.screen.blit(self.frames[self.frame_current], (0, 0))
            self.but_play.draw(self.screen)

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

            # pygame_widgets.update(events)  # ОБЯЗАТЕЛЬНО для обновления виджетов
            self.but_play.update(is_click=is_click, mouse_pos=mouse_pos)  # Обновляем состояние кнопки
            self.but_play.draw(self.screen)  # Отрисовка кнопки
            self.but_settings.update(is_click=is_click, mouse_pos=mouse_pos)  # Обновляем состояние кнопки
            self.but_settings.draw(self.screen)  # Отрисовка кнопки
            self.but_exit.update(is_click=is_click, mouse_pos=mouse_pos)  # Обновляем состояние кнопки
            self.but_exit.draw(self.screen)  # Отрисовка кнопки

            pygame.display.update()

            clock.tick(self.settings.fps)
            pygame.display.flip()
            time += 1
            if time >= 3:
                if right:
                    self.frame_current = self.frame_current - 1
                else:
                    self.frame_current = self.frame_current + 1

                if self.frame_current < 0:
                    self.frame_current = 0
                    right = False
                elif self.frame_current >= len(self.frames):
                    self.frame_current = len(self.frames) - 1
                    right = True
                time = 0

    def exit_game(self):
        self.running = False

    def open_game(self):
        game = GameProcess(self.settings, self.registry, self.audio, self.screen)
        game.game()
    def run_settings(self):
        s = Settings()
        set_show = SettingsShow(self.settings, s.resolution, self.audio, self.screen)
        set_show.set_display()