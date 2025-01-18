from bin.characters.character import Character


class Swordsman(Character):
    def __init__(self, res, settings, name='archer_blue', pos=(0, 0)):
        super().__init__(res, settings, name='archer_blue', pos=pos)

    def update(self, mouse_pos, all_bullets):
        super().update(mouse_pos, all_bullets)
