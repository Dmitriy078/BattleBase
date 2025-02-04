from bin.bullets.arrow import Arrow
from bin.characters.character import Character


# класс лучника
class Archer(Character):
    def __init__(self, res, settings, audio_player, name='archer_blue', pos=(0,0)):
        super().__init__(res, settings, audio_player, name=name, pos=pos)

    # обнавление
    def update(self, mouse_pos, all_bullets, camera, solid_objects):
        super().update(mouse_pos, all_bullets, camera, solid_objects)

        if self.status == 'attack':
            if (self.current_frame == len(self.res.textures[self.name][self.direction][self.status]['frames']) - 2
                    and self.time == 0):
                x = self.x + self.rect.width // 2
                y = self.y + self.rect.height * 0.4
                mouse_pos = (mouse_pos[0] - camera.dx, mouse_pos[1] - camera.dy)
                if x < mouse_pos[0]:
                    self.direction = 'right'
                else:
                    self.direction = 'left'
                arrow = Arrow(self.res, self.settings, self.audio_player, pos=(x, y), target_point=mouse_pos)
                all_bullets.add(arrow)
