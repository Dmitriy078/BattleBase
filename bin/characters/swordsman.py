from bin.characters.character import Character


class Swordsman(Character):
    def __init__(self, res, settings, audio_player, name='archer_blue', pos=(0, 0)):
        super().__init__(res, settings, audio_player, name='archer_blue', pos=pos)

    def update(self, mouse_pos, all_bullets, camera):
        super().update(mouse_pos, all_bullets, camera)
