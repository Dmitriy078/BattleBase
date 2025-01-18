from bin.buttons.arrow import Arrow
from bin.characters.character import Character


class Archer(Character):
    def __init__(self, res, settings, name='archer_blue', pos=(0,0)):
        super().__init__(res, settings, name='archer_blue', pos=pos)
        
    def update(self, mouse_pos, all_bullets):
        super().update(mouse_pos, all_bullets)

        if self.status == 'attack':
            if (self.current_frame == len(self.res.textures[self.name][self.direction][self.status]['frames']) - 2
                    and self.time == 0):
                x = self.x + self.rect.width // 2
                y = self.y + self.rect.height * 0.4
                arrow = Arrow(self.res, self.settings, pos=(x, y), target_point=mouse_pos)
                all_bullets.add(arrow)
