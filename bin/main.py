from bin.settings import Settings
from bin.main_menu import MainMenu
import pygame

if __name__ == "__main__":
    pygame.init()
    settings = Settings()
    main_menu = MainMenu(settings)
    main_menu.show_menu()

    if main_menu.is_reboot:
        pygame.init()
        settings = Settings()
        main_menu = MainMenu(settings)
        main_menu.show_menu()
