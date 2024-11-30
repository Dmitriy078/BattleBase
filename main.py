from bin.settings import Settings
from bin.main_menu import MainMenu


if __name__ == "__main__":
    settings = Settings()
    main_menu = MainMenu(settings)
    main_menu.show_menu()

    if main_menu.is_reboot:
        settings = Settings()
        main_menu = MainMenu(settings)
        main_menu.show_menu()
