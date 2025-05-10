import math
import random

import pygame

from bin.characters.character import Character
from bin.ui.has_path import has_path


# класс сапорта
class Support(Character):
    def __init__(self, res, settings, audio_player, name='support_blue', pos=(0, 0)):
        super().__init__(res, settings, audio_player, name=name, pos=pos)

    def update(self, mouse_pos, all_bullets, camera, solid_objects, is_ai=False):
        super().update(mouse_pos, all_bullets, camera, solid_objects, is_ai)

        if self.health > 0 and is_ai:
            self.ai_controller()

    # Контроллер имитирующий искусственный интеллект
    def ai_controller(self):
        pass
