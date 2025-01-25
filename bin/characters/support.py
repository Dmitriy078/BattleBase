from bin.characters.character import Character


# класс сапорта
class Support(Character):
    def __init__(self, res, settings, audio_player, name='support_blue', pos=(0, 0)):
        super().__init__(res, settings, audio_player, name='support_blue', pos=pos)