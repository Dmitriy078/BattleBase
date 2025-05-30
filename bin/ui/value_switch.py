from bin.ui.button import Button


# Класс переключателя значения для маленького количества
class ValueSwitch:
    # Инициализация параметров
    def __init__(self, texture, texture_press, values, select_value, x, y, width, height, font,
                 font_size, center_text, offset_text_x, offset_text_y, offset_text_press_x, offset_text_press_y,
                 audio_player):
        self.values = values
        if select_value in self.values:
            self.pos_value = self.values.index(select_value)
        elif self.values:
            self.pos_value = 0
        else:
            self.pos_value = -1
        self.call = None
        if self.pos_value in range(len(self.values)):
            text = self.values[self.pos_value]
        else:
            text = 'Не указано'

        self.value_text = Button(texture=texture,
                                 texture_press=texture_press,
                                 text=text,
                                 x=x,
                                 y=y,
                                 width=width,
                                 height=height,
                                 text_color_rgb=(138, 9, 47),

                                 font=font,
                                 font_size=font_size,
                                 center_text=center_text,
                                 offset_text_x=offset_text_x,
                                 offset_text_y=offset_text_y,
                                 offset_text_press_x=offset_text_press_x,
                                 offset_text_press_y=offset_text_press_y,
                                 audio_player=audio_player)
        self.value_text.call = self.click

    # Отрисовка переключателя
    def draw(self, screen):
        self.value_text.draw(screen)

    # Обновление значения
    def update(self, is_click, mouse_pos):
        self.value_text.update(is_click, mouse_pos)

        if self.pos_value > -1:
            self.value_text.set_text(self.get_value())

    def click(self):
        if self.pos_value > -1:
            self.pos_value += 1
        if self.pos_value >= len(self.values):
            self.pos_value = 0
        if self.call:
            self.call()

    # Получение значения
    def get_value(self):
        if self.pos_value > -1:
            return self.values[self.pos_value]
        else:
            return None
