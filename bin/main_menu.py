import pygame

from bin.game_process import GameProcess
from bin.settings import Settings
from bin.settings_menu import SettingsMenu
from bin.ui.button import Button
from bin.ui.value_switch import ValueSwitch



class MainMenu:
    def __init__(self, settings, registry, audio, screen):
        self.settings = settings
        self.w, self.h = self.settings.resolution
        self.registry = registry
        self.audio = audio
        self.audio.set_sound_volume(self.settings.sound/100)
        self.audio.play_music('resources/music/main_menu.mp3')




        self.frames = self.registry.bg_main_menu
        self.frame_current = 0
        self.time = 0
        self.returned_lvl = 'map_road_1'

        self.size = self.width, self.height = self.settings.resolution
        self.screen = screen
        self.running = True
        # Загрузка изображений для кнопки
        button_texture = pygame.image.load("resources/buttons/Button_Blue_3Slides.png")  # Основная текстура
        button_texture_press = pygame.image.load(
            "resources/buttons/Button_Blue_3Slides_Pressed.png")  # Текстура при нажатии

        # Создание шрифта
        font = pygame.font.Font("resources/fonts/EpilepsySansBold.ttf", 30)
        self.but_play = Button(
            texture=button_texture,
            texture_press=button_texture_press,
            text='play',
            x=self.w // 2.5,
            y=self.h // 2,
            width=self.w // 7,
            height=self.h // 11,
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
        self.but_play.call = self.open_game

        self.but_settings = Button(
            texture=button_texture,
            texture_press=button_texture_press,
            text='settings',
            x=self.w // 2.5,
            y=self.h // 1.6,
            width=self.w // 7,
            height=self.h // 11,
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
        self.but_settings.call = self.run_settings
        self.but_exit = Button(
            texture=button_texture,
            texture_press=button_texture_press,
            text='exit',
            x=self.w // 2.5,
            y=self.h // 1.33,
            width=self.w // 7,
            height=self.h // 11,
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
        self.but_exit.call = self.exit_game
        self.but_exit_first = pygame.image.load("resources/buttons/Button_Blue.png")
        self.but_exit_press = pygame.image.load(
            "resources/buttons/Button_Blue_Pressed.png")
        self.level_game = ValueSwitch(
            texture=self.but_exit_first,
            texture_press=self.but_exit_press,
            x=self.settings.w * 0.28,
            y=self.settings.h * 0.71,
            values=["1", "2", "3"],
            select_value=str(self.settings.fps),
            width=110,
            height=70,
            font=font,
            font_size=self.w * self.h // 75000,
            center_text=True,
            offset_text_x=5,
            offset_text_y=10,
            offset_text_press_x=2,
            offset_text_press_y=2,
            audio_player=self.audio
        )
        self.level_game.call = self.set_level
    def show_menu(self):
        clock = pygame.time.Clock()
        time = 0
        right = False
        is_click = False
        while self.running and not self.settings.reboot:
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
            self.level_game.draw(self.screen)
            self.level_game.update(is_click=is_click, mouse_pos=mouse_pos)  # Обновляем состояние кнопки

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
    def set_level(self):
        self.returned_lvl = self.returned_lvl[:-1] + self.level_game.get_value()



    def exit_game(self):
        self.running = False

    def open_game(self):
        game = GameProcess(self.settings, self.registry, self.audio, self.screen, self.returned_lvl)
        game.game()

    def run_settings(self):
        s = Settings()
        set_show = SettingsMenu(self.settings, s.resolution, self.audio, self.screen)
        set_show.set_display()
