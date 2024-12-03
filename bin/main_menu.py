import os
class MainMenu:
    def __init__(self, settings):
        self.settings = settings
        self.is_reboot = False


        if not os.path.exists("data"):
            os.makedirs("data")

    def show_menu(self):
        pass