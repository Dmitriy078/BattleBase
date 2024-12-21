import os
import pygame
from PIL.ImageChops import screen
from pygame_widgets.button import ButtonArray, Button
from pygame.locals import *
import pygame_widgets


class MainMenu:
    def __init__(self, settings, registry, screen):
        self.settings = settings
        self.registry = registry

        self.frames = self.registry.bg_main_menu
        self.frame_current = 0
        self.time = 0
        self.is_reboot = False

        self.size = self.width, self.height = self.settings.resolution
        self.screen = screen
        self.running = True
        self.but_play = Button(
            # Mandatory Parameters
            screen,  # Surface to place button on
            200,  # X-coordinate of top left corner
            290,  # Y-coordinate of top left corner
            100,  # Width
            100,  # Height

            # Optional Parameters
            text='Play',  # Text to display
            fontSize=20,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=(172, 183, 142),  # Colour of button when not being interacted with
            hoverColour=(184, 183, 153),  # Colour of button when being hovered over
            pressedColour=(0, 200, 20),  # Colour of button when being clicked
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=lambda: self.but_play.setText('Clicked!')  # Function to call when clicked on
        )
        self.but_settings = Button(
            # Mandatory Parameters
            screen,  # Surface to place button on
            200,  # X-coordinate of top left corner
            450,  # Y-coordinate of top left corner
            100,  # Width
            100,  # Height

            # Optional Parameters
            text='Settings',  # Text to display
            fontSize=20,  # Size of font
            margin=20,  # Minimum distance between text/image and edge of button
            inactiveColour=(172, 183, 142),  # Colour of button when not being interacted with
            hoverColour=(184, 183, 153),  # Colour of button when being hovered over
            pressedColour=(0, 200, 20),  # Colour of button when being clicked
            radius=20,  # Radius of border corners (leave empty for not curved)
            onClick=lambda: self.but_play.setText('Clicked!') # Function to call when clicked on
        )

    def show_menu(self):
        clock = pygame.time.Clock()
        time = 0
        right = False


        while self.running:
            events = pygame.event.get()
            self.screen.blit(self.frames[self.frame_current], (0, 0))
            self.but_play.draw()
            self.but_settings.draw()
            MENU_M0USE_POS = pygame.mouse.get_pos()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     self.but_play.setText('Clicked!')  # Обновляем текст кнопки

            pygame_widgets.update(events)  # ОБЯЗАТЕЛЬНО для обновления виджетов
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

