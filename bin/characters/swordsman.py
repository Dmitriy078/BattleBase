from bin.characters.character import Character


# класс мечника
class Swordsman(Character):
    def __init__(self, res, settings, audio_player, name='warrior_blue', pos=(0, 0)):
        super().__init__(res, settings, audio_player, name=name, pos=pos)


    def ai_controller(self):
        pass
