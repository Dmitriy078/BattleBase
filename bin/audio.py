from pygame import mixer


# Класс аудио-менеджера для проигрывания музыки и звуков
class AudioManager:
    # Инициализация свойств
    def __init__(self):
        mixer.init()
        self.music_volume = 0.5
        self.sound_volume = 0.5

    # Функция проигрывания музыки
    def play_music(self, file_path, repeat=True):
        mixer.music.load(file_path)
        mixer.music.set_volume(self.music_volume)
        if repeat:
            mixer.music.play(-1)
        else:
            mixer.music.play()

    # Функция остановки проигрывания музыки
    def stop_music(self):
        mixer.music.stop()

    # Функция установки громкости музыки
    def set_music_volume(self, volume):
        self.music_volume = volume
        mixer.music.set_volume(self.music_volume)

    # Функция проигрывания звуков
    def play_sound(self, file_path):
        sound = mixer.Sound(file_path)
        sound.set_volume(self.sound_volume)
        sound.play()

    # Установка громкости звуков
    def set_sound_volume(self, volume):
        self.sound_volume = volume