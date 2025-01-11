import pygame
import ctypes
from bin.audio import AudioManager
from bin.settings import Settings
from bin.registry import Registry
from bin.main_menu import MainMenu


# Запуск игры
def start_game():
    pygame.init()
    ctypes.windll.user32.SetProcessDPIAware()
    pygame.display.set_caption('BattleBase')

    settings = Settings()
    screen = pygame.display.set_mode(settings.resolution)
    registry = Registry(settings.resolution)
    audio = AudioManager()
    main_menu = MainMenu(settings, registry, audio, screen)
    main_menu.show_menu()
    return main_menu.is_reboot

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
# Точка старта
if __name__ == "__main__":
    reboot = start_game()
    while reboot:
        reboot = start_game()
