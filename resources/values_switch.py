from source.ui.text import Text
from source.ui.button import Button


# Класс переключателя значения для большого количества
class ValuesSwitch:
    # Инициализация параметров
    def __init__(self, texture, values, select_value, x, y, width, height, font, font_size, center_text,
                 offset_text_x,
                 offset_text_y,
                 texture_button, texture_button_motion, texture_button_press, offset_text_press_x, offset_text_press_y,
                 audio_player):
        self.values = values
        if select_value in self.values:
            self.pos_value = self.values.index(select_value)
        elif self.values:
            self.pos_value = 0
        else:
            self.pos_value = -1

        if self.pos_value in range(len(self.values)):
            text = self.values[self.pos_value]
        else:
            text = 'Не указано'

        self.value_text = Text(texture=texture,
                               text=text,
                               x=x,
                               y=y,
                               width=width,
                               height=height,
                               font=font,
                               font_size=font_size,
                               center_text=center_text,
                               offset_text_x=offset_text_x,
                               offset_text_y=offset_text_y)

        self.button_left = Button(texture=texture_button,
                                  texture_motion=texture_button_motion,
                                  texture_press=texture_button_press,
                                  text='<=',
                                  x=(x - texture_button.get_width() - (texture_button.get_width() * 0.1)),
                                  y=y,
                                  width=texture_button.get_width(),
                                  height=texture_button.get_height(),
                                  font=font,
                                  font_size=font_size,
                                  center_text=True,
                                  offset_text_x=offset_text_x,
                                  offset_text_y=offset_text_y,
                                  offset_text_press_x=offset_text_press_x,
                                  offset_text_press_y=offset_text_press_y,
                                  audio_player=audio_player)

        self.button_right = Button(texture=texture_button,
                                   texture_motion=texture_button_motion,
                                   texture_press=texture_button_press,
                                   text='=>',
                                   x=(x + texture.get_width() + (texture_button.get_width() * 0.1)),
                                   y=y,
                                   width=texture_button.get_width(),
                                   height=texture_button.get_height(),
                                   font=font,
                                   font_size=font_size,
                                   center_text=True,
                                   offset_text_x=offset_text_x,
                                   offset_text_y=offset_text_y,
                                   offset_text_press_x=offset_text_press_x,
                                   offset_text_press_y=offset_text_press_y,
                                   audio_player=audio_player)

    # Отрисовка переключателя
    def draw(self, screen):
        self.value_text.draw(screen)
        self.button_left.draw(screen)
        self.button_right.draw(screen)

    # Обновление значения
    def update(self, is_click, mouse_pos):
        self.button_left.update(is_click, mouse_pos)
        if self.button_left.is_up:
            if self.pos_value > 0:
                self.pos_value -= 1

        self.button_right.update(is_click, mouse_pos)
        if self.button_right.is_up:
            if self.pos_value < len(self.values) - 1:
                self.pos_value += 1

        if self.pos_value > -1:
            self.value_text.set_text(self.get_value())

    # Получение текущего значения
    def get_value(self):
        if self.pos_value > -1:
            return self.values[self.pos_value]
        else:
            return None
