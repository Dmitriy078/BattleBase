from bin.characters.character import Character


class Archer(Character):
    def __init__(self, res, settings, name='archer_blue', pos=(0,0)):
        super().__init__(res, settings, name='archer_blue', pos=pos)
        
    def update(self):
        super().update()
