from config import *


class Sounds(Config):

    def __init__(self):
        super().__init__()
        self._bg_sound = pg.mixer.Sound('sounds/bg.mp3')

    def bg_sound(self):
        self._bg_sound.set_volume(BG_MUSIC_VALUE)
        if not self._end_game:
            self._bg_sound.play(-1)
        else:
            self._bg_sound.stop()

    @staticmethod
    def ball_sound():
        pg.mixer.music.load('sounds/ball.mp3')
        pg.mixer.music.play(1)

    @staticmethod
    def loose_sound():
        pg.mixer.music.load('sounds/loose.mp3')
        pg.mixer.music.play(1)
